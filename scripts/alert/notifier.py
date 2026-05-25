"""多渠道通知器 - 将告警消息分发到不同通知渠道。"""
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


class NotificationChannel:
    """通知渠道基类。"""

    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}

    def send(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """发送告警通知。"""
        return {
            "channel": self.name,
            "status": "sent",
            "alert_id": alert.get("alert_id", ""),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }


class WebhookNotifier(NotificationChannel):
    """Webhook 通知渠道。"""

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("webhook", config)
        self.url = config.get("url", "") if config else ""

    def send(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """发送 Webhook 通知（记录到文件或调用 URL）。"""
        payload = self._format_payload(alert)

        if self.url:
            try:
                import requests
                resp = requests.post(self.url, json=payload, timeout=10)
                return {
                    "channel": "webhook",
                    "status": "sent" if resp.status_code < 300 else "failed",
                    "alert_id": alert.get("alert_id", ""),
                    "response_code": resp.status_code,
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
            except Exception as e:
                logger.warning(f"Webhook 发送失败: {e}")
                return {
                    "channel": "webhook",
                    "status": "failed",
                    "alert_id": alert.get("alert_id", ""),
                    "error": str(e),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }

        return {
            "channel": "webhook",
            "status": "logged",
            "alert_id": alert.get("alert_id", ""),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def _format_payload(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """格式化 Webhook payload。"""
        severity_emoji = {"critical": "🔴", "warning": "🟡", "info": "🟢"}
        emoji = severity_emoji.get(alert.get("severity", "warning"), "⚠️")

        return {
            "text": f"{emoji} Build-Eye 告警通知",
            "msg_type": "alert",
            "content": {
                "alert_id": alert.get("alert_id", ""),
                "rule_name": alert.get("rule_name", ""),
                "severity": alert.get("severity", ""),
                "message": alert.get("message", ""),
                "actual_value": alert.get("actual_value", 0),
                "threshold": alert.get("threshold", 0),
                "pipeline_type": alert.get("pipeline_type", ""),
                "timestamp": alert.get("timestamp", "")
            }
        }


class DingTalkNotifier(NotificationChannel):
    """钉钉通知渠道。"""

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("dingtalk", config)
        self.webhook_url = config.get("webhook_url", "") if config else ""
        self.secret = config.get("secret", "") if config else ""

    def send(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """发送钉钉机器人通知。"""
        if not self.webhook_url:
            return {
                "channel": "dingtalk",
                "status": "skipped",
                "reason": "no webhook_url configured",
                "alert_id": alert.get("alert_id", ""),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }

        payload = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"Build-Eye 告警: {alert.get('rule_name', '')}",
                "text": self._format_markdown(alert)
            }
        }

        try:
            import requests
            url = self.webhook_url
            if self.secret:
                import hashlib
                import hmac
                import time
                timestamp = str(round(time.time() * 1000))
                sign = hmac.new(self.secret.encode(), f"{timestamp}\n{self.secret}".encode(),
                                hashlib.sha256).digest()
                import base64
                sign_b64 = base64.b64encode(sign).decode()
                url = f"{url}&timestamp={timestamp}&sign={sign_b64}"

            resp = requests.post(url, json=payload, timeout=10)
            return {
                "channel": "dingtalk",
                "status": "sent" if resp.status_code < 300 else "failed",
                "alert_id": alert.get("alert_id", ""),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        except Exception as e:
            logger.warning(f"钉钉通知发送失败: {e}")
            return {
                "channel": "dingtalk",
                "status": "failed",
                "alert_id": alert.get("alert_id", ""),
                "error": str(e),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }

    def _format_markdown(self, alert: Dict[str, Any]) -> str:
        """格式化钉钉 Markdown 消息。"""
        severity_map = {"critical": "🔴 严重", "warning": "🟡 警告", "info": "🟢 提示"}
        severity_text = severity_map.get(alert.get("severity", "warning"), "⚠️")

        return (
            f"## Build-Eye 构建告警\n\n"
            f"**级别**: {severity_text}\n\n"
            f"**规则**: {alert.get('rule_name', '')}\n\n"
            f"**详情**: {alert.get('message', '')}\n\n"
            f"**时间**: {alert.get('timestamp', '')}\n\n"
        )


class LarkNotifier(NotificationChannel):
    """飞书通知渠道。"""

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("lark", config)
        self.webhook_url = config.get("webhook_url", "") if config else ""

    def send(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """发送飞书机器人通知。"""
        if not self.webhook_url:
            return {
                "channel": "lark",
                "status": "skipped",
                "reason": "no webhook_url configured",
                "alert_id": alert.get("alert_id", ""),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }

        payload = {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {"tag": "plain_text", "content": f"Build-Eye 告警: {alert.get('rule_name', '')}"},
                    "template": "red" if alert.get("severity") == "critical" else "yellow"
                },
                "elements": [
                    {"tag": "div", "text": {"tag": "lark_md", "content": alert.get("message", "")}},
                    {"tag": "div", "text": {"tag": "lark_md",
                                           "content": f"**时间**: {alert.get('timestamp', '')}"}}
                ]
            }
        }

        try:
            import requests
            resp = requests.post(self.webhook_url, json=payload, timeout=10)
            return {
                "channel": "lark",
                "status": "sent" if resp.status_code < 300 else "failed",
                "alert_id": alert.get("alert_id", ""),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        except Exception as e:
            logger.warning(f"飞书通知发送失败: {e}")
            return {
                "channel": "lark",
                "status": "failed",
                "alert_id": alert.get("alert_id", ""),
                "error": str(e),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }


class EmailNotifier(NotificationChannel):
    """邮件通知渠道。"""

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__("email", config)
        cfg = config or {}
        self.recipients = cfg.get("recipients", [])
        self.subject_prefix = cfg.get("subject_prefix", "[Build-Eye Alert]")

    def send(self, alert: Dict[str, Any]) -> Dict[str, Any]:
        """发送邮件通知（记录意图）。"""
        if not self.recipients:
            return {
                "channel": "email",
                "status": "skipped",
                "reason": "no recipients configured",
                "alert_id": alert.get("alert_id", ""),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }

        return {
            "channel": "email",
            "status": "prepared",
            "alert_id": alert.get("alert_id", ""),
            "recipients": self.recipients,
            "subject": f"{self.subject_prefix} {alert.get('rule_name', '')}",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }


class NotificationDispatcher:
    """通知分发器 - 将告警分发到多个通知渠道。"""

    CHANNEL_MAP = {
        "webhook": WebhookNotifier,
        "dingtalk": DingTalkNotifier,
        "lark": LarkNotifier,
        "email": EmailNotifier,
    }

    def __init__(self, channel_configs: Dict[str, Dict[str, Any]] = None):
        self.channels: Dict[str, NotificationChannel] = {}
        if channel_configs:
            for name, config in channel_configs.items():
                self.add_channel(name, config)

    def add_channel(self, name: str, config: Dict[str, Any] = None):
        """添加通知渠道。"""
        cls = self.CHANNEL_MAP.get(name, WebhookNotifier)
        self.channels[name] = cls(config)

    def dispatch(self, alert: Dict[str, Any]) -> List[Dict[str, Any]]:
        """将告警分发到所有指定渠道。"""
        target_channels = alert.get("channels", ["webhook"])
        results = []

        for channel_name in target_channels:
            channel = self.channels.get(channel_name)
            if channel:
                result = channel.send(alert)
                results.append(result)
            else:
                results.append({
                    "channel": channel_name,
                    "status": "skipped",
                    "reason": "channel not configured",
                    "alert_id": alert.get("alert_id", ""),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                })

        return results

    def dispatch_all(self, alerts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """分发所有告警。"""
        all_results = []
        for alert in alerts:
            results = self.dispatch(alert)
            all_results.extend(results)
        return all_results

    def load_config(self, config_path: str | Path) -> None:
        """从配置文件加载通知渠道配置。"""
        path = Path(config_path)
        if not path.exists():
            return

        data = json.loads(path.read_text(encoding="utf-8"))
        channels = data.get("channels", {})

        for name, config in channels.items():
            self.add_channel(name, config)