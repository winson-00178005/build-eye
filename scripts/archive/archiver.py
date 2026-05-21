"""报告归档器 - Git 仓库提交。"""
import json
import subprocess
import argparse
import sys
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import List
import tempfile

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))


class ReportArchiver:
    """报告归档器 - 提交到 build-eye 仓库。"""
    
    def __init__(self, repo_url: str, token: str | None = None):
        self.repo_url = repo_url
        self.token = token or os.getenv("ARCHIVE_TOKEN")
        self.reports_dir = "reports"
    
    def archive(self, report_files: List[Path], dry_run: bool = False) -> List[Path]:
        """归档报告文件到 Git 仓库。"""
        
        if not report_files:
            print("没有报告需要归档")
            return []
        
        if dry_run:
            print("[试运行] 模拟归档以下报告:")
            for f in report_files:
                print(f"  - {f.name}")
            return report_files
        
        if not self.token:
            print("警告: 未配置 ARCHIVE_TOKEN，无法归档")
            return []
        
        with tempfile.TemporaryDirectory() as tmp_dir:
            work_dir = Path(tmp_dir)
            
            self._clone_repo(work_dir)
            
            archived_paths = []
            
            for report_file in report_files:
                dest_path = self._get_archive_path(report_file, work_dir)
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                content = report_file.read_text(encoding='utf-8')
                dest_path.write_text(content, encoding='utf-8')
                
                archived_paths.append(dest_path)
            
            self._commit_and_push(work_dir)
            
            return archived_paths
    
    def _clone_repo(self, work_dir: Path):
        """克隆归档仓库。"""
        
        auth_url = self._get_auth_url()
        
        subprocess.run(
            ["git", "clone", "--depth=1", auth_url, str(work_dir)],
            check=True,
            capture_output=True
        )
        
        print(f"已克隆仓库到 {work_dir}")
    
    def _get_auth_url(self) -> str:
        """获取带认证的仓库 URL。"""
        
        if self.token:
            if "github.com" in self.repo_url:
                return self.repo_url.replace(
                    "github.com",
                    f"{self.token}@github.com"
                )
        
        return self.repo_url
    
    def _get_archive_path(self, report_file: Path, work_dir: Path) -> Path:
        """计算归档目标路径。"""
        
        now = datetime.now()
        
        year = str(now.year)
        month = f"{now.month:02d}"
        day = f"{now.day:02d}"
        
        relative_path = Path(self.reports_dir) / year / month / day / report_file.name
        
        return work_dir / relative_path
    
    def _commit_and_push(self, work_dir: Path):
        """提交并推送更改。"""
        
        subprocess.run(
            ["git", "config", "user.name", "Build-Eye Bot"],
            cwd=work_dir,
            check=True
        )
        
        subprocess.run(
            ["git", "config", "user.email", "build-eye-bot@example.com"],
            cwd=work_dir,
            check=True
        )
        
        subprocess.run(
            ["git", "add", "."],
            cwd=work_dir,
            check=True
        )
        
        commit_msg = self._generate_commit_message()
        
        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=work_dir,
            check=True,
            capture_output=True
        )
        
        subprocess.run(
            ["git", "push"],
            cwd=work_dir,
            check=True,
            capture_output=True
        )
        
        print(f"已提交并推送: {commit_msg}")
    
    def _generate_commit_message(self) -> str:
        """生成提交消息。"""
        
        now = datetime.now(timezone.utc)
        date_str = now.strftime("%Y-%m-%d %H:%M UTC")
        
        return f"Add monitoring reports - {date_str}"


def main():
    parser = argparse.ArgumentParser(description='归档报告到 build-eye 仓库')
    parser.add_argument('--input', type=str, default='reports/',
                        help='报告目录')
    parser.add_argument('--repo', type=str, 
                        default='https://github.com/winson-00178005/build-eye.git',
                        help='归档仓库 URL')
    parser.add_argument('--dry-run', action='store_true',
                        help='试运行模式')
    
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    if not input_dir.exists():
        print(f"报告目录不存在: {input_dir}")
        return
    
    report_files = list(input_dir.glob("*.md"))
    
    archiver = ReportArchiver(args.repo)
    
    archived = archiver.archive(report_files, args.dry_run)
    
    print(f"已归档 {len(archived)} 个报告")


if __name__ == "__main__":
    main()