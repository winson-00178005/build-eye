"""模拟测试 - 不需要真实 GitHub Token。"""
import json
from pathlib import Path
from datetime import datetime

def create_mock_data():
    """创建模拟 workflow runs 数据。"""
    
    mock_runs = [
        {
            "id": 123456789,
            "name": "E2E-Full",
            "workflow_id": "pr_test_full.yaml",
            "status": "completed",
            "conclusion": "failure",
            "started_at": "2024-05-21T10:00:00Z",
            "completed_at": "2024-05-21T12:30:00Z",
            "head_sha": "abc123def456",
            "head_branch": "main",
            "html_url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456789",
            "repository": {
                "full_name": "vllm-project/vllm-ascend"
            },
            "associated_pr": {
                "number": 1234,
                "title": "添加推理优化",
                "user": {"login": "developer1"},
                "merged_at": "2024-05-21T09:30:00Z",
                "merge_commit_sha": "abc123def456",
                "html_url": "https://github.com/vllm-project/vllm-ascend/pull/1234",
                "base": {"ref": "main"},
                "head": {"ref": "feature/optimize"}
            }
        },
        {
            "id": 123456790,
            "name": "E2E-Light",
            "workflow_id": "pr_test_light.yaml",
            "status": "completed",
            "conclusion": "failure",
            "started_at": "2024-05-21T08:00:00Z",
            "completed_at": "2024-05-21T09:00:00Z",
            "head_sha": "def456abc123",
            "head_branch": "main",
            "html_url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456790",
            "repository": {
                "full_name": "vllm-project/vllm-ascend"
            },
            "associated_pr": {
                "number": 1235,
                "title": "修复内存泄漏",
                "user": {"login": "developer2"},
                "merged_at": "2024-05-21T07:30:00Z",
                "merge_commit_sha": "def456abc123",
                "html_url": "https://github.com/vllm-project/vllm-ascend/pull/1235",
                "base": {"ref": "main"},
                "head": {"ref": "fix/memory"}
            }
        }
    ]
    
    return mock_runs


def create_mock_metadata():
    """创建模拟构建元数据。"""
    
    return [
        {
            "workflow_run": {
                "id": 123456789,
                "name": "E2E-Full",
                "workflow_id": "pr_test_full.yaml",
                "status": "completed",
                "conclusion": "failure",
                "started_at": "2024-05-21T10:00:00Z",
                "completed_at": "2024-05-21T12:30:00Z",
                "head_sha": "abc123def456",
                "head_branch": "main",
                "url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456789",
                "triggering_actor": "developer1"
            },
            "pr": {
                "number": 1234,
                "title": "添加推理优化",
                "author": "developer1",
                "merged_at": "2024-05-21T09:30:00Z",
                "merge_commit_sha": "abc123def456",
                "url": "https://github.com/vllm-project/vllm-ascend/pull/1234",
                "base_ref": "main",
                "head_ref": "feature/optimize"
            },
            "jobs": [
                {
                    "id": 987654321,
                    "name": "e2e-full",
                    "status": "completed",
                    "conclusion": "failure",
                    "started_at": "2024-05-21T10:00:00Z",
                    "completed_at": "2024-05-21T12:30:00Z",
                    "runner_name": "linux-aarch64-a2b3-1",
                    "runner_group": "self-hosted",
                    "steps": [
                        {"name": "Checkout", "number": 1, "status": "completed", "conclusion": "success"},
                        {"name": "Run tests", "number": 5, "status": "completed", "conclusion": "failure"}
                    ],
                    "url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456789/job/987654321",
                    "log_excerpt": """
FAILED tests/e2e/singlecard/test_inference.py::test_basic_inference
AssertionError: Expected output shape (1, 100) but got (1, 50)
tests/e2e/singlecard/test_inference.py:45: AssertionError
"""
                }
            ],
            "failed_jobs": [
                {
                    "id": 987654321,
                    "name": "e2e-full",
                    "status": "completed",
                    "conclusion": "failure",
                    "runner_name": "linux-aarch64-a2b3-1",
                    "log_excerpt": """
FAILED tests/e2e/singlecard/test_inference.py::test_basic_inference
AssertionError: Expected output shape (1, 100) but got (1, 50)
""",
                    "log_url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456789/job/987654321"
                }
            ]
        },
        {
            "workflow_run": {
                "id": 123456790,
                "name": "E2E-Light",
                "workflow_id": "pr_test_light.yaml",
                "status": "completed",
                "conclusion": "failure",
                "started_at": "2024-05-21T08:00:00Z",
                "completed_at": "2024-05-21T09:00:00Z",
                "head_sha": "def456abc123",
                "head_branch": "main",
                "url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456790",
                "triggering_actor": "developer2"
            },
            "pr": {
                "number": 1235,
                "title": "修复内存泄漏",
                "author": "developer2",
                "merged_at": "2024-05-21T07:30:00Z",
                "merge_commit_sha": "def456abc123",
                "url": "https://github.com/vllm-project/vllm-ascend/pull/1235",
                "base_ref": "main",
                "head_ref": "fix/memory"
            },
            "jobs": [
                {
                    "id": 987654322,
                    "name": "e2e-light",
                    "status": "completed",
                    "conclusion": "failure",
                    "started_at": "2024-05-21T08:00:00Z",
                    "completed_at": "2024-05-21T09:00:00Z",
                    "runner_name": "linux-aarch64-a2b3-0",
                    "runner_group": "self-hosted",
                    "steps": [
                        {"name": "Checkout", "number": 1, "status": "completed", "conclusion": "success"},
                        {"name": "Install dependencies", "number": 3, "status": "completed", "conclusion": "failure"}
                    ],
                    "url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456790/job/987654322",
                    "log_excerpt": """
Could not find a version that satisfies the requirement torch>=2.0
cache-service.nginx-pypi-cache.svc.cluster.local connection refused
ERROR: pip install failed
"""
                }
            ],
            "failed_jobs": [
                {
                    "id": 987654322,
                    "name": "e2e-light",
                    "status": "completed",
                    "conclusion": "failure",
                    "runner_name": "linux-aarch64-a2b3-0",
                    "log_excerpt": """
Could not find a version that satisfies the requirement torch>=2.0
cache-service.nginx-pypi-cache.svc.cluster.local connection refused
""",
                    "log_url": "https://github.com/vllm-project/vllm-ascend/actions/runs/123456790/job/987654322"
                }
            ]
        }
    ]


def run_mock_test():
    """运行模拟测试流程。"""
    
    print("=" * 50)
    print("Build-Eye 模拟测试")
    print("=" * 50)
    
    Path("data").mkdir(exist_ok=True)
    
    print("\n[1/4] 创建模拟 workflow runs 数据...")
    mock_runs = create_mock_data()
    Path("data/workflow_runs.json").write_text(
        json.dumps(mock_runs, indent=2, ensure_ascii=False)
    )
    print(f"已保存 {len(mock_runs)} 条模拟数据")
    
    print("\n[2/4] 创建模拟构建元数据...")
    mock_metadata = create_mock_metadata()
    Path("data/build_metadata.json").write_text(
        json.dumps(mock_metadata, indent=2, ensure_ascii=False)
    )
    print(f"已保存 {len(mock_metadata)} 条元数据")
    
    print("\n[3/4] 运行失败分类...")
    import subprocess
    result = subprocess.run(
        ["python", "scripts/classify/classifier.py",
         "--input", "data/build_metadata.json",
         "--output", "data/classifications.json"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.stderr:
        print("错误:", result.stderr)
    
    print("\n[4/4] 生成修复建议和报告...")
    subprocess.run(
        ["python", "scripts/recommend/recommender.py",
         "--input", "data/classifications.json",
         "--output", "data/recommendations.json"],
        capture_output=True
    )
    
    subprocess.run(
        ["python", "scripts/report/generator.py",
         "--input", "data/recommendations.json",
         "--output", "reports/"],
        capture_output=True
    )
    
    report_files = list(Path("reports").glob("*.md"))
    print(f"\n生成报告: {len(report_files)} 个")
    
    for f in report_files:
        print(f"  - {f.name}")
    
    print("\n" + "=" * 50)
    print("测试完成！查看 reports/ 目录中的报告")
    print("=" * 50)


if __name__ == "__main__":
    run_mock_test()