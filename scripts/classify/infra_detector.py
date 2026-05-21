"""基础设施问题检测器 - 环境、网络、Runner等问题。"""
import re
from typing import Dict, Any, List


def detect_infrastructure_issues(
    log_excerpt: str,
    job: Dict[str, Any],
    metadata: Dict[str, Any]
) -> Dict[str, Any]:
    """
    检测基础设施相关问题（Ascend生态特定）。
    
    检测模式:
    - K8s cache-service 失败
    - Runner 不可用
    - NPU 硬件问题
    - CANN toolkit 问题
    - HCCL 通信失败
    - Docker 镜像拉取失败
    - Csrc 缓存失败
    - OBS wheel 失败
    - 超时
    """
    patterns = {
        "cache_service": [
            r"cache-service\.nginx-pypi-cache",
            r"svc\.cluster\.local",
            r"DNS\s+resolution\s+failed",
            r"Could\s+not\s+find\s+a\s+version",
            r"connection\s+refused.*cache-service"
        ],
        "runner": [
            r"no\s+available\s+runner",
            r"runner\s+offline",
            r"waiting\s+for\s+runner",
            r"runner\s+disconnected"
        ],
        "npu": [
            r"npu-smi\s+.*error",
            r"device\s+not\s+found",
            r"NPU\s+memory\s+error",
            r"ECC\s+error",
            r"npu\s+init\s+failed"
        ],
        "cann": [
            r"CANN\s+environment\s+not\s+activated",
            r"ascend-toolkit.*error",
            r"driver\s+version\s+mismatch",
            r"bash\s+-el.*failed"
        ],
        "hccl": [
            r"HCCL\s+error",
            r"communication\s+timeout",
            r"rank\s+init\s+failed",
            r"collective\s+operation\s+failed"
        ],
        "docker_image": [
            r"image\s+pull\s+failed",
            r"manifest\s+unknown",
            r"swr\.cn-southwest-2\.myhuaweicloud\.com.*error"
        ],
        "csrc_cache": [
            r"cache\s+restore\s+failed",
            r"cache\s+not\s+found",
            r"Cache\s+vllm-ascend\s+csrc.*failed"
        ],
        "obs_wheel": [
            r"mooncake\s+transfer\s+engine.*failed",
            r"vllm-ascend\.obs\.cn-north-4",
            r"mooncake.*install\s+error"
        ],
        "timeout": [
            r"Timeout\s+exceeded",
            r"timed\s+out",
            r"The\s+job\s+was\s+stopped",
            r"deadline\s+exceeded"
        ],
        "network": [
            r"connection\s+reset",
            r"network\s+unreachable",
            r"Temporary\s+failure\s+in\s+name\s+resolution"
        ]
    }
    
    evidence = []
    detected_categories = []
    
    for category, category_patterns in patterns.items():
        for pattern in category_patterns:
            matches = re.findall(pattern, log_excerpt, re.IGNORECASE)
            if matches:
                detected_categories.append(category)
                evidence.append({
                    "category": category,
                    "pattern": pattern,
                    "matches": matches[:5]
                })
    
    if not detected_categories:
        return {"detected": False}
    
    confidence = determine_confidence(detected_categories, job, metadata)
    
    category_detail = categorize_infra_issue(detected_categories)
    
    reasoning = build_infra_reasoning(detected_categories, job, evidence)
    
    runner_info = extract_runner_info(job)
    
    return {
        "detected": True,
        "confidence": confidence,
        "category_detail": category_detail,
        "evidence": evidence,
        "reasoning": reasoning,
        "runner_info": runner_info
    }


def determine_confidence(
    categories: List[str],
    job: Dict[str, Any],
    metadata: Dict[str, Any]
) -> str:
    """确定置信度级别。"""
    
    high_confidence_categories = [
        "cache_service", "npu", "hccl", "runner", "docker_image"
    ]
    
    if any(c in high_confidence_categories for c in categories):
        all_jobs = metadata.get("jobs", [])
        if len(all_jobs) > 1:
            failed_jobs = [j for j in all_jobs if j.get("conclusion") == "failure"]
            if len(failed_jobs) == len(all_jobs):
                return "high"
        
        return "medium"
    
    return "low"


def categorize_infra_issue(categories: List[str]) -> str:
    """确定基础设施问题的具体类型。"""
    
    priority_order = [
        ("cache_service", "K8s内部服务失败"),
        ("runner", "Runner不可用"),
        ("npu", "NPU硬件问题"),
        ("cann", "CANN toolkit问题"),
        ("hccl", "HCCL通信失败"),
        ("docker_image", "Docker镜像拉取失败"),
        ("csrc_cache", "Csrc缓存失败"),
        ("obs_wheel", "OBS wheel安装失败"),
        ("timeout", "构建超时"),
        ("network", "网络异常")
    ]
    
    for cat, label in priority_order:
        if cat in categories:
            return label
    
    return "其他基础设施问题"


def build_infra_reasoning(
    categories: List[str],
    job: Dict[str, Any],
    evidence: List[Dict]
) -> str:
    """构建基础设施问题推理说明。"""
    
    job_name = job.get("name", "unknown")
    runner = job.get("runner_name", "unknown")
    
    evidence_summary = ", ".join([e["category"] for e in evidence])
    
    reasoning = f"检测到基础设施问题: {evidence_summary}。"
    reasoning += f" 问题出现在 job '{job_name}' 中。"
    
    if runner and runner != "unknown":
        reasoning += f" Runner: {runner}。"
    
    reasoning += " 不是PR代码问题，建议检查基础设施状态。"
    
    return reasoning


def extract_runner_info(job: Dict[str, Any]) -> Dict[str, str]:
    """提取 Runner 信息（用于问题定位）。"""
    return {
        "runner_name": job.get("runner_name", "unknown"),
        "runner_group": job.get("runner_group_name", "unknown"),
        "labels": job.get("labels", [])
    }