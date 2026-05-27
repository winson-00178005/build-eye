"""Build-Eye 通知模块 - 支持飞书、钉钉、邮件通知。"""
import hashlib
import hmac
import base64
import json
import smtplib
import time
import urllib.request
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List, Optional


def _feishu_sign(secret: str, timestamp: str) -> str:
    string_to_sign = f"{timestamp}\n{secret}"
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    return base64.b64encode(hmac_code).decode("utf-8")


def send_feishu(webhook_url: str, title: str, content: str, sign_secret: str = "") -> bool:
    timestamp = str(int(time.time()))
    url = webhook_url
    if sign_secret:
        sign = _feishu_sign(sign_secret, timestamp)
        url = f"{webhook_url}&timestamp={timestamp}&sign={sign}"

    message = {
        "msg_type": "interactive",
        "card": {
            "header": {"title": {"tag": "plain_text", "content": title}},
            "elements": [{"tag": "markdown", "content": content}],
        },
    }

    try:
        data = json.dumps(message).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("StatusCode") == 0 or result.get("code") == 0
    except Exception as e:
        print(f"Feishu notification failed: {e}")
        return False


def _dingtalk_sign(secret: str, timestamp: str) -> str:
    string_to_sign = f"{timestamp}\n{secret}"
    hmac_code = hmac.new(secret.encode("utf-8"), string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    return urllib.parse.quote_plus(base64.b64encode(hmac_code).decode("utf-8"))


def send_dingtalk(webhook_url: str, title: str, content: str, sign_secret: str = "") -> bool:
    timestamp = str(int(time.time() * 1000))
    url = webhook_url
    if sign_secret:
        sign = _dingtalk_sign(sign_secret, timestamp)
        url = f"{webhook_url}&timestamp={timestamp}&sign={sign}"

    message = {"msgtype": "markdown", "markdown": {"title": title, "text": content}}

    try:
        data = json.dumps(message).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("errcode") == 0
    except Exception as e:
        print(f"DingTalk notification failed: {e}")
        return False


def send_email(
    smtp_host: str,
    smtp_port: int,
    smtp_user: str,
    smtp_password: str,
    to_addresses: List[str],
    subject: str,
    content: str,
    use_ssl: bool = True,
) -> bool:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = ", ".join(to_addresses)
    html_part = MIMEText(content, "html", "utf-8")
    msg.attach(html_part)

    try:
        if use_ssl:
            server = smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=10)
        else:
            server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
            server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_addresses, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Email notification failed: {e}")
        return False


def send_notification(config: Dict, title: str, content_md: str, content_html: str) -> Dict:
    results = {}

    feishu_url = config.get("feishu_webhook_url", "")
    if feishu_url:
        ok = send_feishu(feishu_url, title, content_md, config.get("feishu_sign_secret", ""))
        results["feishu"] = ok

    dingtalk_url = config.get("dingtalk_webhook_url", "")
    if dingtalk_url:
        ok = send_dingtalk(dingtalk_url, title, content_md, config.get("dingtalk_sign_secret", ""))
        results["dingtalk"] = ok

    smtp_host = config.get("smtp_host", "")
    smtp_to = config.get("smtp_to", "")
    if smtp_host and smtp_to:
        ok = send_email(
            smtp_host,
            int(config.get("smtp_port", 465)),
            config.get("smtp_user", ""),
            config.get("smtp_password", ""),
            [e.strip() for e in smtp_to.split(",") if e.strip()],
            title,
            content_html,
            use_ssl=config.get("smtp_ssl", "true").lower() == "true",
        )
        results["email"] = ok

    return results


def format_report_notification(report_type: str, summary: Dict, failures: List[Dict], report_url: str) -> tuple:
    total = summary.get("total_runs", 0)
    success = summary.get("success_runs", 0)
    failure = summary.get("failure_runs", 0)
    rate = summary.get("overall_success_rate", 0)

    title = f"Build-Eye {report_type} Report"

    md = f"**{title}**\n\n- Total: {total} | Success: {success} | Failed: {failure} | Rate: {rate}%\n\n"
    if failures[:5]:
        md += "**Top Failures**:\n"
        for f in failures[:5]:
            name = f.get("workflow_name", "N/A")
            cat = f.get("classification", "N/A")
            key_err = (f.get("key_errors") or ["N/A"])[0]
            md += f"- {name} ({cat}): `{key_err[:60]}`\n"
    md += f"\n[View Full Report]({report_url})"

    html = f"""<div style="font-family:sans-serif;background:#f6f8fa;padding:16px;border-radius:8px">
<h2 style="color:#1f6feb">{title}</h2>
<p>Total: {total} | Success: {success} | Failed: {failure} | Rate: {rate}%</p>
<table style="border-collapse:collapse;width:100%"><tr style="background:#161b22;color:#c9d1d9">
<th style="padding:8px;border:1px solid #30363d">Workflow</th>
<th style="padding:8px;border:1px solid #30363d">Root Cause</th>
<th style="padding:8px;border:1px solid #30363d">Key Error</th></tr>"""
    for f in failures[:5]:
        html += f"""<tr style="background:#0d1117;color:#c9d1d9">
<td style="padding:6px;border:1px solid #21262d">{f.get('workflow_name','N/A')}</td>
<td style="padding:6px;border:1px solid #21262d">{f.get('classification','N/A')}</td>
<td style="padding:6px;border:1px solid #21262d;font-family:monospace;font-size:12px">{(f.get('key_errors') or ['N/A'])[0][:60]}</td></tr>"""
    html += f"""</table><p style="margin-top:12px"><a href="{report_url}" style="color:#58a6ff">View Full Report</a></p></div>"""

    return title, md, html