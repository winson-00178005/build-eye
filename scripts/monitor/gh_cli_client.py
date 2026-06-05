"""GitHub CLI 客户端 - 使用 gh 命令行工具替代 REST API，自动处理认证和速率限制。"""
import json
import subprocess
import time
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional, List


class GhCLIClient:
    """使用 gh CLI 替代 REST API 调用，自动认证、自动分页、内置速率限制重试。"""

    def __init__(self, owner: str = "", repo: str = "", timeout: int = 120):
        self.owner = owner
        self.repo = repo
        self.timeout = timeout
        self._check_gh_available()

    def _check_gh_available(self):
        try:
            result = subprocess.run(["gh", "--version"], capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                raise RuntimeError("gh CLI not available")
            version = result.stdout.strip().split()[2]
            print(f"gh CLI available: version {version}")
        except FileNotFoundError:
            raise RuntimeError("gh CLI not installed. Install: https://cli.github.com/")

    def _gh_api(self, endpoint: str, paginate: bool = False, jq: str = "",
                params: Dict[str, str] = None, max_retries: int = 3) -> Any:
        cmd = ["gh", "api", endpoint]
        if paginate:
            cmd.append("--paginate")
        if jq:
            cmd.extend(["--jq", jq])
        if params:
            for k, v in params.items():
                cmd.extend(["-f", f"{k}={v}"])

        for attempt in range(max_retries):
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=self.timeout)
                if result.returncode == 0:
                    if jq and paginate:
                        lines = result.stdout.strip().split('\n')
                        items = []
                        for line in lines:
                            if line.strip():
                                try:
                                    parsed = json.loads(line)
                                    items.append(parsed)
                                except json.JSONDecodeError:
                                    pass
                        return items
                    elif jq:
                        text = result.stdout.strip()
                        if not text or text == "null":
                            return None
                        try:
                            return json.loads(text)
                        except json.JSONDecodeError:
                            return text
                    elif paginate:
                        lines = result.stdout.strip().split('\n')
                        all_items = []
                        for line in lines:
                            if line.strip():
                                try:
                                    page_data = json.loads(line)
                                    if isinstance(page_data, dict) and "workflow_runs" in page_data:
                                        all_items.extend(page_data["workflow_runs"])
                                    elif isinstance(page_data, dict) and "jobs" in page_data:
                                        all_items.extend(page_data["jobs"])
                                    elif isinstance(page_data, list):
                                        all_items.extend(page_data)
                                    else:
                                        all_items.append(page_data)
                                except json.JSONDecodeError:
                                    pass
                        return all_items
                    else:
                        try:
                            return json.loads(result.stdout)
                        except json.JSONDecodeError:
                            return result.stdout

                stderr = result.stderr
                if "rate limit" in stderr.lower() or "422" in stderr:
                    wait = 60 * (attempt + 1)
                    print(f"Rate limit hit, waiting {wait}s before retry (attempt {attempt+1}/{max_retries})...")
                    time.sleep(wait)
                    continue
                if "401" in stderr:
                    print(f"Authentication failed. Run: gh auth login")
                    return None
                print(f"gh api error: {stderr[:200]}")
                return None

            except subprocess.TimeoutExpired:
                print(f"gh api timeout ({self.timeout}s): {endpoint}")
                if attempt < max_retries - 1:
                    time.sleep(30 * (attempt + 1))
                    continue
                return None

        print(f"gh api failed after {max_retries} retries: {endpoint}")
        return None

    def _full_repo(self) -> str:
        return f"{self.owner}/{self.repo}"

    def get_workflow_runs(self, owner: str = "", repo: str = "",
                         branch: str | None = None, status: str | None = None,
                         created: str | None = None, event: str | None = None,
                         per_page: int = 100, max_pages: int = 100) -> List[Dict]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/actions/runs"
        params = {"per_page": str(per_page), "status": status or "completed"}
        if branch:
            params["branch"] = branch
        if created:
            params["created"] = created
        if event:
            params["event"] = event

        result = self._gh_api(endpoint, paginate=True, params=params)
        if isinstance(result, list):
            return result
        return []

    def get_workflow_run(self, owner: str = "", repo: str = "", run_id: int = 0) -> Optional[Dict]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/actions/runs/{run_id}"
        return self._gh_api(endpoint)

    def get_workflow_run_jobs(self, owner: str = "", repo: str = "", run_id: int = 0) -> List[Dict]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/actions/runs/{run_id}/jobs"
        params = {"per_page": "100"}
        result = self._gh_api(endpoint, paginate=True, params=params)
        if isinstance(result, list):
            return result
        return []

    def get_job_logs(self, owner: str = "", repo: str = "", job_id: int = 0) -> Optional[str]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/actions/jobs/{job_id}/logs"
        result = self._gh_api(endpoint)
        return result if isinstance(result, str) else None

    def get_pr_for_commit(self, owner: str = "", repo: str = "", commit_sha: str = "") -> Optional[Dict]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/commits/{commit_sha}/pulls"
        result = self._gh_api(endpoint, paginate=True)
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    def get_pr(self, owner: str = "", repo: str = "", pr_number: int = 0) -> Optional[Dict]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/pulls/{pr_number}"
        return self._gh_api(endpoint)

    def list_workflow_files(self, owner: str = "", repo: str = "") -> List[str]:
        o = owner or self.owner
        r = repo or self.repo
        endpoint = f"repos/{o}/{r}/contents/.github/workflows"
        result = self._gh_api(endpoint, paginate=False, jq=".[].name")
        if isinstance(result, str):
            return [name.strip() for name in result.split('\n') if name.strip()]
        if isinstance(result, list):
            return result
        return []


def create_gh_client(owner: str = "", repo: str = "") -> GhCLIClient:
    return GhCLIClient(owner=owner, repo=repo)


def create_client() -> "GitHubAPIClient | GhCLIClient":
    """Auto-detect: use gh CLI if available, fallback to REST API."""
    try:
        subprocess.run(["gh", "--version"], capture_output=True, timeout=5)
        return create_gh_client()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        from monitor.github_client import GitHubAPIClient
        print("gh CLI not available, falling back to REST API client")
        return GitHubAPIClient()