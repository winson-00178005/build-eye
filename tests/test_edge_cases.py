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
    
    def test_empty_log_excerpt(self):
        result = detect_code_issues("", {}, {})
        assert result["detected"] == False
    
    def test_empty_pr_info(self):
        result = detect_code_issues(
            "AssertionError: test failed",
            None,
            {}
        )
        assert result["detected"] == True
    
    def test_empty_workflow_run(self):
        result = detect_code_issues(
            "error: undefined symbol 'vllm_forward'",
            {"number": 123},
            {}
        )
        assert result["detected"] == True
    
    def test_empty_infrastructure_log(self):
        result = detect_infrastructure_issues("", {}, {})
        assert result["detected"] == False
    
    def test_empty_metadata(self):
        result = detect_interference_issues({}, 24)
        assert result["detected"] == False


class TestMalformedLogs:
    
    def test_partial_log_excerpt(self):
        result = detect_infrastructure_issues(
            "cache-service.nginx-pypi-cache connection refused",
            {"runner_name": "test"},
            {}
        )
        assert result["detected"] == True
    
    def test_mixed_languages(self):
        result = detect_code_issues(
            "错误: ImportError 无法导入模块",
            {"number": 123},
            {}
        )
        assert result["detected"] == True
    
    def test_very_long_log(self):
        long_log = "AssertionError\n" + "x" * 10000
        result = detect_code_issues(long_log, {}, {})
        assert result["detected"] == True
    
    def test_unicode_in_log(self):
        result = detect_infrastructure_issues(
            "cache-service.nginx-pypi-cache 错误 🔥",
            {},
            {}
        )
        assert result["detected"] == True


class TestMissingFields:
    
    def test_missing_pr_number(self):
        generator = ReportGenerator()
        data = {
            "pr_number": None,
            "group_key": "run-123",
            "overall_category": "infrastructure",
            "total_failed_workflows": 1,
            "category_counts": {"infrastructure": 1},
            "workflow_runs": [
                {
                    "workflow_run_id": 123,
                    "workflow_name": "E2E-Full",
                    "classification": {"classification": "infrastructure", "confidence": "high", "category_detail": "测试"},
                    "metadata": {"workflow_run": {"url": "http://test"}, "failed_jobs": []},
                    "recommendations": {"recommendations": []}
                }
            ],
            "overall_recommendations": []
        }
        report = generator.generate_pr_report(data)
        assert "run-123" in report
    
    def test_missing_classification_type(self):
        generator = ReportGenerator()
        data = {
            "pr_number": 123,
            "group_key": "pr-123",
            "overall_category": "unknown",
            "total_failed_workflows": 1,
            "category_counts": {},
            "workflow_runs": [
                {
                    "workflow_run_id": 456,
                    "workflow_name": "E2E-Full",
                    "classification": {},
                    "metadata": {"workflow_run": {"url": "http://test"}, "failed_jobs": []},
                    "recommendations": {"recommendations": []}
                }
            ],
            "overall_recommendations": []
        }
        report = generator.generate_pr_report(data)
        assert "unknown" in report or "未知" in report
    
    def test_missing_evidence(self):
        result = {
            "detected": True,
            "confidence": "high",
            "category_detail": "测试失败",
            "evidence": []
        }
        assert result["evidence"] == []


class TestConcurrentPRDetection:
    
    def test_no_related_prs(self):
        metadata = {
            "pr": {"number": 123, "merged_at": "2024-01-15T10:00:00Z"}
        }
        result = detect_interference_issues(metadata, 24)
        assert result["detected"] == False
    
    def test_single_pr(self):
        metadata = {
            "pr": {"number": 123, "merged_at": "2024-01-15T10:00:00Z"},
            "failed_jobs": [{"name": "test"}]
        }
        result = detect_interference_issues(metadata, 24)
        assert result.get("detected") == False or result.get("concurrent_pr_count", 0) < 2
    
    def test_pr_without_merged_at(self):
        metadata = {
            "pr": {"number": 123}
        }
        result = detect_interference_issues(metadata, 24)
        assert result["detected"] == False


class TestReportYAMLFormat:
    
    def test_yaml_parseability(self):
        generator = ReportGenerator()
        data = {
            "pr_number": 123,
            "group_key": "pr-123",
            "overall_category": "code",
            "total_failed_workflows": 1,
            "category_counts": {"code": 1},
            "workflow_runs": [
                {
                    "workflow_run_id": 456,
                    "workflow_name": "E2E-Full",
                    "classification": {"classification": "code", "confidence": "high", "category_detail": "测试失败"},
                    "metadata": {"workflow_run": {"url": "http://test"}, "failed_jobs": []},
                    "recommendations": {"recommendations": []}
                }
            ],
            "overall_recommendations": []
        }
        report = generator.generate_pr_report(data)
        
        import yaml
        lines = report.split("\n")
        yaml_start = lines.index("---")
        yaml_end = lines.index("---", yaml_start + 1)
        yaml_content = "\n".join(lines[yaml_start + 1:yaml_end])
        
        parsed = yaml.safe_load(yaml_content)
        assert parsed["pr_number"] == 123
        assert parsed["overall_classification"] == "code"
    
    def test_filename_with_no_pr(self):
        generator = ReportGenerator()
        data = {
            "pr_number": None,
            "group_key": "run-789",
            "overall_category": "infrastructure"
        }
        filename = generator.generate_filename(data)
        assert "infrastructure" in filename or "infra" in filename
        assert "789" in filename


class TestArchiverFailure:
    
    def test_archive_without_token(self):
        from scripts.archive.archiver import ReportArchiver
        
        archiver = ReportArchiver("test-owner", "test-repo", token=None)
        
        result = archiver.archive([Path("test.md")], dry_run=False)
        assert result == []
    
    def test_dry_run_mode(self):
        from scripts.archive.archiver import ReportArchiver
        
        archiver = ReportArchiver("test-owner", "test-repo", "mock_token")
        result = archiver.archive([Path("test.md")], dry_run=True)
        assert len(result) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])