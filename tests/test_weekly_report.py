"""Weekly Report 测试。"""
import pytest
from scripts.report.weekly_report import WeeklyReportGenerator


MOCK_WEEKLY_RUNS = [
    {
        "id": 2001,
        "name": "Weekly-Smoke-A3",
        "conclusion": "failure",
        "started_at": "2025-01-13T03:00:00Z",
        "completed_at": "2025-01-13T06:00:00Z",
        "classification": {
            "classification": "infrastructure",
            "confidence": "medium",
            "category_detail": "NPU 不可用"
        }
    },
    {
        "id": 2002,
        "name": "Weekly-Smoke-A2",
        "conclusion": "success",
        "started_at": "2025-01-13T03:00:00Z",
        "completed_at": "2025-01-13T04:00:00Z",
        "classification": {}
    }
]


def test_generate_weekly_report():
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(MOCK_WEEKLY_RUNS, "2025-01-13", "2025-01-19")

    assert "---" in report
    assert "Weekly 构建报告" in report
    assert "2025-01-13" in report


def test_report_frontmatter():
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(MOCK_WEEKLY_RUNS, "2025-01-13", "2025-01-19")

    assert "report_type: weekly_summary" in report
    assert "health_score" in report


def test_health_score_section():
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(MOCK_WEEKLY_RUNS, "2025-01-13", "2025-01-19")

    assert "健康度评分" in report
    assert "成功率" in report
    assert "稳定性" in report


def test_failure_details():
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(MOCK_WEEKLY_RUNS, "2025-01-13", "2025-01-19")

    assert "失败详情" in report
    assert "基础设施问题" in report


def test_regression_tracking():
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(MOCK_WEEKLY_RUNS, "2025-01-13", "2025-01-19")

    assert "回归追踪" in report


def test_no_failures():
    runs = [{"id": 1, "name": "Weekly-Smoke", "conclusion": "success", "classification": {},
             "started_at": "2025-01-13T03:00:00Z", "completed_at": "2025-01-13T04:00:00Z"}]
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(runs, "2025-01-13", "2025-01-19")

    assert "本周无 Weekly 构建失败" in report


def test_generate_filename():
    gen = WeeklyReportGenerator()
    assert gen.generate_filename("2025-01-13") == "weekly-summary-2025-01-13.md"


def test_health_rating():
    gen = WeeklyReportGenerator()
    assert gen._get_health_rating(95)["rating"] == "优秀"
    assert gen._get_health_rating(85)["rating"] == "良好"
    assert gen._get_health_rating(75)["rating"] == "一般"
    assert gen._get_health_rating(55)["rating"] == "危险"


def test_calc_health_score():
    gen = WeeklyReportGenerator()
    score = gen._calc_health_score(100, {}, 10, 3600)
    assert score > 80

    score_low = gen._calc_health_score(20, {"infrastructure": 5}, 2, 7200)
    assert score_low < 60


def test_recommendations():
    gen = WeeklyReportGenerator()
    report = gen.generate_weekly_report(MOCK_WEEKLY_RUNS, "2025-01-13", "2025-01-19")
    assert "改进建议" in report


if __name__ == "__main__":
    pytest.main([__file__, "-v"])