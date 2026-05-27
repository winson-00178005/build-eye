"""Build-Eye notification module - Feishu/DingTalk individual messages + Email."""
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


FEISHU_TOKEN_URL = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
FEISHU_SEND_URL = "https://open.feishu.cn/open-apis/message/v4/send"

DINGTALK_TOKEN_URL = "https://oapi.dingtalk.com/gettoken"
DINGTALK_SEND_URL = "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2"


def _feishu_get_tenant_token(app_id: str, app_secret: str) -> Optional[str]:
    payload = json.dumps({"app_id": app_id, "app_secret": app_secret}).encode("utf-8")
    req = urllib.request.Request(FEISHU_TOKEN_URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("code") == 0:
                return result.get("tenant_access_token")
            print(f"Feishu tenant token failed: {result.get('msg')}")
            return None
    except Exception as e:
        print(f"Feishu tenant token request failed: {e}")
        return None


def send_feishu(app_id: str, app_secret: str, receive_ids: List[str], title: str, content: str) -> Dict[str, bool]:
    token = _feishu_get_tenant_token(app_id, app_secret)
    if not token:
        return {rid: False for rid in receive_ids}

    results = {}
    for receive_id in receive_ids:
        msg_content = json.dumps({
            "config": {"wide_screen_mode": True},
            "header": {"title": {"tag": "plain_text", "content": title}},
            "elements": [{"tag": "markdown", "content": content}],
        })

        payload = json.dumps({
            "receive_id": receive_id,
            "msg_type": "interactive",
            "content": msg_content,
        }).encode("utf-8")

        req = urllib.request.Request(
            FEISHU_SEND_URL,
            data=payload,
            headers={"Content-Type": "application/json; charset=utf-8", "Authorization": f"Bearer {token}"},
        )

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                ok = result.get("code") == 0
                if not ok:
                    print(f"Feishu send to {receive_id} failed: {result.get('msg')}")
                results[receive_id] = ok
        except Exception as e:
            print(f"Feishu send to {receive_id} request failed: {e}")
            results[receive_id] = False

    return results


def _dingtalk_get_token(app_key: str, app_secret: str) -> Optional[str]:
    url = f"{DINGTALK_TOKEN_URL}?appkey={app_key}&appsecret={app_secret}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("errcode") == 0:
                return result.get("access_token")
            print(f"DingTalk access token failed: {result.get('errmsg')}")
            return None
    except Exception as e:
        print(f"DingTalk token request failed: {e}")
        return None


def send_dingtalk(app_key: str, app_secret: str, agent_id: str, receive_ids: List[str], title: str, content: str) -> Dict[str, bool]:
    token = _dingtalk_get_token(app_key, app_secret)
    if not token:
        return {rid: False for rid in receive_ids}

    results = {}
    for user_id in receive_ids:
        payload = json.dumps({
            "agent_id": agent_id,
            "userid_list": user_id,
            "msg": {
                "msgtype": "markdown",
                "markdown": {"title": title, "text": content},
            },
        }).encode("utf-8")

        req = urllib.request.Request(
            DINGTALK_SEND_URL,
            data=payload,
            headers={"Content-Type": "application/json", "x-acs-dingtalk-access-token": token},
        )

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                result = json.loads(resp.read().decode("utf-8"))
                ok = result.get("errcode") == 0
                if not ok:
                    print(f"DingTalk send to {user_id} failed: {result.get('errmsg')}")
                results[user_id] = ok
        except Exception as e:
            print(f"DingTalk send to {user_id} request failed: {e}")
            results[user_id] = False

    return results


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


def _parse_ids(id_str: str) -> List[str]:
    return [s.strip() for s in id_str.split(",") if s.strip()]


def send_notification(config: Dict, title: str, content_md: str, content_html: str) -> Dict:
    results = {}

    feishu_app_id = config.get("feishu_app_id", "")
    feishu_app_secret = config.get("feishu_app_secret", "")
    feishu_receive_ids = config.get("feishu_receive_ids", "")
    if feishu_app_id and feishu_app_secret and feishu_receive_ids:
        ids = _parse_ids(feishu_receive_ids)
        per_user = send_feishu(feishu_app_id, feishu_app_secret, ids, title, content_md)
        results["feishu"] = per_user

    dingtalk_app_key = config.get("dingtalk_app_key", "")
    dingtalk_app_secret = config.get("dingtalk_app_secret", "")
    dingtalk_agent_id = config.get("dingtalk_agent_id", "")
    dingtalk_receive_ids = config.get("dingtalk_receive_ids", "")
    if dingtalk_app_key and dingtalk_app_secret and dingtalk_agent_id and dingtalk_receive_ids:
        ids = _parse_ids(dingtalk_receive_ids)
        per_user = send_dingtalk(dingtalk_app_key, dingtalk_app_secret, dingtalk_agent_id, ids, title, content_md)
        results["dingtalk"] = per_user

    smtp_host = config.get("smtp_host", "")
    smtp_to = config.get("smtp_to", "")
    if smtp_host and smtp_to:
        per_addr = send_email(
            smtp_host,
            int(config.get("smtp_port", 465)),
            config.get("smtp_user", ""),
            config.get("smtp_password", ""),
            _parse_ids(smtp_to),
            title,
            content_html,
            use_ssl=config.get("smtp_ssl", "true").lower() == "true",
        )
        results["email"] = per_addr

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