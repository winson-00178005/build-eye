"""Build-Eye 通知模块 CLI - 从环境变量或命令行发送通知，支持多收件人。"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from notify.notifier import send_notification, format_report_notification


def _parse_ids(id_str: str) -> list:
    return [s.strip() for s in id_str.split(",") if s.strip()]


def load_config_from_env() -> dict:
    return {
        "feishu_app_id": os.environ.get("FEISHU_APP_ID", ""),
        "feishu_app_secret": os.environ.get("FEISHU_APP_SECRET", ""),
        "feishu_receive_ids": os.environ.get("FEISHU_RECEIVE_IDS", ""),
        "dingtalk_app_key": os.environ.get("DINGTALK_APP_KEY", ""),
        "dingtalk_app_secret": os.environ.get("DINGTALK_APP_SECRET", ""),
        "dingtalk_agent_id": os.environ.get("DINGTALK_AGENT_ID", ""),
        "dingtalk_receive_ids": os.environ.get("DINGTALK_RECEIVE_IDS", ""),
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
    if config["feishu_app_id"] and config["feishu_app_secret"] and config["feishu_receive_ids"]:
        ids = _parse_ids(config["feishu_receive_ids"])
        enabled.append(f"飞书 ({len(ids)} 人)")
    if config["dingtalk_app_key"] and config["dingtalk_app_secret"] and config["dingtalk_agent_id"] and config["dingtalk_receive_ids"]:
        ids = _parse_ids(config["dingtalk_receive_ids"])
        enabled.append(f"钉钉 ({len(ids)} 人)")
    if config["smtp_host"] and config["smtp_to"]:
        ids = _parse_ids(config["smtp_to"])
        enabled.append(f"邮件 ({len(ids)} 人)")

    if args.dry_run:
        print(f"已启用通知渠道: {enabled or '无'}")
        print(f"飞书: app_id={'已配置' if config['feishu_app_id'] else '未设置'}, 接收人={config['feishu_receive_ids'] or '未设置'}")
        print(f"钉钉: app_key={'已配置' if config['dingtalk_app_key'] else '未设置'}, agent_id={'已配置' if config['dingtalk_agent_id'] else '未设置'}, 接收人={config['dingtalk_receive_ids'] or '未设置'}")
        print(f"邮件: smtp={'已配置' if config['smtp_host'] else '未设置'}, 收件人={config['smtp_to'] or '未设置'}")
        return

    if not enabled:
        print("未配置任何通知渠道，跳过通知。")
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
            print(f"{channel}: 成功 {ok_count}/{len(detail)}, 失败 {fail_count}/{len(detail)}")
        else:
            status = "成功" if detail else "失败"
            print(f"{channel}: {status}")


if __name__ == "__main__":
    main()