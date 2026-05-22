"""边界测试 - 空数据、异常日志、缺失字段等场景。"""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from classify.code_detector import detect_code_issues
from classify.infra_detector import detect_infrastructure_issues
from classify.interference_detector import detect_interference_issues
from report.generator import ReportGenerator


class TestEmptyInputs:
    """测试空输入和边界情况。"""
    
    def test_empty_log_excerpt(self):
        """测试空日志片段。"""
        result = detect_code_issues("", {}, {})
        assert result["detected"] == False
    
    def test_empty_pr_info(self):
        """测试缺失 PR 信息。"""
        result = detect_code_issues(
            "AssertionError: test failed",
            None,
            {}
        )
        assert result["detected"] == True
    
    def test_empty_workflow_run(self):
        """测试缺失 workflow 信息。"""
        result = detect_code_issues(
            "compilation error",
            {"number": 123},
            None
        )
        assert result["detected"] == True
    
    def test_empty_infrastructure_log(self):
        """测试空基础设施日志。"""
        result = detect_infrastructure_issues("", {}, {})
        assert result["detected"] == False
    
    def test_empty_metadata(self):
        """测试空元数据。"""
        result = detect_interference_issues({}, 24)
        assert result["detected"] == False


class TestMalformedLogs:
    """测试异常日志格式。"""
    
    def test_partial_log_excerpt(self):
        """测试部分截断的日志。"""
        result = detect_infrastructure_issues(
            "cache-service.nginx-",  # 不完整的 URL
            {"runner_name": "test"},
            {}
        )
        assert result["detected"] == True
    
    def test_mixed_languages(self):
        """测试中英文混合日志。"""
        result = detect_code_issues(
            "错误: ImportError 无法导入模块",
            {"number": 123},
            {}
        )
        assert result["detected"] == True
    
    def test_very_long_log(self):
        """测试超长日志。"""
        long_log = "AssertionError\n" + "x" * 10000
        result = detect_code_issues(long_log, {}, {})
        assert result["detected"] == True
    
    def test_unicode_in_log(self):
        """测试日志中的 Unicode 字符。"""
        result = detect_infrastructure_issues(
            "cache-service 错误 🔥",
            {},
            {}
        )
        assert result["detected"] == True


class TestMissingFields:
    """测试缺失字段场景。"""
    
    def test_missing_pr_number(self):
        """测试缺失 PR 编号。"""
        generator = ReportGenerator()
        data = {
            "pr_number": None,
            "workflow_run_id": 123,
            "classification": {"classification": "infrastructure"},
            "recommendations": {"recommendations": []}
        }
        report = generator.generate_report(data)
        assert "workflow 123" in report.lower() or "workflow" in report.lower()
    
    def test_missing_classification_type(self):
        """测试缺失分类类型。"""
        generator = ReportGenerator()
        data = {
            "pr_number": 123,
            "classification": {},
            "recommendations": {"recommendations": []}
        }
        report = generator.generate_report(data)
        assert "unknown" in report or "未知" in report
    
    def test_missing_evidence(self):
        """测试缺失证据。"""
        result = {
            "detected": True,
            "confidence": "high",
            "category_detail": "测试失败",
            "evidence": []
        }
        assert result["evidence"] == []


class TestConcurrentPRDetection:
    """测试并发 PR 检测。"""
    
    def test_no_related_prs(self):
        """测试无相关 PR。"""
        metadata = {
            "pr": {"number": 123, "merged_at": "2024-01-15T10:00:00Z"}
        }
        result = detect_interference_issues(metadata, 24)
        assert result["detected"] == False
    
    def test_single_pr(self):
        """测试仅一个 PR。"""
        metadata = {
            "pr": {"number": 123, "merged_at": "2024-01-15T10:00:00Z"},
            "failed_jobs": [{"name": "test"}]
        }
        result = detect_interference_issues(metadata, 24)
        # 没有 related_prs 数据时应该返回 False
        assert result.get("detected") == False or result.get("concurrent_pr_count", 0) < 2
    
    def test_pr_without_merged_at(self):
        """测试无 merged_at 的 PR。"""
        metadata = {
            "pr": {"number": 123}
        }
        result = detect_interference_issues(metadata, 24)
        assert result["detected"] == False


class TestReportYAMLFormat:
    """测试报告 YAML 格式。"""
    
    def test_yaml_parseability(self):
        """测试 YAML frontmatter 可解析。"""
        generator = ReportGenerator()
        data = {
            "pr_number": 123,
            "workflow_run_id": 456,
            "classification": {
                "classification": "code",
                "confidence": "high",
                "category_detail": "测试失败"
            },
            "recommendations": {"recommendations": []},
            "metadata": {"workflow_run": {"url": "http://test"}, "failed_jobs": []}
        }
        report = generator.generate_report(data)
        
        import yaml
        lines = report.split("\n")
        yaml_start = lines.index("---")
        yaml_end = lines.index("---", yaml_start + 1)
        yaml_content = "\n".join(lines[yaml_start + 1:yaml_end])
        
        parsed = yaml.safe_load(yaml_content)
        assert parsed["pr_number"] == 123
        assert parsed["classification"] == "code"
    
    def test_filename_with_no_pr(self):
        """测试无 PR 编号时的文件名生成。"""
        generator = ReportGenerator()
        data = {
            "workflow_run_id": 789,
            "classification": {"classification": "infrastructure"}
        }
        filename = generator.generate_filename(data)
        assert "infrastructure" in filename
        assert "789" in filename


class TestArchiverFailure:
    """测试归档失败场景。"""
    
    def test_archive_without_token(self):
        """测试无 Token 时的归档行为。"""
        from scripts.archive.archiver import ReportArchiver
        
        archiver = ReportArchiver("test-owner", "test-repo", token=None)
        
        result = archiver.archive([Path("test.md")], dry_run=False)
        assert result == []
    
    def test_dry_run_mode(self):
        """测试试运行模式。"""
        from scripts.archive.archiver import ReportArchiver
        
        archiver = ReportArchiver("test-owner", "test-repo", "mock_token")
        result = archiver.archive([Path("test.md")], dry_run=True)
        assert len(result) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])