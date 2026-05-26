"""GitHub API 客户端 - 认证、速率限制处理和请求封装。"""
import os
import time
import json
import requests
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from pathlib import Path


class GitHubAPIClient:
    """GitHub REST API 客户端，支持认证和速率限制管理。"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None, timeout: int = 30):
        self.token = token or os.getenv("GITHUB_TOKEN") or os.getenv("VLLM_ASCEND_TOKEN")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Build-Eye-Monitor/1.0"
        })
        if self.token:
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
            print(f"使用认证 Token 访问 GitHub API")
        else:
            print(f"警告: 未配置 Token，使用公共 API（速率限制: 60次/小时）")
        self.rate_limit_remaining = 60 if not self.token else 5000
        self.rate_limit_reset_time = None
        self._cache_dir = Path("cache")
        self._cache_dir.mkdir(exist_ok=True)
    
    def _check_rate_limit(self) -> bool:
        """检查速率限制状态。"""
        if self.rate_limit_remaining <= 100:
            if self.rate_limit_reset_time:
                wait_seconds = (self.rate_limit_reset_time - datetime.now()).total_seconds()
                if wait_seconds > 0:
                    print(f"接近速率限制，等待 {wait_seconds:.0f} 秒...")
                    time.sleep(wait_seconds + 10)
                    return self._refresh_rate_limit()
            return False
        return True
    
    def _refresh_rate_limit(self) -> bool:
        """刷新速率限制状态。"""
        response = self.session.get(f"{self.BASE_URL}/rate_limit")
        if response.status_code == 200:
            data = response.json()
            self.rate_limit_remaining = data["resources"]["core"]["remaining"]
            reset_timestamp = data["resources"]["core"]["reset"]
            self.rate_limit_reset_time = datetime.fromtimestamp(reset_timestamp)
            print(f"速率限制状态: {self.rate_limit_remaining} / 5000")
            return True
        return False
    
    def _request_with_retry(self, method: str, url: str, **kwargs) -> Optional[Dict]:
        """带重试的请求方法。"""
        max_retries = 3
        backoff_factor = 2
        
        kwargs.setdefault('timeout', self.timeout)
        
        for attempt in range(max_retries):
            try:
                self._check_rate_limit()
                
                response = self.session.request(method, url, **kwargs)
                
                if response.status_code == 200:
                    self.rate_limit_remaining -= 1
                    return response.json()
                
                if response.status_code == 401:
                    print(f"认证失败 (401): {url}")
                    print(f"请配置 VLLM_ASCEND_TOKEN secret")
                    return None
                
                if response.status_code == 403:
                    if "rate limit exceeded" in response.text.lower():
                        wait_time = backoff_factor ** attempt
                        print(f"速率限制耗尽，等待 {wait_time} 秒后重试...")
                        time.sleep(wait_time)
                        self._refresh_rate_limit()
                        continue
                    else:
                        print(f"访问被拒绝 (403): {url}")
                        return None
                
                if response.status_code == 404:
                    print(f"资源不存在 (404): {url}")
                    return None
                
                if attempt < max_retries - 1:
                    wait_time = backoff_factor ** attempt
                    print(f"请求失败 ({response.status_code})，等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
            
            except requests.exceptions.Timeout:
                print(f"请求超时 ({self.timeout}s): {url}")
                if attempt < max_retries - 1:
                    time.sleep(backoff_factor ** attempt)
                continue
            
            except requests.exceptions.RequestException as e:
                print(f"请求异常: {e}")
                if attempt < max_retries - 1:
                    time.sleep(backoff_factor ** attempt)
                continue
        
        print(f"请求失败，已达最大重试次数: {url}")
        return None
    
    def get_workflow_runs(self, owner: str, repo: str, branch: str | None = None,
                          status: str | None = None, created: str | None = None,
                          event: str | None = None,
                          per_page: int = 100, max_pages: int = 10) -> List[Dict]:
        """获取仓库的 workflow runs 列表。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/actions/runs"
        params: Dict[str, Any] = {"per_page": per_page}
        
        if branch:
            params["branch"] = branch
        if status:
            params["status"] = status
        if created:
            params["created"] = created
        if event:
            params["event"] = event
        
        runs = []
        page = 1
        
        while page <= max_pages:
            params["page"] = page
            data = self._request_with_retry("GET", url, params=params)
            
            if not data or not data.get("workflow_runs"):
                break
            
            runs.extend(data["workflow_runs"])
            
            if len(data["workflow_runs"]) < per_page:
                break
            
            page += 1
        
        return runs
    
    def get_workflow_run(self, owner: str, repo: str, run_id: int) -> Optional[Dict]:
        """获取单个 workflow run 详情。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/actions/runs/{run_id}"
        return self._request_with_retry("GET", url)
    
    def get_workflow_run_jobs(self, owner: str, repo: str, run_id: int) -> List[Dict]:
        """获取 workflow run 的 jobs 列表。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/actions/runs/{run_id}/jobs"
        data = self._request_with_retry("GET", url)
        return data.get("jobs", []) if data else []
    
    def get_job_logs(self, owner: str, repo: str, job_id: int) -> Optional[str]:
        """获取 job 的构建日志。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/actions/jobs/{job_id}/logs"
        response = self.session.get(url)
        
        if response.status_code == 200:
            return response.text
        return None
    
    def get_pr_for_commit(self, owner: str, repo: str, commit_sha: str) -> Optional[Dict]:
        """获取 commit 对应的 PR 信息。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits/{commit_sha}/pulls"
        data = self._request_with_retry("GET", url)
        
        if data and len(data) > 0:
            return data[0]
        return None
    
    def get_pr(self, owner: str, repo: str, pr_number: int) -> Optional[Dict]:
        """获取 PR 详情。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls/{pr_number}"
        return self._request_with_retry("GET", url)
    
    def get_workflow_definition(self, owner: str, repo: str, workflow_id: str) -> Optional[Dict]:
        """获取 workflow 定义文件（带缓存）。"""
        cache_file = self._cache_dir / f"workflow_{workflow_id.replace('/', '_')}.json"
        cache_ttl_hours = 24
        
        if cache_file.exists():
            cache_data = json.loads(cache_file.read_text(encoding='utf-8'))
            cached_at = datetime.fromisoformat(cache_data["cached_at"])
            if datetime.now() - cached_at < timedelta(hours=cache_ttl_hours):
                return cache_data["data"]
        
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}"
        data = self._request_with_retry("GET", url)
        
        if data:
            cache_data = {
                "cached_at": datetime.now().isoformat(),
                "data": data
            }
            cache_file.write_text(json.dumps(cache_data))
        
        return data
    
    def search_pr_by_title(self, owner: str, repo: str, title: str) -> Optional[Dict]:
        """通过标题搜索 PR（用于 display_title 关联）。"""
        import urllib.parse
        query = urllib.parse.quote(f"repo:{owner}/{repo} type:pr in:title {title[:60]}")
        url = f"{self.BASE_URL}/search/issues?q={query}"
        data = self._request_with_retry("GET", url)
        
        if data and data.get("total_count", 0) > 0:
            items = data.get("items", [])
            for item in items:
                if item.get("title", "").strip() == title.strip():
                    return {
                        "number": item["number"],
                        "title": item["title"],
                        "state": item["state"],
                        "url": item.get("html_url", ""),
                        "user": {"login": item.get("user", {}).get("login", "unknown")},
                        "base": {"ref": "main"},
                        "head": {"ref": ""}
                    }
            if items:
                return {
                    "number": items[0]["number"],
                    "title": items[0]["title"],
                    "state": items[0]["state"],
                    "url": items[0].get("html_url", ""),
                    "user": {"login": items[0].get("user", {}).get("login", "unknown")},
                    "base": {"ref": "main"},
                    "head": {"ref": ""}
                }
        return None
        """获取最近合并的 PR 列表。"""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls"
        params = {
            "state": "closed",
            "sort": "updated",
            "direction": "desc",
            "per_page": 100
        }
        
        data = self._request_with_retry("GET", url, params=params)
        
        if not data:
            return []
        
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        merged_prs = []
        for pr in data:
            if pr.get("merged_at"):
                merged_at = datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00"))
                if merged_at > cutoff_time and pr["base"]["ref"] == "main":
                    merged_prs.append(pr)
        
        return merged_prs


def create_client() -> GitHubAPIClient:
    """创建 GitHub API 客户端实例。"""
    return GitHubAPIClient()