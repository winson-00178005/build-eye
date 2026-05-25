"""告警模块测试。"""
import json
import tempfile
from pathlib import Path
from scripts.alert.alarm import AlertEngine, AlertRule
from scripts.alert.notifier import (
    NotificationDispatcher, WebhookNotifier, DingTalkNotifier,
    LarkNotifier, EmailNotifier
)


class TestAlertEngine:

    def test_no_alert_when_below_threshold(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures": 1}
        alerts = engine.evaluate(metrics)
        assert len(alerts) == 0

    def test_consecutive_failures_alert(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures": 3}
        alerts = engine.evaluate(metrics)
        assert len(alerts) >= 1
        assert alerts[0]["condition"] == "consecutive_failures"
        assert alerts[0]["actual_value"] == 3

    def test_health_score_below_alert(self):
        engine = AlertEngine()
        metrics = {"health_score": 60}
        alerts = engine.evaluate(metrics)
        health_alerts = [a for a in alerts if a["condition"] == "health_score_below"]
        assert len(health_alerts) >= 1
        assert health_alerts[0]["actual_value"] == 60

    def test_success_rate_drop_alert(self):
        engine = AlertEngine()
        metrics = {"success_rate_current": 50, "success_rate_previous": 85}
        alerts = engine.evaluate(metrics)
        drop_alerts = [a for a in alerts if a["condition"] == "success_rate_drop"]
        assert len(drop_alerts) >= 1
        assert drop_alerts[0]["actual_value"] == 35

    def test_no_drop_alert_when_rate_improves(self):
        engine = AlertEngine()
        metrics = {"success_rate_current": 90, "success_rate_previous": 80}
        alerts = engine.evaluate(metrics)
        drop_alerts = [a for a in alerts if a["condition"] == "success_rate_drop"]
        assert len(drop_alerts) == 0

    def test_severity_mapping(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures": 3}
        alerts = engine.evaluate(metrics)
        cf_alert = next(a for a in alerts if a["condition"] == "consecutive_failures")
        assert cf_alert["severity"] == "critical"

    def test_alert_message_format(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures": 3}
        alerts = engine.evaluate(metrics)
        assert len(alerts) >= 1
        assert "连续" in alerts[0]["message"]

    def test_cooldown_suppresses_duplicate(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures": 3}
        first = engine.evaluate(metrics)
        assert len(first) >= 1
        second = engine.evaluate(metrics)
        assert len(second) == 0

    def test_pipeline_type_specific_alert(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures_nightly": 1}
        alerts = engine.evaluate(metrics)
        nightly_alerts = [a for a in alerts if a["pipeline_type"] == "nightly"]
        assert len(nightly_alerts) >= 1

    def test_load_rules_from_config(self):
        config = {
            "rules": [
                {
                    "rule_id": "C001",
                    "name": "自定义规则",
                    "condition": "consecutive_failures",
                    "threshold": 5,
                    "pipeline_type": "pr",
                    "severity": "info",
                    "channels": ["webhook"]
                }
            ]
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(config, f)
            config_path = f.name

        engine = AlertEngine()
        rules = engine.load_rules_from_config(config_path)
        assert len(rules) == 1
        assert rules[0].rule_id == "C001"
        assert rules[0].threshold == 5
        Path(config_path).unlink(missing_ok=True)

    def test_clear_alerts(self):
        engine = AlertEngine()
        metrics = {"consecutive_failures": 3}
        engine.evaluate(metrics)
        assert len(engine.get_triggered_alerts()) >= 1
        engine.clear_alerts()
        assert len(engine.get_triggered_alerts()) == 0


class TestNotificationDispatcher:

    def test_webhook_notifier_no_url(self):
        notifier = WebhookNotifier()
        result = notifier.send({"alert_id": "test-1", "message": "test alert"})
        assert result["channel"] == "webhook"
        assert result["status"] == "logged"

    def test_dingtalk_notifier_no_url(self):
        notifier = DingTalkNotifier()
        result = notifier.send({"alert_id": "test-1", "message": "test alert"})
        assert result["channel"] == "dingtalk"
        assert result["status"] == "skipped"

    def test_lark_notifier_no_url(self):
        notifier = LarkNotifier()
        result = notifier.send({"alert_id": "test-1", "message": "test alert"})
        assert result["channel"] == "lark"
        assert result["status"] == "skipped"

    def test_email_notifier_no_recipients(self):
        notifier = EmailNotifier()
        result = notifier.send({"alert_id": "test-1", "message": "test alert"})
        assert result["channel"] == "email"
        assert result["status"] == "skipped"

    def test_dispatcher_dispatch_to_webhook(self):
        dispatcher = NotificationDispatcher({"webhook": {"url": ""}})
        alert = {
            "alert_id": "test-1",
            "channels": ["webhook"],
            "message": "test alert",
            "severity": "warning",
            "rule_name": "test rule"
        }
        results = dispatcher.dispatch(alert)
        assert len(results) == 1
        assert results[0]["channel"] == "webhook"

    def test_dispatcher_dispatch_to_multiple_channels(self):
        dispatcher = NotificationDispatcher({
            "webhook": {"url": ""},
            "email": {"recipients": []}
        })
        alert = {
            "alert_id": "test-1",
            "channels": ["webhook", "email"],
            "message": "test alert",
            "severity": "warning",
            "rule_name": "test rule"
        }
        results = dispatcher.dispatch(alert)
        assert len(results) == 2

    def test_dispatcher_skip_unconfigured_channel(self):
        dispatcher = NotificationDispatcher()
        alert = {
            "alert_id": "test-1",
            "channels": ["dingtalk"],
            "message": "test alert"
        }
        results = dispatcher.dispatch(alert)
        assert len(results) == 1
        assert results[0]["status"] == "skipped"

    def test_dispatcher_load_config(self):
        config = {
            "channels": {
                "webhook": {"url": "https://example.com/webhook"},
                "email": {"recipients": ["admin@example.com"]}
            }
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(config, f)
            config_path = f.name

        dispatcher = NotificationDispatcher()
        dispatcher.load_config(config_path)
        assert "webhook" in dispatcher.channels
        assert "email" in dispatcher.channels
        Path(config_path).unlink(missing_ok=True)

    def test_dispatch_all_alerts(self):
        dispatcher = NotificationDispatcher({"webhook": {"url": ""}})
        alerts = [
            {"alert_id": "test-1", "channels": ["webhook"], "message": "alert 1"},
            {"alert_id": "test-2", "channels": ["webhook"], "message": "alert 2"},
        ]
        results = dispatcher.dispatch_all(alerts)
        assert len(results) == 2

    def test_webhook_payload_format(self):
        notifier = WebhookNotifier()
        alert = {
            "alert_id": "R001-20260522030000",
            "rule_name": "连续构建失败",
            "severity": "critical",
            "message": "⚠️ 流水线连续3次构建失败",
            "actual_value": 3,
            "threshold": 2,
            "pipeline_type": "",
            "timestamp": "2026-05-22T03:00:00Z"
        }
        payload = notifier._format_payload(alert)
        assert "🔴" in payload["text"]
        assert payload["content"]["severity"] == "critical"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])