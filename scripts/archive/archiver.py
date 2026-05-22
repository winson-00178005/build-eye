"""报告归档器 - 通过 GitHub Contents API 直接提交文件到仓库。"""
import base64
import json
import argparse
import sys
import os
import time
import requests
from datetime import datetime, timezone
from pathlib import Path
from typing import List

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))


class ReportArchiver:
    """报告归档器 - 使用 GitHub Contents API 提交到 build-eye 仓库。"""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, repo_owner: str, repo_name: str, token: str | None = None):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.token = token or os.getenv("GITHUB_TOKEN") or os.getenv("ARCHIVE_TOKEN")
        self.reports_dir = "reports"
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Build-Eye-Monitor/1.0"
        })
        if self.token:
            self.session.headers.update({
                "Authorization": f"Bearer {self.token}"
            })
    
    def _list_dir(self, path: str) -> list:
        """列出 GitHub 仓库目录下的所有内容。"""
        url = f"{self.BASE_URL}/repos/{self.repo_owner}/{self.repo_name}/contents/{path}"
        response = self.session.get(url)
        
        if response.status_code == 200:
            return response.json()
        
        return []
    
    def _delete_file(self, path: str, sha: str, commit_msg: str) -> bool:
        """通过 GitHub Contents API 删除文件。"""
        url = f"{self.BASE_URL}/repos/{self.repo_owner}/{self.repo_name}/contents/{path}"
        data = {
            "message": commit_msg,
            "sha": sha,
            "branch": "main"
        }
        
        response = self.session.delete(url, json=data)
        
        if response.status_code == 200:
            return True
        
        print(f"删除失败 ({response.status_code}): {path}")
        return False
    
    def _delete_dir_recursive(self, dir_path: str) -> int:
        """递归删除 GitHub 仓库目录下的所有文件和子目录。"""
        deleted = 0
        items = self._list_dir(dir_path)
        
        for item in items:
            item_type = item.get("type", "")
            item_path = item.get("path", "")
            item_sha = item.get("sha", "")
            
            if item_type == "dir":
                deleted += self._delete_dir_recursive(item_path)
            elif item_type == "file":
                commit_msg = f"Remove old report: {item_path}"
                if self._delete_file(item_path, item_sha, commit_msg):
                    deleted += 1
                    time.sleep(0.3)
                else:
                    print(f"  跳过: {item_path}")
        
        return deleted
    
    def clean_date_reports(self, date_path: str) -> int:
        """清除指定日期目录下的所有已有报告。"""
        full_path = f"{self.reports_dir}/{date_path}"
        
        print(f"检查已有报告: {full_path}")
        
        items = self._list_dir(full_path)
        
        if not items:
            print("当日无已有报告，直接写入")
            return 0
        
        print(f"发现 {len(items)} 个已有目录/文件，正在清除...")
        
        deleted = self._delete_dir_recursive(full_path)
        
        print(f"已清除 {deleted} 个旧文件")
        return deleted
    
    def archive(self, report_files: List[Path], group_keys: List[str] | None = None, dry_run: bool = False) -> List[str]:
        """归档报告文件到 GitHub 仓库。每个 PR 一个子目录。归档前先清除当天旧报告。"""
        
        if not report_files:
            print("没有报告需要归档")
            return []
        
        if dry_run:
            print("[试运行] 模拟归档以下报告:")
            for f in report_files:
                print(f"  - {f.name}")
            return [f.name for f in report_files]
        
        if not self.token:
            print("警告: 未配置 Token，无法归档到仓库")
            return []
        
        now = datetime.now(timezone.utc)
        date_path = f"{now.year}/{now.month:02d}/{now.day:02d}"
        
        self.clean_date_reports(date_path)
        
        archived = []
        
        for i, report_file in enumerate(report_files):
            group_key = (group_keys[i] if group_keys and i < len(group_keys)
                         else report_file.stem)
            
            repo_path = f"{self.reports_dir}/{date_path}/{group_key}/report.md"
            
            content = report_file.read_text(encoding='utf-8')
            encoded = base64.b64encode(content.encode('utf-8')).decode('utf-8')
            
            commit_msg = f"Add monitoring report for {group_key}"
            
            success = self._create_file(repo_path, encoded, commit_msg)
            
            if success:
                archived.append(repo_path)
                print(f"已归档: {repo_path}")
                time.sleep(0.3)
            else:
                print(f"归档失败: {repo_path}")
        
        print(f"已归档 {len(archived)} 个报告到 {self.repo_owner}/{self.repo_name}")
        return archived
    
    def _create_file(self, path: str, content_b64: str, commit_msg: str) -> bool:
        """通过 GitHub Contents API 创建文件。"""
        
        url = f"{self.BASE_URL}/repos/{self.repo_owner}/{self.repo_name}/contents/{path}"
        
        data = {
            "message": commit_msg,
            "content": content_b64,
            "branch": "main"
        }
        
        existing_sha = self._get_file_sha(path)
        if existing_sha:
            data["sha"] = existing_sha
        
        response = self.session.put(url, json=data)
        
        if response.status_code in (200, 201):
            return True
        
        print(f"创建文件失败 ({response.status_code}): {path}")
        if response.status_code == 409:
            print("冲突: 文件已被修改，可能需要重试")
        
        return False
    
    def _get_file_sha(self, path: str) -> str | None:
        """获取文件当前 SHA（用于更新已有文件）。"""
        
        url = f"{self.BASE_URL}/repos/{self.repo_owner}/{self.repo_name}/contents/{path}"
        
        response = self.session.get(url)
        
        if response.status_code == 200:
            return response.json().get("sha")
        
        return None


def main():
    parser = argparse.ArgumentParser(description='归档报告到 build-eye 仓库')
    parser.add_argument('--input', type=str, default='reports/',
                        help='报告目录')
    parser.add_argument('--repo', type=str,
                        default='winson-00178005/build-eye',
                        help='归档仓库 (owner/repo格式)')
    parser.add_argument('--dry-run', action='store_true',
                        help='试运行模式')
    
    args = parser.parse_args()
    
    try:
        input_dir = Path(args.input)
        if not input_dir.exists():
            print(f"报告目录不存在: {input_dir}")
            sys.exit(0)
        
        report_files = sorted(input_dir.glob("*.md"))
        
        if not report_files:
            print("没有报告文件")
            sys.exit(0)
        
        group_keys = []
        summary_path = Path("data/summary.json")
        if summary_path.exists():
            summary = json.loads(summary_path.read_text(encoding='utf-8'))
            group_keys = summary.get("group_keys", [])
        
        if not group_keys:
            group_keys = [f.stem for f in report_files]
        
        owner, repo = args.repo.split('/')
        archiver = ReportArchiver(owner, repo)
        
        archived = archiver.archive(report_files, group_keys, args.dry_run)
        
        print(f"已归档 {len(archived)} 个报告")
    except Exception as e:
        print(f"归档异常: {e}")
        sys.exit(0)


if __name__ == "__main__":
    main()