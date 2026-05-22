"""Dashboard Service 测试。"""
import pytest
from scripts.report.dashboard import DashboardService


MOCK_METADATA = [
    {
        "workflow_run": {"id": 1, "name": "E2E-Full", "conclusion": "failure"},
        "pipeline_info": {"pipeline_type": "pr"},
        "classification": {"classification": "code", "confidence": "high"}
    },
    {
        "workflow_run": {"id": 2, "name": "Nightly-A2", "conclusion": "failure"},
        "pipeline_info": {"pipeline_type": "nightly"},
        "classification": {"classification": "infrastructure", "confidence": "high"}
    },
    {
        "workflow_run": {"id": 3, "name": "Weekly-Smoke", "conclusion": "success"},
        "pipeline_info": {"pipeline_type": "weekly"},
        "classification": {}
    }
]


def test_generate_overview():
    service = DashboardService()
    overview = service.generate_overview(MOCK_METADATA)

    assert overview["summary"]["total_runs"] == 3
    assert overview["summary"]["success_runs"] == 1
    assert overview["summary"]["failure_runs"] == 2
    assert "pr" in overview["pipelines"]
    assert "nightly" in overview["pipelines"]
    assert "weekly" in overview["pipelines"]


def test_generate_overview_no_data():
    service = DashboardService()
    overview = service.generate_overview()

    assert overview["summary"]["total_runs"] == 0


def test_generate_categories():
    service = DashboardService()
    categories = service.generate_categories(MOCK_METADATA)

    assert "code" in categories["distribution"]
    assert "infrastructure" in categories["distribution"]
    assert "pr" in categories["by_pipeline_type"]


def test_generate_categories_no_data():
    service = DashboardService()
    categories = service.generate_categories()

    assert categories["distribution"] == {}


def test_generate_full_dashboard():
    service = DashboardService()
    dashboard = service.generate_full_dashboard(MOCK_METADATA)

    assert "overview" in dashboard
    assert "trends" in dashboard
    assert "categories" in dashboard
    assert "recent_failures" in dashboard
    assert "health_scores" in dashboard


def test_save_dashboard():
    import tempfile
    from pathlib import Path

    service = DashboardService()
    dashboard = service.generate_full_dashboard(MOCK_METADATA)

    with tempfile.TemporaryDirectory() as tmp:
        output_path = Path(tmp) / "dashboard.json"
        service.save_dashboard(dashboard, output_path)

        assert output_path.exists()

        import json
        data = json.loads(output_path.read_text(encoding="utf-8"))
        assert "overview" in data


if __name__ == "__main__":
    pytest.main([__file__, "-v"])