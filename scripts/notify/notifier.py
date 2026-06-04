"""Build-Eye 通知模块 - 支持邮件通知，支持多收件人。"""
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List


def send_email(
    smtp_host: str,
    smtp_port: int,
    smtp_user: str,
    smtp_password: str,
    to_addresses: List[str],
    subject: str,
    content: str,
    use_ssl: bool = True,
) -> Dict[str, bool]:
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
        return {addr: True for addr in to_addresses}
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return {addr: False for addr in to_addresses}


def _parse_ids(id_str: str) -> List[str]:
    return [s.strip() for s in id_str.split(",") if s.strip()]


def send_notification(config: Dict, title: str, content_md: str, content_html: str) -> Dict:
    results = {}

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

    md = f"**{title}**\n\n- 总运行: {total} | 成功: {success} | 失败: {failure} | 成率: {rate}%\n\n"
    if failures[:5]:
        md += "**主要失败**:\n"
        for f in failures[:5]:
            name = f.get("workflow_name", "N/A")
            cat = f.get("classification", "N/A")
            key_err = (f.get("key_errors") or ["N/A"])[0]
            md += f"- {name} ({cat}): `{key_err[:60]}`\n"
    md += f"\n[查看完整报告]({report_url})"

    html = f"""<div style="font-family:sans-serif;background:#f6f8fa;padding:16px;border-radius:8px">
<h2 style="color:#1f6feb">{title}</h2>
<p>总运行: {total} | 成功: {success} | 失败: {failure} | 成率: {rate}%</p>
<table style="border-collapse:collapse;width:100%"><tr style="background:#161b22;color:#c9d1d9">
<th style="padding:8px;border:1px solid #30363d">工作流</th>
<th style="padding:8px;border:1px solid #30363d">根因</th>
<th style="padding:8px;border:1px solid #30363d">关键错误</th></tr>"""
    for f in failures[:5]:
        html += f"""<tr style="background:#0d1117;color:#c9d1d9">
<td style="padding:6px;border:1px solid #21262d">{f.get('workflow_name','N/A')}</td>
<td style="padding:6px;border:1px solid #21262d">{f.get('classification','N/A')}</td>
<td style="padding:6px;border:1px solid #21262d;font-family:monospace;font-size:12px">{(f.get('key_errors') or ['N/A'])[0][:60]}</td></tr>"""
    html += f"""</table><p style="margin-top:12px"><a href="{report_url}" style="color:#58a6ff">查看完整报告</a></p></div>"""

    return title, md, html