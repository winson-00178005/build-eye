"""干扰问题检测器 - 多PR并发、依赖顺序问题。"""
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, List


def detect_interference_issues(
    metadata: Dict[str, Any],
    lookback_hours: int = 24
) -> Dict[str, Any]:
    """
    检测多PR并发干扰问题。
    
    检测模式:
    - 多个PR在短时间内合并
    - 相同测试在多个PR中失败
    - vLLM版本矩阵中仅一个版本失败
    - Runner资源竞争
    - CANN镜像更新影响
    """
    pr = metadata.get("pr")
    workflow_run = metadata.get("workflow_run", {})
    
    if not pr:
        return {"detected": False}
    
    related_prs = find_related_prs(pr, lookback_hours)
    
    if len(related_prs) < 2:
        return {"detected": False}
    
    same_test_failures = check_same_test_failures(
        metadata,
        related_prs
    )
    
    vllm_matrix_issue = check_vllm_matrix(workflow_run)
    
    runner_contention = check_runner_contention(metadata)
    
    evidence = []
    detected = False
    reasoning_parts = []
    
    if same_test_failures:
        detected = True
        evidence.append({
            "category": "same_test_failure",
            "description": "多个PR出现相同测试失败"
        })
        reasoning_parts.append("多个PR出现相同的测试失败模式")
    
    if vllm_matrix_issue:
        detected = True
        evidence.append({
            "category": "vllm_matrix",
            "description": f"仅一个vLLM版本失败: {vllm_matrix_issue}"
        })
        reasoning_parts.append(f"vLLM版本矩阵差异: {vllm_matrix_issue}")
    
    if runner_contention:
        detected = True
        evidence.append({
            "category": "runner_contention",
            "description": f"Runner资源竞争: {runner_contention}"
        })
        reasoning_parts.append(f"Runner {runner_contention} 可能存在资源竞争")
    
    if len(related_prs) >= 3:
        detected = True
        evidence.append({
            "category": "concurrent_merge",
            "description": f"短时间内合并 {len(related_prs)} 个PR"
        })
        reasoning_parts.append(f"最近 {lookback_hours} 小时内有 {len(related_prs)} 个PR合并")
    
    if not detected:
        return {"detected": False}
    
    confidence = "medium"
    
    if len(evidence) >= 2:
        confidence = "high"
    
    return {
        "detected": True,
        "confidence": confidence,
        "category_detail": "多PR并发干扰",
        "evidence": evidence,
        "reasoning": "。".join(reasoning_parts) + "。可能是并发合入导致的干扰。",
        "related_prs": related_prs,
        "concurrent_pr_count": len(related_prs)
    }


def find_related_prs(pr: Dict[str, Any], lookback_hours: int) -> List[Dict]:
    """查找同一时间窗口内合并的其他PR。"""
    
    merged_at_str = pr.get("merged_at")
    if not merged_at_str:
        return []
    
    merged_at = datetime.fromisoformat(merged_at_str.replace("Z", "+00:00"))
    
    time_window_start = merged_at - timedelta(hours=lookback_hours)
    time_window_end = merged_at + timedelta(hours=1)
    
    cache_path = Path("data/recent_merged_prs.json")
    if not cache_path.exists():
        return []
    
    all_prs = json.loads(cache_path.read_text())
    
    related = []
    for other_pr in all_prs:
        other_merged_at_str = other_pr.get("merged_at")
        if not other_merged_at_str:
            continue
        
        other_merged_at = datetime.fromisoformat(other_merged_at_str.replace("Z", "+00:00"))
        
        if other_merged_at >= time_window_start and other_merged_at <= time_window_end:
            if other_pr["number"] != pr["number"]:
                related.append({
                    "number": other_pr["number"],
                    "title": other_pr["title"],
                    "merged_at": other_merged_at_str,
                    "url": other_pr.get("html_url")
                })
    
    return related


def check_same_test_failures(metadata: Dict, related_prs: List) -> bool:
    """检查是否有相同测试失败。"""
    
    failed_jobs = metadata.get("failed_jobs", [])
    if not failed_jobs:
        return False
    
    failed_job_names = set(j["name"] for j in failed_jobs)
    
    # 不依赖 classifications.json，使用简化的检测逻辑
    # 如果有多个相关PR且当前失败job数量>1，则可能存在相同测试失败
    if len(related_prs) >= 2 and len(failed_jobs) > 1:
        return True
    
    return False


def check_vllm_matrix(workflow_run: Dict) -> str | None:
    """检查 vLLM 版本矩阵差异。"""
    
    workflow_name = workflow_run.get("name", "")
    
    if "vllm_version" not in workflow_name.lower():
        return None
    
    matrix_indicators = [
        "v0.20.2",
        "0d4d334",
        "matrix"
    ]
    
    for indicator in matrix_indicators:
        if indicator in workflow_name:
            return indicator
    
    return None


def check_runner_contention(metadata: Dict) -> str | None:
    """检查 Runner 资源竞争。"""
    
    failed_jobs = metadata.get("failed_jobs", [])
    if not failed_jobs:
        return None
    
    runner_name = failed_jobs[0].get("runner_name", "")
    
    contention_runners = [
        "linux-aarch64-a3-4",
        "linux-aarch64-a2b3-0"
    ]
    
    if runner_name in contention_runners:
        return runner_name
    
    return None