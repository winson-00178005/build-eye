"""归档测试 - 模拟仓库操作，包含清理当天旧报告功能测试。"""
import pytest
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from scripts.archive.archiver import ReportArchiver


def test_dry_run_mode():
    """测试试运行模式。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    report_files = [Path("test.md")]

    result = archiver.archive(report_files, dry_run=True)

    assert result == ["test.md"]


def test_no_token_warning():
    """测试无 token 警告。"""

    archiver = ReportArchiver("test-owner", "test-repo", token=None)

    report_files = [Path("test.md")]

    result = archiver.archive(report_files, dry_run=False)

    assert result == []


def test_clean_date_reports_no_existing():
    """测试当天无已有报告时，clean 直接返回 0。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    with patch.object(archiver, '_list_dir', return_value=[]):
        deleted = archiver.clean_date_reports("2025/01/15")

    assert deleted == 0


def test_clean_date_reports_with_files():
    """测试当天已有报告文件时，clean 删除并返回删除数。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_items = [
        {"type": "dir", "path": "reports/2025/01/15/code-pr-1234", "sha": "dir-sha1"},
        {"type": "file", "path": "reports/2025/01/15/old-report.md", "sha": "file-sha1"}
    ]

    mock_sub_items = [
        {"type": "file", "path": "reports/2025/01/15/code-pr-1234/report.md", "sha": "sub-file-sha1"}
    ]

    with patch.object(archiver, '_list_dir') as mock_list, \
         patch.object(archiver, '_delete_file', return_value=True) as mock_delete:

        mock_list.side_effect = [mock_items, mock_items, mock_sub_items]

        deleted = archiver.clean_date_reports("2025/01/15")

    assert deleted == 2
    assert mock_delete.call_count == 2


def test_clean_date_reports_delete_failure_skipped():
    """测试删除失败时跳过文件，继续删除其他文件。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_items = [
        {"type": "file", "path": "reports/2025/01/15/report-a.md", "sha": "sha-a"},
        {"type": "file", "path": "reports/2025/01/15/report-b.md", "sha": "sha-b"},
        {"type": "file", "path": "reports/2025/01/15/report-c.md", "sha": "sha-c"}
    ]

    with patch.object(archiver, '_list_dir', return_value=mock_items), \
         patch.object(archiver, '_delete_file') as mock_delete:

        mock_delete.side_effect = [False, True, True]

        deleted = archiver.clean_date_reports("2025/01/15")

    assert deleted == 2


def test_archive_calls_clean_before_write():
    """测试 archive 方法在写入前调用 clean_date_reports。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    with tempfile.TemporaryDirectory() as tmp_dir:
        report_file = Path(tmp_dir) / "test.md"
        report_file.write_text("---\npr_number: 1\n---\nTest report")

        with patch.object(archiver, 'clean_date_reports', return_value=0) as mock_clean, \
             patch.object(archiver, '_create_file', return_value=True):

            archiver.archive([report_file], ["code-pr-1"], dry_run=False)

        mock_clean.assert_called_once()


def test_delete_file_success():
    """测试 _delete_file 成功。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_response = Mock()
    mock_response.status_code = 200

    with patch.object(archiver.session, 'delete', return_value=mock_response):
        result = archiver._delete_file("reports/2025/01/15/old.md", "abc123", "Remove old")

    assert result == True


def test_delete_file_failure():
    """测试 _delete_file 失败。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_response = Mock()
    mock_response.status_code = 404

    with patch.object(archiver.session, 'delete', return_value=mock_response):
        result = archiver._delete_file("reports/2025/01/15/old.md", "abc123", "Remove old")

    assert result == False


def test_list_dir_success():
    """测试 _list_dir 成功返回目录内容。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_items = [
        {"type": "file", "path": "reports/2025/01/15/a.md", "sha": "sha1"},
        {"type": "dir", "path": "reports/2025/01/15/sub", "sha": "sha2"}
    ]

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json = Mock(return_value=mock_items)

    with patch.object(archiver.session, 'get', return_value=mock_response):
        result = archiver._list_dir("reports/2025/01/15")

    assert len(result) == 2


def test_list_dir_not_found():
    """测试 _list_dir 目录不存在时返回空列表。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_response = Mock()
    mock_response.status_code = 404

    with patch.object(archiver.session, 'get', return_value=mock_response):
        result = archiver._list_dir("reports/2025/01/15")

    assert result == []


def test_delete_dir_recursive_nested():
    """测试 _delete_dir_recursive 处理嵌套子目录。"""

    archiver = ReportArchiver("test-owner", "test-repo", "mock_token")

    mock_root = [
        {"type": "dir", "path": "reports/2025/01/15/code-pr-1", "sha": "d1"},
        {"type": "file", "path": "reports/2025/01/15/top.md", "sha": "f1"}
    ]

    mock_subdir = [
        {"type": "file", "path": "reports/2025/01/15/code-pr-1/report.md", "sha": "f2"},
        {"type": "dir", "path": "reports/2025/01/15/code-pr-1/evidence", "sha": "d2"}
    ]

    mock_nested = [
        {"type": "file", "path": "reports/2025/01/15/code-pr-1/evidence/log.txt", "sha": "f3"}
    ]

    with patch.object(archiver, '_list_dir') as mock_list, \
         patch.object(archiver, '_delete_file', return_value=True):

        mock_list.side_effect = [mock_root, mock_subdir, mock_nested]

        deleted = archiver._delete_dir_recursive("reports/2025/01/15")

    assert deleted == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])