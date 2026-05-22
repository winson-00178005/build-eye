"""Weekly 周报生成器 - 每周冒烟测试流水线汇总报告 + 健康评分。"""
import json
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any, List


class WeeklyReportGenerator:
    """Weekly 流水线周报生成器。"""

    CATEGORY_LABELS = {
        "code": "代码问题",
        "infrastructure": "基础设施问题",
        "interference": "并发干扰"
    }

    CONFIDENCE_LABELS = {
        "high": "高",
        "medium": "中",
        "low": "低"
    }

    def __init__(self, aggregator=None):
        self.aggregator = aggregator

    def generate_weekly_report(self, weekly_runs: List[Dict], week_start: str = None, week_end: str = None) -> str:
        """生成 Weekly 周报。"""
        if not week_start:
            today = datetime.now(timezone.utc)
            week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
        if not week_end:
            week_end = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        report_id = str(uuid.uuid4())[:8]

        total_runs = len(weekly_runs)
        success_runs = sum(1 for r in weekly_runs if r.get("conclusion") == "success")
        failure_runs = total_runs - success_runs
        success_rate = (success_runs / max(total_runs, 1)) * 100

        avg_duration = self._calc_avg_duration(weekly_runs)

        category_counts = {}
        for r in weekly_runs:
            cls = r.get("classification", {})
            if cls:
                cat = cls.get("classification", "infrastructure")
                category_counts[cat] = category_counts.get(cat, 0) + 1

        health_score = self._calc_health_score(success_rate, category_counts, total_runs, avg_duration)
        health_rating = self._get_health_rating(health_score)

        regression_tracking = self._generate_regression_tracking(weekly_runs)

        frontmatter = self._generate_frontmatter(report_id, week_start, week_end, total_runs, success_runs, failure_runs, health_score)

        overview = self._generate_overview(total_runs, success_rate, avg_duration, failure_runs, health_score, health_rating)

        health_section = self._generate_health_section(health_score, health_rating, success_rate, category_counts, total_runs, avg_duration)

        failure_detail = self._generate_failure_details(weekly_runs)

        regression_section = regression_tracking

        week_comparison = ""
        if self.aggregator:
            trend = self.aggregator.get_trend_data("weekly", 14)
            if len(trend) >= 2:
                week_comparison = self._generate_comparison(trend)

        recommendations = self._generate_recommendations(weekly_runs, health_score)

        report = f"""{frontmatter}

# Weekly 构建报告 - {week_start} ~ {week_end}

{overview}

{health_section}

{failure_detail}

{regression_section}

{week_comparison}

{recommendations}

---
报告生成时间: {datetime.now(timezone.utc).isoformat()}
"""

        return report

    def _generate_frontmatter(self, report_id, week_start, week_end, total, success, failure, health):
        lines = [
            "---",
            f"report_id: {report_id}",
            f"report_type: weekly_summary",
            f"week_start: {week_start}",
            f"week_end: {week_end}",
            f"generated_at: {datetime.now(timezone.utc).isoformat()}",
            f"total_runs: {total}",
            f"success_runs: {success}",
            f"failure_runs: {failure}",
            f"health_score: {health}",
            "---"
        ]
        return "\n".join(lines)

    def _generate_overview(self, total, success_rate, avg_duration, failure_runs, health_score, health_rating):
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
            f"| 健康评分 | {health_score:.1f} ({health_rating['emoji']} {health_rating['rating']}) |",
            ""
        ]
        return "\n".join(lines)

    def _generate_health_section(self, score, rating, success_rate, category_counts, total_runs, avg_duration):
        stability = min(100, max(0, 100 - category_counts.get("infrastructure", 0) * 10))
        efficiency = min(100, max(0, 100 - category_counts.get("interference", 0) * 15))
        coverage = min(100, total_runs * 5)

        lines = [
            "## 健康度评分",
            "",
            f"**综合评分**: {score:.1f} {rating['emoji']} {rating['rating']}",
            "",
            "| 维度 | 得分 | 权重 | 贡献 |",
            "|------|------|------|------|",
            f"| 成功率 | {success_rate:.1f} | 40% | {success_rate * 0.4:.1f} |",
            f"| 稳定性 | {stability:.1f} | 30% | {stability * 0.3:.1f} |",
            f"| 效率 | {efficiency:.1f} | 20% | {efficiency * 0.2:.1f} |",
            f"| 覆盖率 | {coverage:.1f} | 10% | {coverage * 0.1:.1f} |",
            ""
        ]
        return "\n".join(lines)

    def _generate_failure_details(self, runs: List[Dict]):
        failed = [r for r in runs if r.get("conclusion") == "failure"]
        if not failed:
            return "## 失败详情\n\n本周无 Weekly 构建失败。\n"

        lines = ["## 失败详情", ""]

        cat_summary = {}
        for r in failed:
            cls = r.get("classification", {})
            cat = cls.get("classification", "infrastructure")
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            cat_summary[cat_label] = cat_summary.get(cat_label, 0) + 1

        for label, count in cat_summary.items():
            lines.append(f"- {label} ({count})")

        lines.append("")
        lines.append("| # | Workflow | 根因 | 置信度 | 详情 |")
        lines.append("|---|---|---|---|---|")

        for i, r in enumerate(failed, 1):
            cls = r.get("classification", {})
            cat = cls.get("classification", "infrastructure")
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            conf = cls.get("confidence", "low")
            conf_label = self.CONFIDENCE_LABELS.get(conf, conf)
            detail = cls.get("category_detail", "")
            name = r.get("name", r.get("workflow_run", {}).get("name", ""))
            run_id = r.get("id", r.get("workflow_run", {}).get("id", ""))
            lines.append(f"| {i} | {name} (#{run_id}) | {cat_label} | {conf_label} | {detail} |")

        lines.append("")
        return "\n".join(lines)

    def _generate_regression_tracking(self, runs: List[Dict]):
        """生成回归追踪 - 识别本周新增失败。"""
        new_failures = []
        for r in runs:
            if r.get("conclusion") == "failure":
                cls = r.get("classification", {})
                new_failures.append({
                    "name": r.get("name", r.get("workflow_run", {}).get("name", "")),
                    "classification": cls.get("classification", ""),
                    "category_detail": cls.get("category_detail", "")
                })

        if not new_failures:
            return "## 回归追踪\n\n本周无新增回归失败。\n"

        lines = [
            "## 回归追踪",
            "",
            f"本周新增失败: {len(new_failures)} 个",
            ""
        ]

        for nf in new_failures:
            cat_label = self.CATEGORY_LABELS.get(nf["classification"], nf["classification"])
            lines.append(f"- **{nf['name']}**: {cat_label} - {nf['category_detail']}")

        lines.append("")
        return "\n".join(lines)

    def _generate_comparison(self, trend_data: List[Dict]):
        """生成周对比。"""
        if len(trend_data) < 2:
            return ""

        current = trend_data[-1]
        previous = trend_data[-2]

        rate_diff = current.get("success_rate", 0) - previous.get("success_rate", 0)
        health_diff = current.get("health_score", 0) - previous.get("health_score", 0)

        rate_arrow = "↑" if rate_diff > 0 else "↓" if rate_diff < 0 else "→"
        health_arrow = "↑" if health_diff > 0 else "↓" if health_diff < 0 else "→"

        lines = [
            "## 与上周对比",
            "",
            "| 指标 | 本周 | 上周 | 变化 |",
            "|------|------|------|------|",
            f"| 成功率 | {current.get('success_rate',0):.1f}% | {previous.get('success_rate',0):.1f}% | {rate_arrow}{rate_diff:+.1f}% |",
            f"| 失败数 | {current.get('failure_runs',0)} | {previous.get('failure_runs',0)} | {current.get('failure_runs',0) - previous.get('failure_runs',0)} |",
            f"| 健康度 | {current.get('health_score',0):.1f} | {previous.get('health_score',0):.1f} | {health_arrow}{health_diff:+.1f} |",
            ""
        ]
        return "\n".join(lines)

    def _generate_recommendations(self, runs: List[Dict], health_score: float):
        """生成基于健康评分的改进建议。"""
        lines = [
            "## 改进建议",
            ""
        ]

        failed = [r for r in runs if r.get("conclusion") == "failure"]
        if not failed:
            lines.append("本周构建状况良好，无需特别改进。")
            lines.append("")
            return "\n".join(lines)

        infra_failures = [r for r in failed if r.get("classification", {}).get("classification") == "infrastructure"]
        code_failures = [r for r in failed if r.get("classification", {}).get("classification") == "code"]

        if infra_failures:
            lines.append("1. **基础设施优化**: 检查 Runner 状态和 K8s 服务可用性，减少环境不稳定导致的失败")
        if code_failures:
            lines.append("2. **代码质量提升**: 加强 PR 预检和本地测试覆盖，减少代码问题导致的回归")

        if health_score < 70:
            lines.append("3. **紧急**: 健康评分低于 70，建议优先处理基础设施稳定性问题")

        lines.append("")
        return "\n".join(lines)

    def _calc_health_score(self, success_rate, category_counts, total_runs, avg_duration):
        stability = min(100, max(0, 100 - category_counts.get("infrastructure", 0) * 10))
        efficiency = min(100, max(0, 100 - category_counts.get("interference", 0) * 15))
        coverage = min(100, total_runs * 5)
        score = success_rate * 0.4 + stability * 0.3 + efficiency * 0.2 + coverage * 0.1
        return round(min(score, 100), 1)

    def _get_health_rating(self, score: float) -> Dict[str, str]:
        if score >= 90:
            return {"rating": "优秀", "color": "green", "emoji": "🟢"}
        elif score >= 80:
            return {"rating": "良好", "color": "green", "emoji": "🟢"}
        elif score >= 70:
            return {"rating": "一般", "color": "yellow", "emoji": "🟡"}
        elif score >= 60:
            return {"rating": "较差", "color": "yellow", "emoji": "🟡"}
        else:
            return {"rating": "危险", "color": "red", "emoji": "🔴"}

    def _calc_avg_duration(self, runs: List[Dict]) -> float:
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

    def generate_filename(self, week_start: str = None) -> str:
        if not week_start:
            today = datetime.now(timezone.utc)
            week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
        return f"weekly-summary-{week_start}.md"