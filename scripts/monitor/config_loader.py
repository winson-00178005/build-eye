"""配置管理模块 - 环境变量和配置文件加载。"""
import os
import yaml
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent / "config" / "config.yaml"


class Config:
    """系统配置管理类。"""
    
    def __init__(self, config_path: Path | None = None):
        self.config_path = config_path or DEFAULT_CONFIG_PATH
        self._config = self._load_config()
        self._override_from_env()
    
    def _load_config(self) -> Dict[str, Any]:
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        return {
            "target_repository": {
                "owner": "vllm-project",
                "repo": "vllm-ascend",
                "url": "https://github.com/vllm-project/vllm-ascend",
                "branch": "main"
            },
            "archive_repository": {
                "owner": "winson-00178005",
                "repo": "build-eye",
                "url": "https://github.com/winson-00178005/build-eye.git"
            },
            "monitoring": {
                "polling_interval_hours": 6,
                "lookback_hours": 24
            },
            "api": {
                "rate_limit_threshold_percent": 20,
                "retry_max_attempts": 3
            }
        }
    
    def _override_from_env(self):
        if os.getenv("TARGET_REPO_OWNER"):
            self._config["target_repository"]["owner"] = os.getenv("TARGET_REPO_OWNER")
        if os.getenv("TARGET_REPO_NAME"):
            self._config["target_repository"]["repo"] = os.getenv("TARGET_REPO_NAME")
        if os.getenv("ARCHIVE_REPO_URL"):
            self._config["archive_repository"]["url"] = os.getenv("ARCHIVE_REPO_URL")
        if os.getenv("GITHUB_TOKEN"):
            self._config["api"]["token"] = os.getenv("GITHUB_TOKEN")
        if os.getenv("ARCHIVE_TOKEN"):
            self._config["archive_repository"]["token"] = os.getenv("ARCHIVE_TOKEN")
    
    @property
    def target_repo(self) -> Dict[str, str]:
        return self._config["target_repository"]
    
    @property
    def archive_repo(self) -> Dict[str, str]:
        return self._config["archive_repository"]
    
    @property
    def monitoring(self) -> Dict[str, Any]:
        return self._config["monitoring"]
    
    @property
    def api(self) -> Dict[str, Any]:
        return self._config["api"]

    @property
    def pipeline_types(self) -> Dict[str, Any]:
        return self._config.get("pipeline_types", {})


config = Config()