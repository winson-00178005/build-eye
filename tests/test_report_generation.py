"""报告生成测试 - 验证检查。"""
import pytest
import yaml
from pathlib import Path
from scripts.report.generator import ReportGenerator


def test_frontmatter_yaml_valid():
    """测试 YAML frontmatter 可解析。"""
    
    generator = ReportGenerator()
    
    data = {
        "pr_number": 123,
        "workflow_run_id": 456789,
        "classification": {
            "classification": "code",
            "confidence": "high",
            "category_detail": "测试断言失败"
        },
        "recommendations": {
            "recommendations": []
        }
    }
    
    report = generator.generate_report(data)
    
    lines = report.split("\n")
    
    yaml_start = lines.index("---")
    yaml_end = lines.index("---", yaml_start + 1)
    
    yaml_content = "\n".join(lines[yaml_start + 1:yaml_end])
    
    parsed = yaml.safe_load(yaml_content)
    
    assert parsed["pr_number"] == 123
    assert parsed["classification"] == "code"


def test_report_filename_format():
    """测试报告文件名格式。"""
    
    generator = ReportGenerator()
    
    data = {
        "pr_number": 123,
        "classification": {"classification": "code"}
    }
    
    filename = generator.generate_filename(data)
    
    assert filename == "code-pr-123.md"
    
    data_no_pr = {
        "workflow_run_id": 789,
        "classification": {"classification": "infrastructure"}
    }
    
    filename = generator.generate_filename(data_no_pr)
    
    assert filename == "infrastructure-789.md"


def test_section_headers_consistent():
    """测试章节标题一致性。"""
    
    generator = ReportGenerator()
    
    data = {
        "pr_number": 1,
        "classification": {"classification": "infrastructure", "reasoning": "test"},
        "recommendations": {"recommendations": [{"step": 1, "action": "test", "detail": "", "effort": "low", "commands": []}]},
        "metadata": {"workflow_run": {"url": "http://example.com"}, "failed_jobs": []}
    }
    
    report = generator.generate_report(data)
    
    assert "## 概要" in report
    assert "## 根因分析" in report
    assert "## 证据" in report
    assert "## 修复建议" in report


if __name__ == "__main__":
    pytest.main([__file__, "-v"])