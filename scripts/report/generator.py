"""监测报告生成器 - 标准化 Markdown 报告。"""
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
    """标准化监测报告生成器。"""
    
    def __init__(self, template_dir: Path | None = None):
        self.template_dir = template_dir or Path("templates")
    
    def generate_report(self, data: Dict[str, Any]) -> str:
        """生成单个失败构建的监测报告。"""
        
        report_id = str(uuid.uuid4())[:8]
        
        classification = data.get("classification", {})
        recommendations = data.get("recommendations", {})
        
        pr_number = data.get("pr_number")
        workflow_run_id = data.get("workflow_run_id")
        
        frontmatter = self._generate_frontmatter(
            report_id, pr_number, workflow_run_id, classification
        )
        
        summary = self._generate_summary(data)
        
        root_cause = self._generate_root_cause_section(data)
        
        evidence = self._generate_evidence_section(data)
        
        recommendations_section = self._generate_recommendations_section(recommendations)
        
        related_prs = self._generate_related_prs_section(data)
        
        report = f"""{frontmatter}

# 构建失败报告: {self._get_title(data)}

## 概要

{summary}

## 根因分析

{root_cause}

## 证据

{evidence}

## 修复建议

{recommendations_section}

{related_prs}

---
报告生成时间: {datetime.now(timezone.utc).isoformat()}
"""
        
        return report
    
    def _generate_frontmatter(
        self,
        report_id: str,
        pr_number: int | None,
        workflow_run_id: int | None,
        classification: Dict
    ) -> str:
        """生成 YAML frontmatter。"""
        
        fm = {
            "report_id": report_id,
            "pr_number": pr_number,
            "workflow_run_id": workflow_run_id,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "classification": classification.get("classification", "unknown"),
            "confidence": classification.get("confidence", "low"),
            "category_detail": classification.get("category_detail", ""),
            "requires_manual_review": classification.get("requires_manual_review", False)
        }
        
        lines = ["---"]
        for key, value in fm.items():
            if isinstance(value, bool):
                lines.append(f"{key}: {str(value).lower()}")
            elif isinstance(value, (int, str)):
                lines.append(f"{key}: {value}")
            elif value is None:
                lines.append(f"{key}: null")
        lines.append("---")
        
        return "\n".join(lines)
    
    def _get_title(self, data: Dict) -> str:
        """生成报告标题。"""
        
        pr_number = data.get("pr_number")
        workflow_name = data.get("classification", {}).get("workflow_name", "")
        
        if pr_number:
            return f"PR #{pr_number}"
        
        return f"Workflow {workflow_name}"
    
    def _generate_summary(self, data: Dict) -> str:
        """生成概要部分（1-2句话）。"""
        
        classification = data.get("classification", {})
        recommendations = data.get("recommendations", {})
        
        cat = classification.get("classification", "unknown")
        detail = classification.get("category_detail", "")
        
        summary = recommendations.get("summary", "")
        
        if cat == "code":
            return f"PR #{data.get('pr_number')} 构建失败，根因: {detail}。{summary}"
        
        elif cat == "infrastructure":
            return f"构建失败由基础设施问题导致: {detail}。不是代码问题，建议重试。"
        
        elif cat == "interference":
            count = classification.get("concurrent_pr_count", 0)
            return f"构建失败由 {count} 个并发PR合入干扰导致。{summary}"
        
        return f"构建失败，根因待确认。建议人工审查。"
    
    def _generate_root_cause_section(self, data: Dict) -> str:
        """生成根因分析部分。"""
        
        classification = data.get("classification", {})
        
        cat = classification.get("classification", "unknown")
        reasoning = classification.get("reasoning", "")
        confidence = classification.get("confidence", "low")
        
        lines = [
            f"**分类**: {self._get_category_label(cat)}",
            f"**置信度**: {self._get_confidence_label(confidence)}",
            f"**具体问题**: {classification.get('category_detail', '未知')}",
            "",
            "### 分析推理",
            "",
            reasoning,
            ""
        ]
        
        if classification.get("requires_manual_review"):
            lines.append("**⚠️ 需要人工审查**: 未能明确归类，建议人工检查日志。")
            lines.append("")
        
        return "\n".join(lines)
    
    def _get_category_label(self, cat: str) -> str:
        """获取分类标签中文描述。"""
        
        labels = {
            "code": "PR代码问题",
            "infrastructure": "基础设施问题",
            "interference": "多PR并发干扰"
        }
        
        return labels.get(cat, cat)
    
    def _get_confidence_label(self, confidence: str) -> str:
        """获取置信度标签中文描述。"""
        
        labels = {
            "high": "高 ✓",
            "medium": "中 ~",
            "low": "低 ⚠️"
        }
        
        return labels.get(confidence, confidence)
    
    def _generate_evidence_section(self, data: Dict) -> str:
        """生成证据部分。"""
        
        classification = data.get("classification", {})
        metadata = data.get("metadata", {})
        
        evidence_list = classification.get("evidence", [])
        
        lines = ["### 匹配模式", ""]
        
        if evidence_list:
            for ev in evidence_list:
                lines.append(f"- **{ev.get('category', '未知')}**: `{ev.get('pattern', '')}`")
                matches = ev.get("matches", [])
                if matches:
                    for m in matches[:3]:
                        lines.append(f"  - `{m}`")
        else:
            lines.append("未匹配已知模式")
        
        lines.append("")
        lines.append("### 链接")
        lines.append("")
        
        workflow_run = metadata.get("workflow_run", {})
        pr = metadata.get("pr")
        
        if workflow_run.get("url"):
            lines.append(f"- [Workflow Run]({workflow_run['url']})")
        
        if pr and pr.get("url"):
            lines.append(f"- [PR #{pr['number']}]({pr['url']})")
        
        failed_jobs = metadata.get("failed_jobs", [])
        for job in failed_jobs:
            if job.get("log_url"):
                lines.append(f"- [Job: {job['name']}]({job['log_url']})")
        
        lines.append("")
        
        log_excerpt = self._get_log_excerpt(metadata)
        if log_excerpt:
            lines.append("### 日志片段")
            lines.append("")
            lines.append("```")
            lines.append(log_excerpt[:500])
            lines.append("```")
        
        return "\n".join(lines)
    
    def _get_log_excerpt(self, metadata: Dict) -> str:
        """获取日志片段。"""
        
        failed_jobs = metadata.get("failed_jobs", [])
        
        for job in failed_jobs:
            excerpt = job.get("log_excerpt", "")
            if excerpt:
                return excerpt
        
        return ""
    
    def _generate_recommendations_section(self, recommendations: Dict) -> str:
        """生成修复建议部分。"""
        
        rec_list = recommendations.get("recommendations", [])
        
        if not rec_list:
            return "无法生成建议，请人工审查日志。"
        
        lines = []
        
        primary = recommendations.get("primary_recommendation")
        if primary:
            lines.append(f"**优先建议**: {primary.get('action', '')} ({primary.get('effort', '')})")
            lines.append("")
        
        lines.append("### 详细步骤")
        lines.append("")
        
        for rec in rec_list:
            lines.append(f"{rec['step']}. **{rec['action']}** ({rec['effort']})")
            lines.append(f"   {rec.get('detail', '')}")
            
            commands = rec.get("commands", [])
            if commands:
                lines.append("")
                for cmd in commands:
                    lines.append(f"   - {cmd}")
            
            lines.append("")
        
        return "\n".join(lines)
    
    def _generate_related_prs_section(self, data: Dict) -> str:
        """生成相关PR部分（仅干扰分类）。"""
        
        classification = data.get("classification", {})
        
        if classification.get("classification") != "interference":
            return ""
        
        related_prs = classification.get("related_prs", [])
        
        if not related_prs:
            return ""
        
        lines = ["## 相关PR", "", "可能与当前构建冲突的PR:", ""]
        
        for pr in related_prs:
            lines.append(f"- PR #{pr.get('number')}: {pr.get('title', '')}")
            if pr.get("url"):
                lines.append(f"  [{pr['url']}]({pr['url']})")
            lines.append("")
        
        return "\n".join(lines)
    
    def generate_filename(self, data: Dict) -> str:
        """生成报告文件名。"""
        
        classification = data.get("classification", {})
        pr_number = data.get("pr_number")
        
        cat = classification.get("classification", "infra")
        
        if pr_number:
            return f"{cat}-pr-{pr_number}.md"
        
        workflow_id = data.get("workflow_run_id")
        return f"{cat}-{workflow_id}.md"
    
    def generate_all(self, recommendations_list: List[Dict], output_dir: Path) -> List[Path]:
        """生成所有报告并保存。"""
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        report_files = []
        
        for data in recommendations_list:
            report = self.generate_report(data)
            filename = self.generate_filename(data)
            
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
    
    recommendations = json.loads(input_path.read_text(encoding='utf-8'))
    
    if not recommendations:
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
    
    report_files = generator.generate_all(recommendations, output_dir)
    
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