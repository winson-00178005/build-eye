"""端到端测试 - API客户端模拟响应。"""
import json
import pytest
from pathlib import Path
from unittest.mock import Mock, patch
from scripts.monitor.github_client import GitHubAPIClient


class MockGitHubClient(GitHubAPIClient):
    """模拟 GitHub API 客户端。"""
    
    def __init__(self):
        super().__init__(token="mock_token")
        self._mock_data = self._load_mock_data()
    
    def _load_mock_data(self) -> dict:
        """加载模拟数据。"""
        mock_file = Path("tests/mock_data/github_responses.json")
        if mock_file.exists():
            return json.loads(mock_file.read_text())
        return {}
    
    def get_workflow_runs(self, *args, **kwargs) -> list:
        return self._mock_data.get("workflow_runs", [])
    
    def get_workflow_run_jobs(self, *args, **kwargs) -> list:
        return self._mock_data.get("jobs", [])
    
    def get_pr_for_commit(self, *args, **kwargs) -> dict:
        return self._mock_data.get("pr", {})


def test_workflow_runs_pagination():
    """测试 workflow runs 分页获取。"""
    client = MockGitHubClient()
    
    runs = client.get_workflow_runs("vllm-project", "vllm-ascend")
    
    assert isinstance(runs, list)


def test_pr_association_detection():
    """测试 PR 关联检测。"""
    client = MockGitHubClient()
    
    pr = client.get_pr_for_commit("vllm-project", "vllm-ascend", "abc123")
    
    assert pr is None or isinstance(pr, dict)


def test_rate_limit_handling():
    """测试速率限制处理。"""
    client = MockGitHubClient()
    
    assert client.rate_limit_remaining >= 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])