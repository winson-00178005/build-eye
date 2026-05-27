"""Build-Eye notification CLI - supports multi-recipient via webhook/app."""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from notify.notifier import send_notification, format_report_notification


def _parse_ids(id_str: str) -> list:
    return [s.strip() for s in id_str.split(",") if s.strip()]


def load_config_from_env() -> dict:
    feishu_receive_ids = os.environ.get("FEISHU_RECEIVE_IDS", "")
    dingtalk_receive_ids = os.environ.get("DINGTALK_RECEIVE_IDS", "")
    return {
        "feishu_app_id": os.environ.get("FEISHU_APP_ID", ""),
        "feishu_app_secret": os.environ.get("FEISHU_APP_SECRET", ""),
        "feishu_receive_ids": feishu_receive_ids,
        "dingtalk_app_key": os.environ.get("DINGTALK_APP_KEY", ""),
        "dingtalk_app_secret": os.environ.get("DINGTALK_APP_SECRET", ""),
        "dingtalk_agent_id": os.environ.get("DINGTALK_AGENT_ID", ""),
        "dingtalk_receive_ids": dingtalk_receive_ids,
        "smtp_host": os.environ.get("SMTP_HOST", ""),
        "smtp_port": os.environ.get("SMTP_PORT", "465"),
        "smtp_user": os.environ.get("SMTP_USER", ""),
        "smtp_password": os.environ.get("SMTP_PASSWORD", ""),
        "smtp_to": os.environ.get("SMTP_TO", ""),
        "smtp_ssl": os.environ.get("SMTP_SSL", "true"),
    }


def main():
    parser = argparse.ArgumentParser(description="Build-Eye notification CLI")
    parser.add_argument("--config", help="Notification config JSON file path")
    parser.add_argument("--report-type", default="Nightly", help="Report type (Nightly/Weekly/PR)")
    parser.add_argument("--summary", help="Report summary JSON file (dashboard_data.json)")
    parser.add_argument("--report-url", help="Report URL")
    parser.add_argument("--title", help="Custom title")
    parser.add_argument("--content", help="Custom content (markdown)")
    parser.add_argument("--dry-run", action="store_true", help="Print config only, no send")
    args = parser.parse_args()

    config = load_config_from_env()
    if args.config:
        file_config = json.loads(open(args.config, encoding="utf-8").read())
        for k, v in file_config.items():
            if v and not config.get(k):
                config[k] = v

    enabled = []
    if config["feishu_app_id"] and config["feishu_app_secret"] and config["feishu_receive_ids"]:
        ids = _parse_ids(config["feishu_receive_ids"])
        enabled.append("Feishu (" + str(len(ids)) + " recipients)")
    if config["dingtalk_app_key"] and config["dingtalk_app_secret"] and config["dingtalk_agent_id"] and config["dingtalk_receive_ids"]:
        ids = _parse_ids(config["dingtalk_receive_ids"])
        enabled.append("DingTalk (" + str(len(ids)) + " recipients)")
    if config["smtp_host"] and config["smtp_to"]:
        ids = _parse_ids(config["smtp_to"])
        enabled.append("Email (" + str(len(ids)) + " recipients)")

    if args.dry_run:
        print("Notification channels enabled: " + str(enabled or []))
        feishu_status = "configured" if config["feishu_app_id"] else "not set"
        dingtalk_status = "configured" if config["dingtalk_app_key"] else "not set"
        dingtalk_agent_status = "configured" if config["dingtalk_agent_id"] else "not set"
        smtp_status = "configured" if config["smtp_host"] else "not set"
        print("Feishu: app_id=" + feishu_status + ", receive_ids=" + (config["feishu_receive_ids"] or "not set"))
        print("DingTalk: app_key=" + dingtalk_status + ", agent_id=" + dingtalk_agent_status + ", receive_ids=" + (config["dingtalk_receive_ids"] or "not set"))
        print("Email: smtp=" + smtp_status + ", to=" + (config["smtp_to"] or "not set"))
        return

    if not enabled:
        print("No notification channels configured. Skipping.")
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
    for channel, detail in results.items():
        if isinstance(detail, dict):
            ok_count = sum(1 for v in detail.values() if v)
            fail_count = sum(1 for v in detail.values() if not v)
            print(channel + ": success " + str(ok_count) + "/" + str(len(detail)) + ", failed " + str(fail_count) + "/" + str(len(detail)))
        else:
            status = "success" if detail else "failed"
            print(channel + ": " + status)


if __name__ == "__main__":
    main()