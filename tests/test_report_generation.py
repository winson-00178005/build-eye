"""报告生成测试 - 验证 PR 报告 YAML frontmatter 和文件名。"""
import pytest
import yaml
from pathlib import Path
from scripts.report.generator import ReportGenerator


def test_frontmatter_yaml_valid():
    generator = ReportGenerator()
    
    data = {
        "pr_number": 123,
        "group_key": "pr-123",
        "overall_category": "code",
        "total_failed_workflows": 1,
        "category_counts": {"code": 1},
        "workflow_runs": [
            {
                "workflow_run_id": 456789,
                "workflow_name": "E2E-Full",
                "classification": {"classification": "code", "confidence": "high", "category_detail": "测试断言失败"},
                "metadata": {"workflow_run": {"url": "http://test"}, "failed_jobs": []},
                "recommendations": {"recommendations": []}
            }
        ],
        "overall_recommendations": []
    }
    
    report = generator.generate_pr_report(data)
    
    lines = report.split("\n")
    
    yaml_start = lines.index("---")
    yaml_end = lines.index("---", yaml_start + 1)
    
    yaml_content = "\n".join(lines[yaml_start + 1:yaml_end])
    
    parsed = yaml.safe_load(yaml_content)
    
    assert parsed["pr_number"] == 123
    assert parsed["overall_classification"] == "code"


def test_report_filename_format():
    generator = ReportGenerator()
    
    data_code = {
        "pr_number": 123,
        "group_key": "pr-123",
        "overall_category": "code"
    }
    
    filename = generator.generate_filename(data_code)
    
    assert filename == "report.md"


def test_section_headers_consistent():
    generator = ReportGenerator()
    
    data = {
        "pr_number": 1,
        "group_key": "pr-1",
        "overall_category": "infrastructure",
        "total_failed_workflows": 1,
        "category_counts": {"infrastructure": 1},
        "workflow_runs": [
            {
                "workflow_run_id": 999,
                "workflow_name": "E2E-Full",
                "classification": {"classification": "infrastructure", "confidence": "high", "category_detail": "K8s 问题", "reasoning": "测试推理"},
                "metadata": {"workflow_run": {"url": "http://example.com"}, "failed_jobs": []},
                "recommendations": {"recommendations": []}
            }
        ],
        "overall_recommendations": []
    }
    
    report = generator.generate_pr_report(data)
    
    assert "## 概要" in report
    assert "## Workflow 详细分析" in report
    assert "## 修复建议" in report


if __name__ == "__main__":
    pytest.main([__file__, "-v"])