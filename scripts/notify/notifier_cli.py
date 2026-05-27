"""Build-Eye 通知模块 CLI - 从环境变量或命令行发送通知。"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from notify.notifier import send_notification, format_report_notification


def load_config_from_env() -> dict:
    return {
        "feishu_webhook_url": os.environ.get("FEISHU_WEBHOOK_URL", ""),
        "feishu_sign_secret": os.environ.get("FEISHU_SIGN_SECRET", ""),
        "dingtalk_webhook_url": os.environ.get("DINGTALK_WEBHOOK_URL", ""),
        "dingtalk_sign_secret": os.environ.get("DINGTALK_SIGN_SECRET", ""),
        "smtp_host": os.environ.get("SMTP_HOST", ""),
        "smtp_port": os.environ.get("SMTP_PORT", "465"),
        "smtp_user": os.environ.get("SMTP_USER", ""),
        "smtp_password": os.environ.get("SMTP_PASSWORD", ""),
        "smtp_to": os.environ.get("SMTP_TO", ""),
        "smtp_ssl": os.environ.get("SMTP_SSL", "true"),
    }


def main():
    parser = argparse.ArgumentParser(description="Build-Eye 通知发送工具")
    parser.add_argument("--config", help="通知配置 JSON 文件路径")
    parser.add_argument("--report-type", default="Nightly", help="报告类型 (Nightly/Weekly/PR)")
    parser.add_argument("--summary", help="报告摘要 JSON 文件 (dashboard_data.json)")
    parser.add_argument("--report-url", help="报告 URL")
    parser.add_argument("--title", help="自定义标题")
    parser.add_argument("--content", help="自定义内容 (markdown)")
    parser.add_argument("--dry-run", action="store_true", help="仅打印配置，不发送")
    args = parser.parse_args()

    config = load_config_from_env()
    if args.config:
        file_config = json.loads(open(args.config, encoding="utf-8").read())
        for k, v in file_config.items():
            if v and not config.get(k):
                config[k] = v

    enabled = []
    if config["feishu_webhook_url"]:
        enabled.append("Feishu")
    if config["dingtalk_webhook_url"]:
        enabled.append("DingTalk")
    if config["smtp_host"] and config["smtp_to"]:
        enabled.append("Email")

    if args.dry_run:
        print(f"Notification channels enabled: {enabled or 'None'}")
        print(f"Feishu: webhook={'configured' if config['feishu_webhook_url'] else 'not set'}")
        print(f"DingTalk: webhook={'configured' if config['dingtalk_webhook_url'] else 'not set'}")
        print(f"Email: smtp={'configured' if config['smtp_host'] else 'not set'}, to={config['smtp_to'] or 'not set'}")
        return

    if not enabled:
        print("No notification channels configured. Skipping notification.")
        return

    if args.summary:
        dashboard_data = json.loads(open(args.summary, encoding="utf-8").read())
        summary = dashboard_data.get("overview", {}).get("summary", {})
        all_failures = dashboard_data.get("recent_failures", {}).get("failures", [])
        ptype_map = {"Nightly": "nightly", "Weekly": "weekly", "PR": "pr"}
        ptype = ptype_map.get(args.report_type, "")
        if ptype:
            failures = [f for f in all_failures if f.get("pipeline_type") == ptype]
            pipeline_data = dashboard_data.get("overview", {}).get("pipelines", {}).get(ptype, {})
            summary = {
                "total_runs": pipeline_data.get("total_runs", 0),
                "success_runs": pipeline_data.get("success_runs", 0),
                "failure_runs": pipeline_data.get("failure_runs", 0),
                "overall_success_rate": pipeline_data.get("success_rate", 0),
            }
            report_url = pipeline_data.get("latest_report_url", "")
        else:
            failures = all_failures
            report_url = args.report_url or ""
        title, md, html = format_report_notification(args.report_type, summary, failures, report_url)
    elif args.title and args.content:
        title = args.title
        md = args.content
        html = args.content
    else:
        print("No content specified. Use --summary or --title + --content.")
        return

    results = send_notification(config, title, md, html)
    for channel, ok in results.items():
        status = "sent" if ok else "failed"
        print(f"{channel}: {status}")


if __name__ == "__main__":
    main()