"""Git 客户端封装。"""
import subprocess
from pathlib import Path
from typing import Optional


class GitClient:
    """Git 命令封装。"""
    
    def __init__(self, work_dir: Path):
        self.work_dir = work_dir
    
    def clone(self, url: str, depth: int = 1) -> bool:
        """克隆仓库。"""
        
        result = subprocess.run(
            ["git", "clone", "--depth", str(depth), url, str(self.work_dir)],
            capture_output=True,
            text=True
        )
        
        return result.returncode == 0
    
    def config_user(self, name: str, email: str) -> bool:
        """配置用户信息。"""
        
        subprocess.run(
            ["git", "config", "user.name", name],
            cwd=self.work_dir,
            check=True
        )
        
        subprocess.run(
            ["git", "config", "user.email", email],
            cwd=self.work_dir,
            check=True
        )
        
        return True
    
    def add(self, path: str = ".") -> bool:
        """添加文件到暂存区。"""
        
        result = subprocess.run(
            ["git", "add", path],
            cwd=self.work_dir,
            capture_output=True,
            text=True
        )
        
        return result.returncode == 0
    
    def commit(self, message: str) -> bool:
        """提交更改。"""
        
        result = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=self.work_dir,
            capture_output=True,
            text=True
        )
        
        return result.returncode == 0
    
    def push(self, remote: str = "origin", branch: str = "main") -> bool:
        """推送到远程仓库。"""
        
        result = subprocess.run(
            ["git", "push", remote, branch],
            cwd=self.work_dir,
            capture_output=True,
            text=True
        )
        
        return result.returncode == 0
    
    def status(self) -> str:
        """获取状态。"""
        
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=self.work_dir,
            capture_output=True,
            text=True
        )
        
        return result.stdout
    
    def log(self, count: int = 5) -> str:
        """获取日志。"""
        
        result = subprocess.run(
            ["git", "log", "--oneline", f"-{count}"],
            cwd=self.work_dir,
            capture_output=True,
            text=True
        )
        
        return result.stdout