"""失败分类引擎 - 三类根因分析。"""
import json
import argparse
import sys
import os
from pathlib import Path
from typing import Dict, Any
from datetime import datetime, timedelta

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

from classify.code_detector import detect_code_issues
from classify.infra_detector import detect_infrastructure_issues
from classify.interference_detector import detect_interference_issues


class FailureClassifier:
    """
    CI 构建失败根因分类器。
    
    分类类别:
    - code: PR代码问题
    - infrastructure: 基础设施问题
    - interference: 多PR并发干扰
    """
    
    CONFIDENCE_HIGH = "high"
    CONFIDENCE_MEDIUM = "medium"
    CONFIDENCE_LOW = "low"
    
    def __init__(self, lookback_hours: int = 24):
        self.lookback_hours = lookback_hours
    
    def classify(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        对单个失败的 workflow run 进行分类。
        
        Returns:
            {
                "classification": "code|infrastructure|interference",
                "confidence": "high|medium|low",
                "category_detail": str,
                "evidence": list,
                "reasoning": str,
                "related_prs": list (仅 interference)
            }
        """
        failed_jobs = metadata.get("failed_jobs", [])
        
        if not failed_jobs:
            return {
                "classification": "infrastructure",
                "confidence": self.CONFIDENCE_LOW,
                "category_detail": "无失败job信息",
                "evidence": [],
                "reasoning": "无法获取job详情，默认归类为基础设施问题"
            }
        
        for job in failed_jobs:
            log_excerpt = job.get("log_excerpt", "")
            
            code_result = detect_code_issues(
                log_excerpt,
                metadata.get("pr", {}),
                metadata.get("workflow_run", {})
            )
            
            if code_result["detected"]:
                code_result["job_name"] = job["name"]
                code_result["job_id"] = job["id"]
                code_result["classification"] = "code"
                return code_result
            
            infra_result = detect_infrastructure_issues(
                log_excerpt,
                job,
                metadata
            )
            
            if infra_result["detected"]:
                infra_result["job_name"] = job["name"]
                infra_result["job_id"] = job["id"]
                infra_result["classification"] = "infrastructure"
                return infra_result
        
        interference_result = detect_interference_issues(
            metadata,
            self.lookback_hours
        )
        
        if interference_result["detected"]:
            interference_result["classification"] = "interference"
            return interference_result
        
        return {
            "classification": "infrastructure",
            "confidence": self.CONFIDENCE_LOW,
            "category_detail": "未能明确归类",
            "evidence": [],
            "reasoning": "未匹配已知失败模式，建议人工审查",
            "requires_manual_review": True
        }
    
    def classify_all(self, metadata_list: list) -> list:
        """对所有失败构建进行分类。"""
        results = []
        
        for metadata in metadata_list:
            classification = self.classify(metadata)
            
            result = {
                "workflow_run_id": metadata["workflow_run"]["id"],
                "workflow_name": metadata["workflow_run"]["name"],
                "pr_number": metadata["pr"]["number"] if metadata.get("pr") else None,
                "pipeline_type": metadata.get("pipeline_info", {}).get("pipeline_type", "pr"),
                "classification": classification,
                "metadata": metadata
            }
            
            results.append(result)
        
        return results


def main():
    parser = argparse.ArgumentParser(description='分类失败根因')
    parser.add_argument('--input', type=str, default='data/build_metadata.json')
    parser.add_argument('--output', type=str, default='data/classifications.json')
    parser.add_argument('--lookback', type=int, default=24)
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"输入文件不存在: {input_path}")
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        sys.exit(0)
    
    metadata_list = json.loads(input_path.read_text(encoding='utf-8'))
    
    if not metadata_list:
        print("没有元数据需要分类")
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        sys.exit(0)
    
    classifier = FailureClassifier(args.lookback)
    classifications = classifier.classify_all(metadata_list)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(classifications, f, indent=2, ensure_ascii=False)
    
    print(f"已分类 {len(classifications)} 条记录")
    
    stats = {
        "code": 0,
        "infrastructure": 0,
        "interference": 0,
        "manual_review": 0
    }
    
    for c in classifications:
        cat = c["classification"]["classification"]
        stats[cat] += 1
        if c["classification"].get("requires_manual_review"):
            stats["manual_review"] += 1
    
    print(f"分类统计:")
    print(f"  代码问题: {stats['code']}")
    print(f"  基础设施: {stats['infrastructure']}")
    print(f"  干扰问题: {stats['interference']}")
    print(f"  待人工审查: {stats['manual_review']}")


if __name__ == "__main__":
    main()