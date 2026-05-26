"""Nightly 日报生成器 - 每日定时流水线汇总报告。"""
import json
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any, List


class NightlyReportGenerator:
    """Nightly 流水线日报生成器。"""

    CATEGORY_LABELS = {
        "code": "代码问题",
        "infrastructure": "基础设施问题",
        "interference": "并发干扰"
    }

    STATUS_LABELS = {
        "success": "成功",
        "failure": "失败",
        "skipped": "跳过",
        "cancelled": "取消",
        "timed_out": "超时",
        "action_required": "需操作"
    }

    CONFIDENCE_LABELS = {
        "high": "高",
        "medium": "中",
        "low": "低"
    }

    def __init__(self, aggregator=None):
        self.aggregator = aggregator

    def generate_daily_report(self, nightly_runs: List[Dict], date_str: str = None) -> str:
        """生成 Nightly 日报。"""
        if not date_str:
            date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        report_id = str(uuid.uuid4())[:8]

        total_runs = len(nightly_runs)
        success_runs = sum(1 for r in nightly_runs if r.get("conclusion") == "success")
        failure_runs = total_runs - success_runs
        success_rate = (success_runs / max(total_runs, 1)) * 100

        avg_duration = self._calc_avg_duration(nightly_runs)

        frontmatter = self._generate_frontmatter(report_id, date_str, total_runs, success_runs, failure_runs)

        overview = self._generate_overview(total_runs, success_rate, avg_duration, failure_runs)

        failure_detail = self._generate_failure_details(nightly_runs)

        trend_section = ""
        if self.aggregator:
            trend_data = self.aggregator.get_trend_data("nightly", 7)
            if trend_data:
                trend_section = self._generate_trend(trend_data, success_rate)

        alert_section = self._generate_alert(nightly_runs)

        yesterday_comparison = ""
        if self.aggregator:
            yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
            yesterday_agg = self.aggregator.get_daily_aggregates("nightly", 2)
            if len(yesterday_agg) >= 1:
                yesterday_comparison = self._generate_comparison(yesterday_agg[-1], success_rate, avg_duration, total_runs)

        report = f"""{frontmatter}

# Nightly 构建报告 - {date_str}

{overview}

{yesterday_comparison}

{failure_detail}

{trend_section}

{alert_section}

---
报告生成时间: {datetime.now(timezone.utc).isoformat()}
"""

        return report

    def _generate_frontmatter(self, report_id, date_str, total, success, failure):
        """生成 YAML frontmatter。"""
        lines = [
            "---",
            f"report_id: {report_id}",
            f"report_type: nightly_daily",
            f"date: {date_str}",
            f"generated_at: {datetime.now(timezone.utc).isoformat()}",
            f"total_runs: {total}",
            f"success_runs: {success}",
            f"failure_runs: {failure}",
            "---"
        ]
        return "\n".join(lines)

    def _generate_overview(self, total, success_rate, avg_duration, failure_runs):
        """生成概览表格。"""
        avg_min = round(avg_duration / 60, 1) if avg_duration else 0
        lines = [
            "## 概览",
            "",
            "| 指标 | 数值 |",
            "|------|------|",
            f"| 运行总数 | {total} |",
            f"| 成功率 | {success_rate:.1f}% |",
            f"| 失败数 | {failure_runs} |",
            f"| 平均时长 | {avg_min} 分钟 |",
            ""
        ]
        return "\n".join(lines)

    def _generate_comparison(self, yesterday_agg, today_rate, today_duration, today_total):
        """生成与昨日的对比。"""
        y_total = yesterday_agg.get("total_runs", 0)
        y_success = yesterday_agg.get("success_runs", 0)
        y_rate = (y_success / max(y_total, 1)) * 100
        y_avg = yesterday_agg.get("avg_duration_seconds", 0)

        rate_diff = today_rate - y_rate
        duration_diff = round((today_duration - y_avg) / 60, 1)
        total_diff = today_total - y_total

        rate_arrow = "↑" if rate_diff > 0 else "↓" if rate_diff < 0 else "→"
        dur_arrow = "↓" if duration_diff < 0 else "↑" if duration_diff > 0 else "→"
        total_arrow = "↑" if total_diff > 0 else "↓" if total_diff < 0 else "→"

        lines = [
            "## 较昨日对比",
            "",
            "| 指标 | 今日 | 昨日 | 变化 |",
            "|------|------|------|------|",
            f"| 运行总数 | {today_total} | {y_total} | {total_arrow}{total_diff} |",
            f"| 成功率 | {today_rate:.1f}% | {y_rate:.1f}% | {rate_arrow}{rate_diff:+.1f}% |",
            f"| 平均时长 | {round(today_duration/60,1)}分钟 | {round(y_avg/60,1)}分钟 | {dur_arrow}{duration_diff:+.1f}分钟 |",
            ""
        ]
        return "\n".join(lines)

    def _generate_failure_details(self, runs: List[Dict]):
        """生成失败详情（包含所有非成功状态：failure/skipped/cancelled 等）。"""
        non_success_runs = [r for r in runs if r.get("conclusion") != "success"]
        if not non_success_runs:
            return "## 失败详情\n\n今日无 Nightly 构建失败。\n"

        lines = ["## 失败详情", ""]

        status_counts = {}
        for r in non_success_runs:
            status = r.get("conclusion", "unknown")
            status_label = self.STATUS_LABELS.get(status, status)
            status_counts[status_label] = status_counts.get(status_label, 0) + 1

        for status_label, count in status_counts.items():
            lines.append(f"- {status_label} ({count})")

        category_counts = {}
        for r in non_success_runs:
            cls = r.get("classification", {})
            cat = cls.get("classification", "infrastructure") if cls else "infrastructure"
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            category_counts[cat_label] = category_counts.get(cat_label, 0) + 1

        if category_counts:
            lines.append("")
            lines.append("**根因分类**:")
            for cat_label, count in category_counts.items():
                lines.append(f"- {cat_label} ({count})")

        lines.append("")
        lines.append("| # | Workflow | 状态 | 根因 | 置信度 | 详情 |")
        lines.append("|---|---|---|---|---|---|")

        for i, r in enumerate(non_success_runs, 1):
            cls = r.get("classification", {})
            status = r.get("conclusion", "unknown")
            status_label = self.STATUS_LABELS.get(status, status)
            cat = cls.get("classification", "infrastructure") if cls else "infrastructure"
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            conf = cls.get("confidence", "low") if cls else "low"
            conf_label = self.CONFIDENCE_LABELS.get(conf, conf)
            detail = cls.get("category_detail", "") if cls else f"状态: {status_label}"
            name = r.get("name", r.get("workflow_run", {}).get("name", ""))
            run_id = r.get("id", r.get("workflow_run", {}).get("id", ""))

            lines.append(f"| {i} | {name} (#{run_id}) | {status_label} | {cat_label} | {conf_label} | {detail} |")

        lines.append("")
        return "\n".join(lines)

    def _generate_trend(self, trend_data: List[Dict], current_rate: float):
        """生成 7 日趋势可视化。"""
        lines = ["## 7 日趋势", ""]

        if not trend_data:
            return ""

        rates = [t.get("success_rate", 0) for t in trend_data]
        avg_rate = sum(rates) / max(len(rates), 1)
        rate_diff = current_rate - avg_rate
        arrow = "↑" if rate_diff > 0 else "↓" if rate_diff < 0 else "→"

        bar = self._render_bar(current_rate)

        lines.append(f"成功率: {bar} {current_rate:.1f}% ({arrow}{rate_diff:+.1f}%)")
        lines.append("")

        lines.append("| 日期 | 成功率 | 失败数 | 健康度 |")
        lines.append("|------|--------|--------|--------|")

        for t in trend_data:
            lines.append(f"| {t.get('date','')} | {t.get('success_rate',0):.1f}% | {t.get('failure_runs',0)} | {t.get('health_score',0):.1f} |")

        lines.append("")
        return "\n".join(lines)

    def _generate_alert(self, runs: List[Dict]):
        """生成连续失败告警。"""
        if not self.aggregator:
            return ""

        consecutive = self.aggregator.get_consecutive_failures("nightly")
        alert_config = {}

        from monitor.config_loader import config
        pipeline_types = config._config.get("pipeline_types", {})
        if "nightly" in pipeline_types:
            alert_config = pipeline_types["nightly"]

        threshold = alert_config.get("alert_on_consecutive_failures", 2)

        if consecutive >= threshold:
            lines = [
                "## 告警",
                "",
                f"⚠️ **连续失败告警**: Nightly 流水线已连续失败 {consecutive} 次，超过阈值 ({threshold})。",
                "",
                "建议立即排查基础设施状态或检查最近代码变更。",
                ""
            ]
            return "\n".join(lines)

        return ""

    def _render_bar(self, value: float, width: int = 10) -> str:
        """渲染 Unicode 进度条。"""
        filled = int(value / 10)
        empty = width - filled
        return "█" * filled + "░" * empty

    def _calc_avg_duration(self, runs: List[Dict]) -> float:
        """计算平均运行时长（秒）。"""
        durations = []
        for r in runs:
            wf = r.get("workflow_run", r)
            started = wf.get("started_at", r.get("run_started_at", ""))
            completed = wf.get("completed_at", r.get("updated_at", ""))
            if started and completed:
                try:
                    s = datetime.fromisoformat(started.replace("Z", "+00:00"))
                    e = datetime.fromisoformat(completed.replace("Z", "+00:00"))
                    durations.append(max((e - s).total_seconds(), 0))
                except (ValueError, TypeError):
                    pass

        return sum(durations) / max(len(durations), 1) if durations else 0

    def generate_filename(self, date_str: str = None) -> str:
        """生成 Nightly 日报文件名。"""
        if not date_str:
            date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return f"nightly-daily-{date_str}.md"