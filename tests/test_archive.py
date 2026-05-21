"""归档测试 - 模拟仓库操作。"""
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from scripts.archive.archiver import ReportArchiver


def test_archive_path_generation():
    """测试归档路径生成。"""
    
    archiver = ReportArchiver("https://github.com/test/test.git", "mock_token")
    
    report_file = Path("code-pr-123.md")
    
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_dir:
        work_dir = Path(tmp_dir)
        
        dest_path = archiver._get_archive_path(report_file, work_dir)
        
        assert "reports" in str(dest_path)
        assert dest_path.name == "code-pr-123.md"


def test_dry_run_mode():
    """测试试运行模式。"""
    
    archiver = ReportArchiver("https://github.com/test/test.git", "mock_token")
    
    report_files = [Path("test.md")]
    
    result = archiver.archive(report_files, dry_run=True)
    
    assert result == report_files


def test_no_token_warning():
    """测试无 token 警告。"""
    
    archiver = ReportArchiver("https://github.com/test/test.git", token=None)
    
    report_files = [Path("test.md")]
    
    result = archiver.archive(report_files, dry_run=False)
    
    assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])