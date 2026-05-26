"""Weekly 周报生成器 - 每周冒烟测试流水线汇总报告 + 健康评分。"""
import json
import re
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

        per_failure_analysis = self._generate_per_failure_analysis(weekly_runs)

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

{per_failure_analysis}

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
        failed = [r for r in runs if r.get("conclusion") != "success"]
        if not failed:
            return "## 失败详情\n\n本周无 Weekly 构建失败。\n"

        lines = ["## 失败详情", ""]

        status_counts = {}
        for r in failed:
            status = r.get("conclusion", "unknown")
            status_label = self.STATUS_LABELS.get(status, status)
            status_counts[status_label] = status_counts.get(status_label, 0) + 1

        for status_label, count in status_counts.items():
            lines.append(f"- {status_label} ({count})")

        cat_summary = {}
        for r in failed:
            cls = r.get("classification", {})
            cat = cls.get("classification", "infrastructure") if cls else "infrastructure"
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            cat_summary[cat_label] = cat_summary.get(cat_label, 0) + 1

        if cat_summary:
            lines.append("")
            lines.append("**根因分类**:")
            for label, count in cat_summary.items():
                lines.append(f"- {label} ({count})")

        lines.append("")
        lines.append("| # | Workflow | 执行日期 | 状态 | 根因 | 置信度 | 详情 |")
        lines.append("|---|---|---|---|---|---|---|")

        for i, r in enumerate(failed, 1):
            cls = r.get("classification", {})
            status = r.get("conclusion", "unknown")
            status_label = self.STATUS_LABELS.get(status, status)
            cat = cls.get("classification", "infrastructure") if cls else "infrastructure"
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            conf = cls.get("confidence", "low") if cls else "low"
            conf_label = self.CONFIDENCE_LABELS.get(conf, conf)
            name = r.get("name", r.get("workflow_run", {}).get("name", ""))
            run_id = r.get("id", r.get("workflow_run", {}).get("id", ""))
            started_at = r.get("started_at", r.get("workflow_run", {}).get("started_at", ""))
            exec_date = ""
            if started_at:
                try:
                    dt = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
                    exec_date = dt.strftime("%Y-%m-%d")
                except (ValueError, TypeError):
                    exec_date = started_at[:10] if len(started_at) >= 10 else ""
            lines.append(f"| {i} | {name} (#{run_id}) | {exec_date} | {status_label} | {cat_label} | {conf_label} | [详细分析](#failure-{i}) |")

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
        """生成基于健康评分的改进建议 + 每个失败的优先建议。"""
        lines = [
            "## 改进建议",
            ""
        ]

        failed = [r for r in runs if r.get("conclusion") != "success"]
        if not failed:
            lines.append("本周构建状况良好，无需特别改进。")
            lines.append("")
            return "\n".join(lines)

        priority_recs = []
        for r in failed:
            rec = r.get("recommendations", {})
            primary = rec.get("primary_recommendation")
            cls = r.get("classification", {})
            if primary:
                priority_recs.append({
                    "name": r.get("name", ""),
                    "run_id": r.get("id", ""),
                    "action": primary.get("action", ""),
                    "effort": primary.get("effort", ""),
                    "detail": primary.get("detail", ""),
                    "category": cls.get("classification", "infrastructure") if cls else "infrastructure"
                })

        code_recs = [r for r in priority_recs if r["category"] == "code"]
        infra_recs = [r for r in priority_recs if r["category"] == "infrastructure"]

        if code_recs:
            lines.append("### 优先修复（代码问题）")
            lines.append("")
            for r in code_recs:
                lines.append(f"- **{r['name']} (#{r['run_id']})**: {r['action']} ({r['effort']}) - {r['detail']}")

        if infra_recs:
            lines.append("")
            lines.append("### 建议关注（基础设施问题）")
            lines.append("")
            for r in infra_recs:
                lines.append(f"- **{r['name']} (#{r['run_id']})**: {r['action']} ({r['effort']}) - {r['detail']}")

        if health_score < 70:
            lines.append("")
            lines.append(f"**紧急**: 健康评分低于 70 ({health_score:.1f})，建议优先处理基础设施稳定性问题")

        lines.append("")
        return "\n".join(lines)

    def _generate_per_failure_analysis(self, runs: List[Dict]) -> str:
        """为每个失败 run 生成详细分析段落（日志片段 + 修复建议）。"""
        failed = [r for r in runs if r.get("conclusion") not in ("success",)]
        if not failed:
            return ""

        sections = []
        for i, r in enumerate(failed, 1):
            cls = r.get("classification", {})
            meta = r.get("metadata", {})
            rec = r.get("recommendations", {})
            status = r.get("conclusion", "unknown")
            status_label = self.STATUS_LABELS.get(status, status)
            cat = cls.get("classification", "infrastructure") if cls else "infrastructure"
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            conf = cls.get("confidence", "low") if cls else "low"
            conf_label = self.CONFIDENCE_LABELS.get(conf, conf)
            detail = cls.get("category_detail", "") if cls else f"状态: {status_label}"
            reasoning = cls.get("reasoning", "") if cls else ""
            name = r.get("name", "")
            run_id = r.get("id", "")
            started_at = r.get("started_at", r.get("workflow_run", {}).get("started_at", ""))

            section_lines = [
                f"<a id='failure-{i}'></a>",
                f"### {i}. {name} (Run #{run_id})",
                "",
                f"- **状态**: {status_label}",
                f"- **根因分类**: {cat_label}",
                f"- **置信度**: {conf_label}",
                f"- **具体问题**: {detail}",
                ""
            ]

            if started_at:
                try:
                    dt = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
                    section_lines.append(f"- **执行时间**: {dt.strftime('%Y-%m-%d %H:%M')} UTC")
                except (ValueError, TypeError):
                    pass
                section_lines.append("")

            if reasoning:
                section_lines.append(f"**分析推理**: {reasoning}")
                section_lines.append("")

            evidence_list = cls.get("evidence", []) if cls else []
            if evidence_list:
                section_lines.append("**匹配模式**:")
                for ev in evidence_list:
                    section_lines.append(f"- {ev.get('category', '未知')}: `{ev.get('pattern', '')}`")
                section_lines.append("")

            workflow_run = meta.get("workflow_run", {})
            if workflow_run.get("url"):
                section_lines.append(f"[查看 Workflow Run]({workflow_run['url']})")

            failed_jobs = meta.get("failed_jobs", [])
            for job in failed_jobs:
                if job.get("log_url"):
                    section_lines.append(f"[查看 Job: {job['name']}]({job['log_url']})")

            log_excerpt = self._get_log_excerpt(meta)
            if log_excerpt:
                section_lines.append("")
                section_lines.append("**错误日志**:")
                section_lines.append("```")
                section_lines.append(log_excerpt[:800])
                section_lines.append("```")

            key_errors = self._extract_key_errors(log_excerpt, cat)
            if key_errors:
                section_lines.append("")
                section_lines.append("**关键错误信息**:")
                for err in key_errors:
                    section_lines.append(f"- `{err}`")

            section_lines.append("")
            section_lines.append("**修复建议**:")
            context_recs = self._generate_contextual_recommendations(cat, detail, key_errors, name)
            for rec_item in context_recs:
                prefix = f"- **{rec_item['priority']}**: " if rec_item.get('priority') else "- "
                section_lines.append(f"{prefix}{rec_item['action']} ({rec_item['effort']}) — {rec_item['detail']}")

            sections.append("\n".join(section_lines))

        if not sections:
            return ""

        header = "## 失败 Workflow 详细分析\n"
        return header + "\n\n".join(sections)

    def _get_log_excerpt(self, metadata: Dict) -> str:
        """获取日志片段。"""
        failed_jobs = metadata.get("failed_jobs", [])
        for job in failed_jobs:
            excerpt = job.get("log_excerpt", "")
            if excerpt:
                return excerpt
        return ""

    _INFRA_WRAPPER_RE = re.compile(
        r"Error:\s+command terminated with non-zero exit code"
        r"|failed to run script step"
        r"|gh.*CLI not found"
        r"|Process completed with exit code"
        r"|The operation was canceled",
        re.IGNORECASE
    )

    def _extract_key_errors(self, log_excerpt: str, category: str) -> List[str]:
        """从日志片段中提取关键错误行（去除 ANSI 控制码、时间戳前缀和 Runner 包装行）。"""
        if not log_excerpt:
            return []

        import re as _re
        key_error_patterns = [
            _re.compile(r"ModuleNotFoundError:\s+(.{5,80})"),
            _re.compile(r"ImportError:\s+(.{5,80})"),
            _re.compile(r"cannot\s+import\s+(.{5,60})"),
            _re.compile(r"AssertionError:\s+(.{5,80})"),
            _re.compile(r"AttributeError:\s+(.{5,80})"),
            _re.compile(r"RuntimeError:\s+(.{5,80})"),
            _re.compile(r"TypeError:\s+(.{5,80})"),
            _re.compile(r"ValueError:\s+(.{5,80})"),
            _re.compile(r"KeyError:\s+(.{5,60})"),
            _re.compile(r"OSError:\s+(.{5,80})"),
            _re.compile(r"FileNotFoundError:\s+(.{5,80})"),
            _re.compile(r"ConnectionRefusedError:\s+(.{5,80})"),
            _re.compile(r"FAILED\s+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"CMake Error\s+(.{5,80})", _re.IGNORECASE),
            _re.compile(r"undefined symbol[:\s]+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"HCCL\w*[:\s]+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"npu.*error[:\s]+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"cache-service[.\w]+[:\s]+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"compilation\s+failed[:\s]+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"timeout[:\s]+(.{5,60})", _re.IGNORECASE),
            _re.compile(r"Traceback\s+\(most recent call last\)", _re.IGNORECASE),
            _re.compile(r"error:\s+(.{5,80})", _re.IGNORECASE),
            _re.compile(r"\bError:\s+(.{5,80})"),
        ]

        errors = []
        ansi_re = _re.compile(r'\x1b\[[0-9;]*m|\x1b\].*?\x07|\[[0-9;]*m')
        for line in log_excerpt.split('\n')[:50]:
            clean = ansi_re.sub('', line)
            clean = _re.sub(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z\s+', '', clean).strip()
            if not clean or len(clean) < 5:
                continue
            if self._INFRA_WRAPPER_RE.search(clean):
                continue
            for pattern in key_error_patterns:
                m = pattern.search(clean)
                if m:
                    err = m.group(1) if m.lastindex else m.group(0)
                    err = err.strip()[:120]
                    if err not in errors:
                        errors.append(err)
                    break

        return errors[:8]

    def _generate_contextual_recommendations(self, category: str, detail: str, key_errors: List[str], workflow_name: str) -> List[Dict]:
        """根据实际错误内容生成针对性修复建议。"""
        recs = []

        if category == "code":
            has_compilation = any("编译" in detail or "compilation" in detail.lower() or "error:" in e.lower() for e in key_errors)
            has_import = any("Import" in e or "ModuleNot" in e for e in key_errors)
            has_assert = any("Assertion" in e or "FAILED" in e for e in key_errors)

            if has_compilation:
                specific_files = []
                for e in key_errors:
                    if ".py" in e or ".c" in e or ".cpp" in e or ".h" in e:
                        specific_files.append(e.split()[0] if e.split() else e[:40])
                file_hint = f"（涉及 {', '.join(specific_files[:3])}）" if specific_files else ""
                recs.append({"priority": "优先", "action": "定位并修复编译错误", "effort": "中等成本", "detail": f"根据日志中的 error 信息找到具体出错文件和行号{file_hint}，修改代码使编译通过"})
                recs.append({"priority": "", "action": "本地复现编译并验证", "effort": "低成本", "detail": f"在本地使用相同配置编译 {workflow_name}，确认修复后不再报错"})
            if has_import:
                recs.append({"priority": "优先", "action": "修复导入错误", "effort": "低成本", "detail": "检查 vLLM 或 vllm-ascend 的 API 变更，更新 import 语句适配新版本"})
                recs.append({"priority": "", "action": "更新依赖版本", "effort": "中等成本", "detail": "确认当前依赖版本与代码兼容，必要时锁定兼容版本"})
            if has_assert:
                recs.append({"priority": "优先", "action": "修复断言失败的测试", "effort": "中等成本", "detail": "查看具体测试用例的断言内容，确认是否为代码回归或预期变更"})
                recs.append({"priority": "", "action": "增加测试稳定性", "effort": "低成本", "detail": "对于因环境不稳定导致的断言失败，增加重试逻辑或放宽容差"})
            if not recs:
                recs.append({"priority": "优先", "action": "检查日志定位根因", "effort": "低成本", "detail": f"查看 {workflow_name} 的完整 CI 日志，找到第一个失败 step 的具体错误"})
                recs.append({"priority": "", "action": "提交修复并观察", "effort": "中等成本", "detail": "修复后推送代码，观察下一次 weekly 构建是否通过"})

        elif category == "infrastructure":
            has_k8s = any("cache-service" in e or "K8s" in detail or "svc" in e.lower() for e in key_errors)
            has_npu = any("npu" in e.lower() or "NPU" in detail for e in key_errors)
            has_hccl = any("HCCL" in e or "hccl" in e.lower() for e in key_errors)
            has_timeout = any("timeout" in e.lower() or "超时" in detail for e in key_errors)

            if has_k8s:
                recs.append({"priority": "优先", "action": "等待 cache-service 恢复后重试", "effort": "低成本", "detail": "cache-service.nginx-pypi-cache 通常会自动恢复，等待 10-30 分钟后重新触发"})
                recs.append({"priority": "", "action": "配置备用 pip 镜像源", "effort": "中等成本", "detail": "在 CI 配置中添加公网 pip mirror 作为 fallback，减少 K8s 服务依赖"})
            if has_npu:
                recs.append({"priority": "优先", "action": "排查 NPU 状态", "effort": "中等成本", "detail": "运行 npu-smi info 检查 NPU 卡状态，确认 ECC 错误或设备不可用的原因"})
                recs.append({"priority": "", "action": "联系运维团队", "effort": "低成本", "detail": "如 NPU 硬件持续异常，联系基础设施运维团队更换或维修"})
            if has_hccl:
                recs.append({"priority": "优先", "action": "检查多卡通信配置", "effort": "中等成本", "detail": "HCCL 通信失败通常是网络或 NPU 间通信问题，检查 HCCL 配置和网络连接"})
                recs.append({"priority": "", "action": "降级为单卡测试", "effort": "低成本", "detail": "如多卡测试持续失败，可临时降级为单卡测试以排除通信因素"})
            if has_timeout:
                recs.append({"priority": "优先", "action": "重新触发构建", "effort": "低成本", "detail": "超时可能是 Runner 临时负载高，重新触发通常能通过"})
                recs.append({"priority": "", "action": "优化超时配置", "effort": "中等成本", "detail": f"如 {workflow_name} 持续超时，考虑增加 timeout-minutes 或拆分大任务"})
            if not recs:
                recs.append({"priority": "优先", "action": "重新触发构建", "effort": "低成本", "detail": "基础设施问题通常自动恢复，重新触发是最直接的验证方式"})
                recs.append({"priority": "", "action": "联系运维团队排查", "effort": "中等成本", "detail": "如持续失败，联系基础设施运维团队检查 Runner 和 K8s 集群状态"})

        elif category == "interference":
            recs.append({"priority": "优先", "action": "重新触发构建", "effort": "低成本", "detail": "并发合入导致的干扰可通过重试解决，等待其他构建完成后重试"})
            recs.append({"priority": "", "action": "协调合入顺序", "effort": "中等成本", "detail": "如持续失败，联系相关作者协调合入时机，避免同时构建"})

        else:
            recs.append({"priority": "优先", "action": "检查日志定位根因", "effort": "低成本", "detail": f"查看 {workflow_name} 的完整 CI 日志，找到第一个失败 step"})
            recs.append({"priority": "", "action": "人工审查", "effort": "中等成本", "detail": "未能明确归类，建议人工审查日志确认失败原因"})

        return recs

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