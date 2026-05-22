"""监测报告生成器 - 按 PR 聚合的标准化 Markdown 报告。"""
import json
import uuid
import argparse
import sys
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))


class ReportGenerator:
    """按 PR 聚合的监测报告生成器。"""

    CATEGORY_LABELS = {
        "code": "PR代码问题",
        "infrastructure": "基础设施问题",
        "interference": "多PR并发干扰"
    }

    CONFIDENCE_LABELS = {
        "high": "高",
        "medium": "中",
        "low": "低"
    }

    def generate_pr_report(self, group: Dict[str, Any]) -> str:
        """生成单个 PR 的聚合报告（包含所有失败的 workflow 分析）。"""

        report_id = str(uuid.uuid4())[:8]
        pr_number = group.get("pr_number")
        group_key = group.get("group_key", "")
        overall_category = group.get("overall_category", "infrastructure")
        total_failed = group.get("total_failed_workflows", 0)
        category_counts = group.get("category_counts", {})
        workflow_runs = group.get("workflow_runs", [])
        overall_recommendations = group.get("overall_recommendations", [])

        frontmatter = self._generate_frontmatter(
            report_id, pr_number, group_key, overall_category,
            total_failed, category_counts
        )

        header_summary = self._generate_header_summary(
            pr_number, group_key, total_failed, category_counts, workflow_runs
        )

        workflow_sections = self._generate_workflow_sections(workflow_runs)

        recommendations_section = self._generate_recommendations_section(
            overall_category, overall_recommendations
        )

        title = self._get_title(pr_number, group_key)

        report = f"""{frontmatter}

# 构建失败报告: {title}

## 概要

{header_summary}

{workflow_sections}

## 修复建议

{recommendations_section}

---
报告生成时间: {datetime.now(timezone.utc).isoformat()}
"""

        return report

    def _generate_frontmatter(
        self,
        report_id: str,
        pr_number: int | None,
        group_key: str,
        overall_category: str,
        total_failed: int,
        category_counts: Dict
    ) -> str:
        """生成 YAML frontmatter。"""

        fm = {
            "report_id": report_id,
            "pr_number": pr_number,
            "group_key": group_key,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "overall_classification": overall_category,
            "total_failed_workflows": total_failed,
            "category_counts": category_counts
        }

        lines = ["---"]
        for key, value in fm.items():
            if isinstance(value, dict):
                lines.append(f"{key}:")
                for k, v in value.items():
                    lines.append(f"  {k}: {v}")
            elif isinstance(value, bool):
                lines.append(f"{key}: {str(value).lower()}")
            elif isinstance(value, (int, str)):
                lines.append(f"{key}: {value}")
            elif value is None:
                lines.append(f"{key}: null")
        lines.append("---")

        return "\n".join(lines)

    def _get_title(self, pr_number: int | None, group_key: str) -> str:
        """生成报告标题。"""
        if pr_number is not None:
            return f"PR #{pr_number}"
        return group_key

    def _generate_header_summary(
        self,
        pr_number: int | None,
        group_key: str,
        total_failed: int,
        category_counts: Dict,
        workflow_runs: List[Dict]
    ) -> str:
        """生成报告头部汇总：整体分类统计 + 各 workflow 一览表。"""

        subject = f"PR #{pr_number}" if pr_number is not None else group_key

        lines = [
            f"{subject} 触发了 {total_failed} 个 workflow，均失败。",
            ""
        ]

        code_count = category_counts.get("code", 0)
        infra_count = category_counts.get("infrastructure", 0)
        inter_count = category_counts.get("interference", 0)

        if code_count > 0:
            lines.append(f"- **代码问题**: {code_count} 次")
        if infra_count > 0:
            lines.append(f"- **基础设施问题**: {infra_count} 次")
        if inter_count > 0:
            lines.append(f"- **并发干扰**: {inter_count} 次")

        lines.append("")
        lines.append("| # | Workflow | 根因分类 | 置信度 | 具体问题 |")
        lines.append("|---|---|---|---|---|")

        for i, item in enumerate(workflow_runs, 1):
            cls = item.get("classification", {})
            cat = cls.get("classification", "unknown")
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            confidence = cls.get("confidence", "low")
            conf_label = self.CONFIDENCE_LABELS.get(confidence, confidence)
            detail = cls.get("category_detail", "")
            wf_name = item.get("workflow_name", "")
            run_id = item.get("workflow_run_id", "")

            lines.append(f"| {i} | {wf_name} (#{run_id}) | {cat_label} | {conf_label} | {detail} |")

        lines.append("")
        return "\n".join(lines)

    def _generate_workflow_sections(self, workflow_runs: List[Dict]) -> str:
        """为每个失败的 workflow run 生成详细分析段落。"""

        sections = []

        for i, item in enumerate(workflow_runs, 1):
            cls = item.get("classification", {})
            metadata = item.get("metadata", {})
            recommendations = item.get("recommendations", {})
            wf_name = item.get("workflow_name", "")
            run_id = item.get("workflow_run_id", "")

            cat = cls.get("classification", "unknown")
            cat_label = self.CATEGORY_LABELS.get(cat, cat)
            confidence = cls.get("confidence", "low")
            conf_label = self.CONFIDENCE_LABELS.get(confidence, confidence)
            reasoning = cls.get("reasoning", "")
            detail = cls.get("category_detail", "")

            section_lines = [
                f"### {i}. {wf_name} (Run #{run_id})",
                "",
                f"- **根因分类**: {cat_label}",
                f"- **置信度**: {conf_label}",
                f"- **具体问题**: {detail}",
                ""
            ]

            if reasoning:
                section_lines.append(f"**分析推理**: {reasoning}")
                section_lines.append("")

            if cls.get("requires_manual_review"):
                section_lines.append("**需要人工审查**: 未能明确归类，建议人工检查日志。")
                section_lines.append("")

            evidence_list = cls.get("evidence", [])
            if evidence_list:
                section_lines.append("**匹配模式**:")
                for ev in evidence_list:
                    section_lines.append(f"- {ev.get('category', '未知')}: `{ev.get('pattern', '')}`")
                section_lines.append("")

            workflow_run = metadata.get("workflow_run", {})
            if workflow_run.get("url"):
                section_lines.append(f"[查看 Workflow Run]({workflow_run['url']})")

            pr = metadata.get("pr")
            if pr and pr.get("url"):
                section_lines.append(f"[查看 PR #{pr.get('number')}]({pr['url']})")

            failed_jobs = metadata.get("failed_jobs", [])
            for job in failed_jobs:
                if job.get("log_url"):
                    section_lines.append(f"[查看 Job: {job['name']}]({job['log_url']})")

            log_excerpt = self._get_log_excerpt(metadata)
            if log_excerpt:
                section_lines.append("")
                section_lines.append("**日志片段**:")
                section_lines.append("```")
                section_lines.append(log_excerpt[:500])
                section_lines.append("```")

            rec_list = recommendations.get("recommendations", [])
            if rec_list:
                section_lines.append("")
                section_lines.append("**建议**:")
                primary = recommendations.get("primary_recommendation")
                if primary:
                    section_lines.append(f"- 优先: {primary.get('action', '')} ({primary.get('effort', '')})")
                for rec in rec_list:
                    section_lines.append(f"- {rec.get('action', '')} ({rec.get('effort', '')})")

            sections.append("\n".join(section_lines))

        header = "## Workflow 详细分析\n"
        return header + "\n\n".join(sections)

    def _get_log_excerpt(self, metadata: Dict) -> str:
        """获取日志片段。"""
        failed_jobs = metadata.get("failed_jobs", [])
        for job in failed_jobs:
            excerpt = job.get("log_excerpt", "")
            if excerpt:
                return excerpt
        return ""

    def _generate_recommendations_section(
        self,
        overall_category: str,
        overall_recommendations: List[Dict]
    ) -> str:
        """生成整体修复建议部分。"""

        cat_label = self.CATEGORY_LABELS.get(overall_category, overall_category)

        lines = [
            f"**整体根因**: {cat_label}",
            ""
        ]

        if not overall_recommendations:
            lines.append("无法生成建议，请人工审查日志。")
            return "\n".join(lines)

        lines.append("### 优先建议")
        lines.append("")
        for rec in overall_recommendations:
            wf = rec.get("workflow_name", "")
            wf_id = rec.get("workflow_run_id", "")
            action = rec.get("action", "")
            effort = rec.get("effort", "")
            detail = rec.get("detail", "")
            lines.append(f"- **{wf} (#{wf_id})**: {action} ({effort}) - {detail}")

        return "\n".join(lines)

    def generate_filename(self, group: Dict[str, Any]) -> str:
        """生成报告文件名。"""
        overall_category = group.get("overall_category", "infra")
        pr_number = group.get("pr_number")
        group_key = group.get("group_key", "")

        if pr_number is not None:
            return f"{overall_category}-pr-{pr_number}.md"
        return f"{overall_category}-pr-{group_key}.md"

    def generate_all(self, grouped_list: List[Dict], output_dir: Path) -> List[Path]:
        """生成所有报告并保存。"""

        output_dir.mkdir(parents=True, exist_ok=True)

        report_files = []

        for group in grouped_list:
            report = self.generate_pr_report(group)
            filename = self.generate_filename(group)

            output_path = output_dir / filename
            output_path.write_text(report, encoding='utf-8')

            report_files.append(output_path)
            print(f"生成报告: {filename}")

        return report_files


def main():
    parser = argparse.ArgumentParser(description='生成监测报告')
    parser.add_argument('--input', type=str, default='data/recommendations.json')
    parser.add_argument('--output', type=str, default='reports/')

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"输入文件不存在: {input_path}")
        sys.exit(1)

    grouped_list = json.loads(input_path.read_text(encoding='utf-8'))

    if not grouped_list:
        print("没有数据生成报告，创建空报告目录")
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)

        no_data_report = output_dir / "no-data.md"
        no_data_report.write_text(
            "---\nstatus: no_data\ngenerated_at: " + datetime.now(timezone.utc).isoformat() + "\n---\n\n# 本轮监测无失败构建\n\n本次检查未发现需要报告的失败构建。\n", encoding='utf-8'
        )

        summary = {
            "total_reports": 0,
            "generated_at": datetime.now().isoformat(),
            "output_dir": str(output_dir),
            "status": "no_data"
        }
        summary_path = Path("data/summary.json")
        summary_path.parent.mkdir(parents=True, exist_ok=True)
        summary_path.write_text(json.dumps(summary, indent=2))

        print(f"摘要已保存到 {summary_path}")
        sys.exit(0)

    generator = ReportGenerator()
    output_dir = Path(args.output)

    report_files = generator.generate_all(grouped_list, output_dir)

    print(f"已生成 {len(report_files)} 个报告")

    summary = {
        "total_reports": len(report_files),
        "generated_at": datetime.now().isoformat(),
        "output_dir": str(output_dir)
    }

    summary_path = Path("data/summary.json")
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2))

    print(f"摘要已保存到 {summary_path}")


if __name__ == "__main__":
    main()