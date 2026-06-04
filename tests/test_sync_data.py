"""sync_data module tests."""
import json
import tempfile
from pathlib import Path
from scripts.monitor.aggregator import BuildAggregator


class TestSyncDataLogic:
    def test_pipeline_detection_preserved(self):
        from scripts.monitor.pipeline_detector import PipelineDetector
        config = {
            "nightly": {"name_patterns": ["Nightly-*", "*_nightly_*"]},
            "weekly": {"name_patterns": ["Weekly-*", "*_weekly_*"]},
        }
        detector = PipelineDetector(config)
        run = {"name": "Nightly-A2", "event": "schedule", "head_branch": "main", "pull_requests": []}
        results = detector.detect_all([run])
        assert results[0]["pipeline_info"]["pipeline_type"] == "nightly"

    def test_hardware_label_extraction(self):
        from scripts.monitor.sync_data import extract_hardware_label
        assert extract_hardware_label("Nightly-A2") == "A2"
        assert extract_hardware_label("Nightly-A3") == "A3"
        assert extract_hardware_label("Weekly-A3") == "A3"
        assert extract_hardware_label("E2E-Light") == ""
        assert extract_hardware_label("vLLM Main Schedule Test") == ""

    def test_sync_workflow_run_to_db(self):
        db_path = tempfile.mktemp(suffix=".db")
        agg = BuildAggregator(db_path=db_path)
        run = {
            "id": 99999, "name": "Nightly-A2", "workflow_id": 100,
            "conclusion": "failure", "status": "completed", "event": "schedule",
            "head_branch": "main", "head_sha": "abc", "triggering_actor": {"login": "bot"},
            "html_url": "https://github.com/test", "run_started_at": "2026-06-01T00:00:00Z",
            "completed_at": "2026-06-01T10:00:00Z", "created_at": "2026-06-01T00:00:00Z",
            "updated_at": "2026-06-01T10:00:00Z",
        }
        agg.record_workflow_run(run, pipeline_type="nightly", hardware_label="A2")
        conn = agg._get_conn()
        row = conn.execute("SELECT conclusion, pipeline_type, hardware_label FROM workflow_runs WHERE id=99999").fetchone()
        assert row[0] == "failure"
        assert row[1] == "nightly"
        assert row[2] == "A2"
        conn.close()
        agg.close()
        Path(db_path).unlink(missing_ok=True)

    def test_sync_job_to_db(self):
        db_path = tempfile.mktemp(suffix=".db")
        agg = BuildAggregator(db_path=db_path)
        agg.record_workflow_run({"id": 99999, "name": "Nightly-A2", "workflow_id": 100, "conclusion": "failure", "status": "completed", "event": "schedule", "head_branch": "main", "head_sha": "abc", "triggering_actor": {"login": "bot"}, "html_url": "...", "run_started_at": "2026-06-01T00:00:00Z", "completed_at": "2026-06-01T10:00:00Z", "created_at": "2026-06-01T00:00:00Z", "updated_at": "2026-06-01T10:00:00Z"}, pipeline_type="nightly", hardware_label="A2")
        agg.record_job({"id": 100001, "workflow_run_id": 99999, "workflow_name": "Nightly-A2", "job_name": "Build nightly-a2 image", "conclusion": "success", "status": "completed", "started_at": "2026-06-01T00:00:19Z", "completed_at": "2026-06-01T00:19:47Z", "runner_name": "self-hosted-A2", "runner_group_name": "Default", "steps": [{"name": "Checkout", "conclusion": "success"}, {"name": "Build", "conclusion": "success"}]})
        conn = agg._get_conn()
        row = conn.execute("SELECT job_name, conclusion, steps_count FROM job_records WHERE id=100001").fetchone()
        assert row[0] == "Build nightly-a2 image"
        assert row[1] == "success"
        assert row[2] == 2
        conn.close()
        agg.close()
        Path(db_path).unlink(missing_ok=True)

    def test_success_rate_excludes_cancelled(self):
        db_path = tempfile.mktemp(suffix=".db")
        agg = BuildAggregator(db_path=db_path)
        for i, (concl, hw) in enumerate([
            ("success", "A2"), ("failure", "A2"), ("cancelled", "A3"),
            ("skipped", "A2"), ("timed_out", "A3"),
        ]):
            agg.record_workflow_run({"id": 100+i, "name": f"Test-{i}", "workflow_id": 10, "conclusion": concl, "status": "completed", "event": "schedule", "head_branch": "main", "head_sha": f"sha{i}", "triggering_actor": {"login": "bot"}, "html_url": "...", "run_started_at": "2026-06-01T00:00:00Z", "completed_at": "2026-06-01T10:00:00Z", "created_at": "2026-06-01T00:00:00Z", "updated_at": "2026-06-01T10:00:00Z"}, pipeline_type="nightly", hardware_label=hw)
        conn = agg._get_conn()
        total = conn.execute("SELECT COUNT(*) FROM workflow_runs").fetchone()[0]
        success = conn.execute("SELECT COUNT(*) FROM workflow_runs WHERE conclusion='success'").fetchone()[0]
        failure = conn.execute("SELECT COUNT(*) FROM workflow_runs WHERE conclusion='failure'").fetchone()[0]
        cancelled = conn.execute("SELECT COUNT(*) FROM workflow_runs WHERE conclusion='cancelled'").fetchone()[0]
        assert total == 5
        assert success == 1
        assert failure == 1
        assert cancelled == 1
        rate = success / (success + failure) * 100
        assert rate == 50.0
        conn.close()
        agg.close()
        Path(db_path).unlink(missing_ok=True)