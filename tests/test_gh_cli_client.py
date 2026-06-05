"""gh_cli_client module tests."""
import json
import subprocess
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock


class TestGhCLIClient:
    def test_client_creation(self):
        from scripts.monitor.gh_cli_client import GhCLIClient
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="gh version 2.90.0 (2026-04-16)\n")
            client = GhCLIClient(owner="vllm-project", repo="vllm-ascend")
            assert client.owner == "vllm-project"
            assert client.repo == "vllm-ascend"

    def test_client_not_available(self):
        from scripts.monitor.gh_cli_client import GhCLIClient
        with patch("subprocess.run", side_effect=FileNotFoundError):
            try:
                GhCLIClient()
                assert False, "Should have raised RuntimeError"
            except RuntimeError as e:
                assert "not installed" in str(e).lower()

    def test_get_workflow_runs_mock(self):
        from scripts.monitor.gh_cli_client import GhCLIClient
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="gh version 2.90.0\n")
            client = GhCLIClient(owner="vllm-project", repo="vllm-ascend")

            run_data = json.dumps({"workflow_runs": [{"id": 1, "name": "Test", "conclusion": "success", "status": "completed"}]})
            mock_run.return_value = MagicMock(returncode=0, stdout=run_data)
            result = client.get_workflow_runs()
            assert isinstance(result, list)

    def test_get_workflow_run_jobs_mock(self):
        from scripts.monitor.gh_cli_client import GhCLIClient
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="gh version 2.90.0\n")
            client = GhCLIClient(owner="vllm-project", repo="vllm-ascend")

            job_data = json.dumps({"jobs": [{"id": 100, "name": "Build", "conclusion": "success", "status": "completed"}]})
            mock_run.return_value = MagicMock(returncode=0, stdout=job_data)
            result = client.get_workflow_run_jobs(run_id=1)
            assert isinstance(result, list)

    def test_rate_limit_retry(self):
        from scripts.monitor.gh_cli_client import GhCLIClient
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="gh version 2.90.0\n")
            client = GhCLIClient(owner="vllm-project", repo="vllm-ascend")

            mock_run.side_effect = [
                MagicMock(returncode=1, stderr="rate limit exceeded"),
                MagicMock(returncode=0, stdout=json.dumps({"workflow_runs": [{"id": 1}]})),
            ]
            with patch("time.sleep"):
                result = client._gh_api("repos/vllm-project/vllm-ascend/actions/runs", params={"per_page": "1"})
                assert result is not None

    def test_auto_detect_client(self):
        from scripts.monitor.gh_cli_client import create_client
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="gh version 2.90.0\n")
            client = create_client()
            from scripts.monitor.gh_cli_client import GhCLIClient
            assert isinstance(client, GhCLIClient)