"""代码问题检测器 - PR代码本身问题。"""
import re
from typing import Dict, Any, List


def detect_code_issues(
    log_excerpt: str,
    pr: Dict[str, Any],
    workflow_run: Dict[str, Any]
) -> Dict[str, Any]:
    """
    检测 PR 代码相关问题。
    
    检测模式:
    - pytest 断言失败
    - 编译错误 (CMake, clang)
    - Python import 错误
    - vLLM API 不兼容
    - Ascend kernel 编译问题
    """
    patterns = {
        "test_assertion": [
            r"AssertionError",
            r"assert\s+\w+\s*==",
            r"FAILED\s+[\w/]+\.py",
            r"test_\w+.*failed"
        ],
        "compilation": [
            r"error:\s+",
            r"undefined\s+symbol",
            r"compilation\s+failed",
            r"CMake Error",
            r"clang:\s+error"
        ],
        "import_error": [
            r"ImportError",
            r"ModuleNotFoundError",
            r"cannot\s+import\s+name",
            r"AttributeError"
        ],
        "vllm_api": [
            r"cannot\s+import\s+from\s+vllm",
            r"vllm\.\w+\s+not\s+found",
            r"'vllm\.\w+'\s+has\s+no\s+attribute"
        ],
        "triton_ascend": [
            r"triton-ascend\s+error",
            r"kernel\s+compile\s+failed",
            r"Triton\s+backend\s+error"
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
    
    if pr:
        is_pr_code = check_if_in_pr_diff(log_excerpt, pr)
    else:
        is_pr_code = True
    
    confidence = "high" if is_pr_code else "medium"
    
    category_detail = categorize_code_issue(detected_categories)
    
    reasoning = build_reasoning(detected_categories, pr, evidence)
    
    return {
        "detected": True,
        "confidence": confidence,
        "category_detail": category_detail,
        "evidence": evidence,
        "reasoning": reasoning,
        "is_pr_code": is_pr_code
    }


def check_if_in_pr_diff(log_excerpt: str, pr: Dict[str, Any]) -> bool:
    """检查错误是否出现在 PR 修改的文件中。"""
    
    file_patterns = [
        r"File\s+\"([^\"]+)\"",
        r"([/\w]+\.py)",
        r"in\s+([\w]+)\s+\(",
        r"at\s+([\w/]+\.py:\d+)"
    ]
    
    mentioned_files = set()
    for pattern in file_patterns:
        matches = re.findall(pattern, log_excerpt)
        mentioned_files.update(matches)
    
    return len(mentioned_files) > 0


def categorize_code_issue(categories: List[str]) -> str:
    """确定代码问题的具体类型。"""
    
    if "test_assertion" in categories:
        return "测试断言失败"
    
    if "compilation" in categories or "triton_ascend" in categories:
        return "编译错误"
    
    if "vllm_api" in categories:
        return "vLLM API不兼容"
    
    if "import_error" in categories:
        return "导入错误"
    
    return "代码逻辑问题"


def build_reasoning(
    categories: List[str],
    pr: Dict[str, Any],
    evidence: List[Dict]
) -> str:
    """构建分类推理说明。"""
    
    pr_info = f"PR #{pr.get('number', 'unknown')}" if pr else "未知PR"
    
    evidence_summary = ", ".join([e["category"] for e in evidence])
    
    reasoning = f"检测到代码问题模式: {evidence_summary}。"
    
    if pr:
        reasoning += f" 问题出现在 PR #{pr['number']} 代码中。"
    
    reasoning += " 建议检查 PR 的代码修改和测试用例。"
    
    return reasoning