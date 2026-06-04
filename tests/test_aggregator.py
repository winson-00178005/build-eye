"""Build Aggregator 测试。"""
import gc
import pytest
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from scripts.monitor.aggregator import BuildAggregator

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


@pytest.fixture
def aggregator():
    tmp = tempfile.mkdtemp()
    db_path = Path(tmp) / "test_metrics.db"
    agg = BuildAggregator(str(db_path))
    yield agg
    agg.close()
    gc.collect()


def test_init_db(aggregator):
    """测试数据库初始化。"""
    assert aggregator.db_path.exists()


def test_record_build(aggregator):
    """测试记录单次构建。"""
    metadata = {
        "workflow_run": {
            "id": 12345,
            "name": "E2E-Full",
            "conclusion": "failure",
            "started_at": "2025-01-15T10:00:00Z",
            "completed_at": "2025-01-15T12:00:00Z"
        },
        "pipeline_info": {"pipeline_type": "pr"},
        "pr": {"number": 999}
    }
    classification = {
        "classification": "infrastructure",
        "confidence": "high"
    }

    aggregator.record_build(metadata, classification)

    failures = aggregator.get_recent_failures("pr", 5)
    assert len(failures) == 1
    assert failures[0]["classification"] == "infrastructure"


def test_record_builds_batch(aggregator):
    """测试批量记录。"""
    metadata_list = [
        {
            "workflow_run": {"id": 100, "name": "Nightly-A2", "conclusion": "failure",
                             "started_at": "2025-01-15T03:00:00Z", "completed_at": "2025-01-15T05:00:00Z"},
            "pipeline_info": {"pipeline_type": "nightly"},
            "pr": None
        },
        {
            "workflow_run": {"id": 200, "name": "E2E-Light", "conclusion": "failure",
                             "started_at": "2025-01-15T08:00:00Z", "completed_at": "2025-01-15T09:00:00Z"},
            "pipeline_info": {"pipeline_type": "pr"},
            "pr": {"number": 888}
        }
    ]
    classifications = [
        {"workflow_run_id": 100, "classification": {"classification": "infrastructure", "confidence": "high"}},
        {"workflow_run_id": 200, "classification": {"classification": "code", "confidence": "medium"}}
    ]

    aggregator.record_builds_batch(metadata_list, classifications)

    all_failures = aggregator.get_recent_failures(None, 10)
    assert len(all_failures) == 2


def test_update_daily_aggregate(aggregator):
    """测试更新每日聚合。"""
    aggregator.update_daily_aggregate(TODAY, "nightly", "Nightly-A2")

    aggregates = aggregator.get_daily_aggregates("nightly", 7)
    assert len(aggregates) >= 1


def test_get_trend_data(aggregator):
    """测试趋势数据查询。"""
    aggregator.update_daily_aggregate(TODAY, "nightly", "Nightly-A2")

    trend = aggregator.get_trend_data("nightly", 7)
    assert isinstance(trend, list)


def test_consecutive_failures(aggregator):
    """测试连续失败计数。"""
    for i in range(3):
        aggregator.record_build({
            "workflow_run": {"id": 1000 + i, "name": "Nightly-A2", "conclusion": "failure",
                             "started_at": f"2025-01-{15+i}T03:00:00Z", "completed_at": f"2025-01-{15+i}T04:00:00Z"},
            "pipeline_info": {"pipeline_type": "nightly"},
            "pr": None
        }, {"classification": "infrastructure", "confidence": "high"})

    consecutive = aggregator.get_consecutive_failures("nightly")
    assert consecutive >= 1


def test_calc_duration(aggregator):
    """测试时长计算。"""
    dur = aggregator._calc_duration("2025-01-15T10:00:00Z", "2025-01-15T12:00:00Z")
    assert dur == 7200

    dur_empty = aggregator._calc_duration("", "")
    assert dur_empty == 0


def test_calc_health_score(aggregator):
    """测试健康评分计算。"""
    score = aggregator._calc_health_score(8, 10, {"infrastructure": 2})
    assert score > 0
    assert score <= 100

    score_zero = aggregator._calc_health_score(0, 0, {})
    assert score_zero == 0


def test_health_rating(aggregator):
    """测试评级。"""
    assert aggregator.get_health_rating(95)["rating"] == "优秀"
    assert aggregator.get_health_rating(85)["rating"] == "良好"
    assert aggregator.get_health_rating(75)["rating"] == "一般"
    assert aggregator.get_health_rating(65)["rating"] == "较差"
    assert aggregator.get_health_rating(30)["rating"] == "危险"


def test_workflow_runs_table_created(aggregator):
    conn = aggregator._get_conn()
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    table_names = [t[0] for t in tables]
    assert "workflow_runs" in table_names
    assert "job_records" in table_names
    conn.close()


def test_record_workflow_run(aggregator):
    aggregator.record_workflow_run({
        "id": 12345,
        "name": "Nightly-A2",
        "workflow_id": 999,
        "conclusion": "failure",
        "status": "completed",
        "event": "schedule",
        "head_branch": "main",
        "head_sha": "abc123",
        "triggering_actor": {"login": "bot"},
        "html_url": "https://github.com/...",
        "run_started_at": "2026-06-03T03:03:08Z",
        "completed_at": "2026-06-03T06:49:08Z",
        "created_at": "2026-06-03T03:03:08Z",
        "updated_at": "2026-06-03T06:49:08Z",
    }, pipeline_type="nightly", hardware_label="A2")
    conn = aggregator._get_conn()
    row = conn.execute("SELECT conclusion, pipeline_type, hardware_label FROM workflow_runs WHERE id=12345").fetchone()
    assert row[0] == "failure"
    assert row[1] == "nightly"
    assert row[2] == "A2"
    conn.close()


def test_record_job(aggregator):
    aggregator.record_workflow_run({
        "id": 12345, "name": "Nightly-A2", "workflow_id": 999, "conclusion": "failure",
        "status": "completed", "event": "schedule", "head_branch": "main", "head_sha": "abc123",
        "triggering_actor": {"login": "bot"}, "html_url": "...",
        "run_started_at": "2026-06-03T03:03:08Z", "completed_at": "2026-06-03T06:49:08Z",
        "created_at": "2026-06-03T03:03:08Z", "updated_at": "2026-06-03T06:49:08Z",
    }, pipeline_type="nightly", hardware_label="A2")
    aggregator.record_job({
        "id": 100001, "workflow_run_id": 12345, "workflow_name": "Nightly-A2",
        "job_name": "Build nightly-a2 image", "conclusion": "success", "status": "completed",
        "started_at": "2026-06-03T03:03:19Z", "completed_at": "2026-06-03T03:19:47Z",
        "runner_name": "self-hosted-A2", "runner_group_name": "Default",
        "steps": [{"name": "Checkout", "conclusion": "success"}, {"name": "Build", "conclusion": "success"}],
    })
    conn = aggregator._get_conn()
    row = conn.execute("SELECT job_name, conclusion, steps_count FROM job_records WHERE id=100001").fetchone()
    assert row[0] == "Build nightly-a2 image"
    assert row[1] == "success"
    assert row[2] == 2
    conn.close()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])