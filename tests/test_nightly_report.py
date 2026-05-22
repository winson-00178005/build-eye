"""Nightly Report 测试。"""
import pytest
from scripts.report.nightly_report import NightlyReportGenerator


MOCK_NIGHTLY_RUNS = [
    {
        "id": 1001,
        "name": "Nightly-A2",
        "conclusion": "failure",
        "started_at": "2025-01-15T03:00:00Z",
        "completed_at": "2025-01-15T05:00:00Z",
        "classification": {
            "classification": "infrastructure",
            "confidence": "high",
            "category_detail": "K8s cache-service 不可用"
        }
    },
    {
        "id": 1002,
        "name": "Nightly-A3",
        "conclusion": "success",
        "started_at": "2025-01-15T03:00:00Z",
        "completed_at": "2025-01-15T04:30:00Z",
        "classification": {}
    }
]


def test_generate_daily_report():
    gen = NightlyReportGenerator()
    report = gen.generate_daily_report(MOCK_NIGHTLY_RUNS, "2025-01-15")

    assert "---" in report
    assert "Nightly 构建报告" in report
    assert "2025-01-15" in report
    assert "概览" in report
    assert "失败详情" in report


def test_report_contains_frontmatter():
    gen = NightlyReportGenerator()
    report = gen.generate_daily_report(MOCK_NIGHTLY_RUNS, "2025-01-15")

    assert "report_type: nightly_daily" in report
    assert "total_runs: 2" in report
    assert "failure_runs: 1" in report


def test_report_overview_table():
    gen = NightlyReportGenerator()
    report = gen.generate_daily_report(MOCK_NIGHTLY_RUNS, "2025-01-15")

    assert "运行总数" in report
    assert "成功率" in report


def test_report_failure_details():
    gen = NightlyReportGenerator()
    report = gen.generate_daily_report(MOCK_NIGHTLY_RUNS, "2025-01-15")

    assert "基础设施问题" in report
    assert "Nightly-A2" in report


def test_report_no_failures():
    runs = [{"id": 1, "name": "Nightly-A2", "conclusion": "success", "classification": {},
             "started_at": "2025-01-15T03:00:00Z", "completed_at": "2025-01-15T04:00:00Z"}]
    gen = NightlyReportGenerator()
    report = gen.generate_daily_report(runs, "2025-01-15")

    assert "今日无 Nightly 构建失败" in report


def test_generate_filename():
    gen = NightlyReportGenerator()
    assert gen.generate_filename("2025-01-15") == "nightly-daily-2025-01-15.md"


def test_render_bar():
    gen = NightlyReportGenerator()
    bar = gen._render_bar(80)
    assert "█" in bar
    assert "░" in bar
    assert len(bar) == 10


def test_calc_avg_duration():
    gen = NightlyReportGenerator()
    avg = gen._calc_avg_duration(MOCK_NIGHTLY_RUNS)
    assert avg > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])