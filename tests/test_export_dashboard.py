"""export_dashboard module tests."""
import json
import tempfile
from pathlib import Path
from scripts.monitor.aggregator import BuildAggregator
from scripts.report.export_dashboard import export_dashboard_json


class TestExportDashboard:
    def setup_method(self):
        self.db_path = tempfile.mktemp(suffix=".db")
        self.agg = BuildAggregator(db_path=self.db_path)
        for i, (concl, ptype, hw) in enumerate([
            ("success", "nightly", "A2"), ("failure", "nightly", "A2"),
            ("cancelled", "nightly", "A3"), ("success", "pr", ""),
            ("failure", "weekly", "A3"),
        ]):
            self.agg.record_workflow_run({"id": 100+i, "name": f"WF-{i}", "workflow_id": 10, "conclusion": concl, "status": "completed", "event": "schedule", "head_branch": "main", "head_sha": f"sha{i}", "triggering_actor": {"login": "bot"}, "html_url": "...", "run_started_at": "2026-06-01T00:00:00Z", "completed_at": "2026-06-01T10:00:00Z", "created_at": "2026-06-01T00:00:00Z", "updated_at": "2026-06-01T10:00:00Z"}, pipeline_type=ptype, hardware_label=hw)
            for j in range(2):
                self.agg.record_job({"id": 200+i*10+j, "workflow_run_id": 100+i, "workflow_name": f"WF-{i}", "job_name": f"Job-{i}-{j}", "conclusion": concl if j==0 else "success", "status": "completed", "started_at": "2026-06-01T00:00:00Z", "completed_at": "2026-06-01T00:30:00Z", "runner_name": "runner", "runner_group_name": "Default", "steps": []})

    def teardown_method(self):
        self.agg.close()
        Path(self.db_path).unlink(missing_ok=True)

    def test_export_all_range(self):
        output = tempfile.mktemp(suffix=".json")
        export_dashboard_json(self.db_path, output, range_type="all")
        data = json.loads(Path(output).read_text(encoding="utf-8"))
        assert data["meta"]["time_range"] == "all"
        assert data["workflow_overview"]["total_runs"] >= 1
        assert "success_runs" in data["workflow_overview"]
        assert "cancelled_runs" in data["workflow_overview"]
        assert "job_overview" in data
        assert "workflow_runs" in data
        assert "job_stats" in data
        Path(output).unlink(missing_ok=True)

    def test_success_rate_calculation(self):
        output = tempfile.mktemp(suffix=".json")
        export_dashboard_json(self.db_path, output, range_type="all")
        data = json.loads(Path(output).read_text(encoding="utf-8"))
        wo = data["workflow_overview"]
        assert wo["success_runs"] == 2
        assert wo["failure_runs"] == 2
        assert wo["cancelled_runs"] == 1
        rate = wo["success_runs"] / (wo["success_runs"] + wo["failure_runs"]) * 100
        assert round(rate, 1) == 50.0
        Path(output).unlink(missing_ok=True)

    def test_custom_range(self):
        output = tempfile.mktemp(suffix=".json")
        export_dashboard_json(self.db_path, output, range_type="custom", start_date="2026-05-01", end_date="2026-06-30")
        data = json.loads(Path(output).read_text(encoding="utf-8"))
        assert data["meta"]["time_range"] == "custom"
        assert data["meta"]["start_date"] == "2026-05-01"
        assert data["meta"]["end_date"] == "2026-06-30"
        Path(output).unlink(missing_ok=True)

    def test_job_stats_present(self):
        output = tempfile.mktemp(suffix=".json")
        export_dashboard_json(self.db_path, output, range_type="all")
        data = json.loads(Path(output).read_text(encoding="utf-8"))
        assert len(data["job_stats"]) > 0
        for stat in data["job_stats"]:
            assert "workflow_name" in stat
            assert "job_name" in stat
            assert "total_runs" in stat
            assert "success_rate" in stat
        Path(output).unlink(missing_ok=True)

    def test_pipelines_breakdown(self):
        output = tempfile.mktemp(suffix=".json")
        export_dashboard_json(self.db_path, output, range_type="all")
        data = json.loads(Path(output).read_text(encoding="utf-8"))
        pipelines = data["workflow_overview"]["pipelines"]
        assert "nightly" in pipelines
        assert "weekly" in pipelines
        assert "pr" in pipelines
        assert pipelines["nightly"]["total_runs"] >= 2
        Path(output).unlink(missing_ok=True)