"""报告摘要生成器 - 用于 GitHub Step Summary。"""
import json
import sys
from pathlib import Path
from datetime import datetime


def generate_summary_from_summary_json(input_path: Path) -> str:
    """从 summary.json 生成摘要。"""
    
    if not input_path.exists():
        return "无报告数据"
    
    data = json.loads(input_path.read_text(encoding='utf-8'))
    
    if not data:
        return "本次检查未发现失败构建"
    
    if isinstance(data, dict):
        status = data.get("status", "")
        if status == "no_data":
            return "本次检查未发现失败构建，无需处理"
        
        total = data.get("total_reports", 0)
        generated_at = data.get("generated_at", "")
        return f"生成 {total} 个报告 | 时间: {generated_at}"
    
    return "无报告数据"


def generate_summary_table(input_path: Path) -> str:
    """从 classifications.json 生成报告摘要表格。"""
    
    if not input_path.exists():
        return "无报告数据"
    
    classifications = json.loads(input_path.read_text(encoding='utf-8'))
    
    if not classifications:
        return "本次检查未发现失败构建"
    
    if isinstance(classifications, dict):
        return generate_summary_from_summary_json(input_path)
    
    if not isinstance(classifications, list):
        return generate_summary_from_summary_json(input_path)
    
    lines = ["| PR | Workflow | 分类 | 置信度 | 问题类型 |", "|---|---|---|---|---|"]
    
    stats = {
        "code": 0,
        "infrastructure": 0,
        "interference": 0,
        "manual_review": 0
    }
    
    for c in classifications:
        pr = c.get("pr_number", "N/A")
        workflow = c.get("workflow_name", "unknown")
        
        classification = c.get("classification", {})
        cat = classification.get("classification", "unknown")
        confidence = classification.get("confidence", "low")
        detail = classification.get("category_detail", "")
        
        stats[cat] += 1
        
        if classification.get("requires_manual_review"):
            stats["manual_review"] += 1
        
        cat_label = {
            "code": "代码",
            "infrastructure": "基建",
            "interference": "干扰"
        }.get(cat, cat)
        
        conf_label = {
            "high": "high",
            "medium": "med",
            "low": "low"
        }.get(confidence, confidence)
        
        lines.append(f"| #{pr} | {workflow} | {cat_label} | {conf_label} | {detail} |")
    
    lines.append("")
    lines.append("### 统计")
    lines.append("")
    lines.append(f"- 代码问题: {stats['code']}")
    lines.append(f"- 基础设施: {stats['infrastructure']}")
    lines.append(f"- 干扰问题: {stats['interference']}")
    lines.append(f"- 待人工审查: {stats['manual_review']}")
    
    return "\n".join(lines)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='生成报告摘要')
    parser.add_argument('--input', type=str, default='data/summary.json')
    
    args = parser.parse_args()
    
    try:
        input_path = Path(args.input)
        summary = generate_summary_table(input_path)
        print(summary)
    except Exception as e:
        print(f"摘要生成失败: {e}")


if __name__ == "__main__":
    main()