"""告警规则引擎 - 根据构建指标评估告警条件。"""
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone


class AlertRule:
    """告警规则定义。"""

    def __init__(self, rule_id: str, name: str, condition: str, threshold: float,
                 pipeline_type: str = "", severity: str = "warning",
                 channels: List[str] = None, cooldown_minutes: int = 60):
        self.rule_id = rule_id
        self.name = name
        self.condition = condition
        self.threshold = threshold
        self.pipeline_type = pipeline_type
        self.severity = severity
        self.channels = channels or ["webhook"]
        self.cooldown_minutes = cooldown_minutes


class AlertEngine:
    """告警引擎 - 评估告警规则并触发通知。"""

    SEVERITY_LEVELS = {"critical": 3, "warning": 2, "info": 1}

    DEFAULT_RULES = [
        AlertRule("R001", "连续构建失败", "consecutive_failures", 2,
                  pipeline_type="", severity="critical", channels=["webhook"]),
        AlertRule("R002", "健康评分过低", "health_score_below", 70,
                  pipeline_type="", severity="warning", channels=["webhook"]),
        AlertRule("R003", "成功率骤降", "success_rate_drop", 20,
                  pipeline_type="", severity="warning", channels=["webhook"]),
        AlertRule("R004", "基础设施连续失败", "consecutive_failures", 1,
                  pipeline_type="nightly", severity="critical", channels=["webhook"]),
    ]

    def __init__(self, rules: List[AlertRule] = None, cooldown_tracker: Dict = None):
        self.rules = rules or self.DEFAULT_RULES
        self._cooldown_tracker = cooldown_tracker or {}
        self._triggered_alerts: List[Dict[str, Any]] = []

    def evaluate(self, metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """评估所有告警规则，返回触发的告警列表。"""
        triggered = []

        for rule in self.rules:
            alert = self._evaluate_rule(rule, metrics)
            if alert:
                triggered.append(alert)

        self._triggered_alerts.extend(triggered)
        return triggered

    def _evaluate_rule(self, rule: AlertRule, metrics: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """评估单个规则。"""
        value = self._extract_metric(rule.condition, metrics, rule.pipeline_type)

        if value is None:
            return None

        should_trigger = False

        if rule.condition == "consecutive_failures":
            should_trigger = value >= rule.threshold
        elif rule.condition == "health_score_below":
            should_trigger = value < rule.threshold
        elif rule.condition == "success_rate_drop":
            should_trigger = value >= rule.threshold

        if not should_trigger:
            return None

        if self._is_in_cooldown(rule.rule_id):
            return None

        self._cooldown_tracker[rule.rule_id] = datetime.now(timezone.utc)

        return {
            "alert_id": f"{rule.rule_id}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
            "rule_id": rule.rule_id,
            "rule_name": rule.name,
            "severity": rule.severity,
            "condition": rule.condition,
            "threshold": rule.threshold,
            "actual_value": value,
            "pipeline_type": rule.pipeline_type,
            "channels": rule.channels,
            "message": self._format_message(rule, value),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def _extract_metric(self, condition: str, metrics: Dict[str, Any],
                        pipeline_type: str) -> Optional[float]:
        """从指标数据中提取告警条件对应的值。"""
        if condition == "consecutive_failures":
            if pipeline_type:
                return metrics.get(f"consecutive_failures_{pipeline_type}")
            return metrics.get("consecutive_failures", metrics.get("consecutive_failures_nightly"))

        if condition == "health_score_below":
            if pipeline_type:
                return metrics.get(f"health_score_{pipeline_type}")
            return metrics.get("health_score", metrics.get("health_score_nightly"))

        if condition == "success_rate_drop":
            current = metrics.get("success_rate_current", 0)
            previous = metrics.get("success_rate_previous", 0)
            if current > 0 and previous > 0:
                return previous - current
            return None

        return None

    def _format_message(self, rule: AlertRule, value: float) -> str:
        """格式化告警消息。"""
        if rule.condition == "consecutive_failures":
            pipeline = rule.pipeline_type or "所有"
            return f"⚠️ {pipeline}流水线连续{int(value)}次构建失败，请检查！"
        elif rule.condition == "health_score_below":
            pipeline = rule.pipeline_type or "整体"
            return f"⚠️ {pipeline}健康评分仅{value}分，低于阈值{rule.threshold}分！"
        elif rule.condition == "success_rate_drop":
            return f"⚠️ 成功率骤降{value}%，请关注！"
        return f"⚠️ 告警: {rule.name}"

    def _is_in_cooldown(self, rule_id: str) -> bool:
        """检查规则是否在冷却期。"""
        if rule_id not in self._cooldown_tracker:
            return False
        last_trigger = self._cooldown_tracker[rule_id]
        rule = next((r for r in self.rules if r.rule_id == rule_id), None)
        if not rule:
            return False
        from datetime import timedelta
        cooldown_end = last_trigger + timedelta(minutes=rule.cooldown_minutes)
        return datetime.now(timezone.utc) < cooldown_end

    def get_triggered_alerts(self) -> List[Dict[str, Any]]:
        """获取所有已触发的告警。"""
        return self._triggered_alerts

    def clear_alerts(self):
        """清除告警记录。"""
        self._triggered_alerts = []

    def load_rules_from_config(self, config_path: str | Path) -> List[AlertRule]:
        """从配置文件加载告警规则。"""
        path = Path(config_path)
        if not path.exists():
            return self.DEFAULT_RULES

        data = json.loads(path.read_text(encoding="utf-8"))
        rules = []

        for item in data.get("rules", []):
            rule = AlertRule(
                rule_id=item.get("rule_id", ""),
                name=item.get("name", ""),
                condition=item.get("condition", ""),
                threshold=item.get("threshold", 0),
                pipeline_type=item.get("pipeline_type", ""),
                severity=item.get("severity", "warning"),
                channels=item.get("channels", ["webhook"]),
                cooldown_minutes=item.get("cooldown_minutes", 60)
            )
            rules.append(rule)

        self.rules = rules
        return rules