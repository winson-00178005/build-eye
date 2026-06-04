# Build-Eye Dashboard 重设计 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Redesign Build-Eye dashboard to support Job-level statistics, full-history data storage, and multi-page navigation, matching the external vLLM Ascend Dashboard's data granularity.

**Architecture:** SQLite stores full-history workflow_runs and job_records. A new sync_data.py script incrementally fetches all workflows (no whitelist/event/pagination limits) from GitHub API and stores in SQLite. An export_dashboard.py script queries SQLite and exports 3 time-range JSON files + custom range. Frontend index.html is rebuilt with multi-page navigation (Workflow, Job, Categories, Health, Settings).

**Tech Stack:** Python 3.11, SQLite (WAL mode), GitHub REST API, vanilla HTML/JS/CSS, GitHub Pages deployment

---

### Task 1: Add workflow_runs and job_records tables to SQLite

**Files:**
- Modify: `scripts/monitor/aggregator.py`
- Test: `tests/test_aggregator.py`

**Step 1: Write the failing test**

Add test methods to `tests/test_aggregator.py` for the new tables:

```python
def test_workflow_runs_table_created(self):
    agg = BuildAggregator(db_path=self.db_path)
    conn = agg._get_conn()
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    table_names = [t[0] for t in tables]
    assert "workflow_runs" in table_names
    assert "job_records" in table_names
    conn.close()
    agg.close()

def test_record_workflow_run(self):
    agg = BuildAggregator(db_path=self.db_path)
    agg.record_workflow_run({
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
    conn = agg._get_conn()
    row = conn.execute("SELECT * FROM workflow_runs WHERE id=12345").fetchone()
    assert row is not None
    conn.close()
    agg.close()

def test_record_job(self):
    agg = BuildAggregator(db_path=self.db_path)
    agg.record_workflow_run({"id": 12345, "name": "Nightly-A2", "workflow_id": 999, "conclusion": "failure", "status": "completed", "event": "schedule", "head_branch": "main", "head_sha": "abc123", "triggering_actor": {"login": "bot"}, "html_url": "...", "run_started_at": "2026-06-03T03:03:08Z", "completed_at": "2026-06-03T06:49:08Z", "created_at": "2026-06-03T03:03:08Z", "updated_at": "2026-06-03T06:49:08Z"}, pipeline_type="nightly", hardware_label="A2")
    agg.record_job({
        "id": 100001,
        "workflow_run_id": 12345,
        "workflow_name": "Nightly-A2",
        "job_name": "Build nightly-a2 image",
        "conclusion": "success",
        "status": "completed",
        "started_at": "2026-06-03T03:03:19Z",
        "completed_at": "2026-06-03T03:19:47Z",
        "runner_name": "self-hosted-A2",
        "runner_group_name": "Default",
        "steps_count": 3,
        "failed_step_name": None,
    })
    conn = agg._get_conn()
    row = conn.execute("SELECT * FROM job_records WHERE id=100001").fetchone()
    assert row is not None
    conn.close()
    agg.close()
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_aggregator.py::TestBuildAggregator::test_workflow_runs_table_created tests/test_aggregator.py::TestBuildAggregator::test_record_workflow_run tests/test_aggregator.py::TestBuildAggregator::test_record_job -v`
Expected: FAIL — tables and methods don't exist yet

**Step 3: Add tables and methods to aggregator.py**

In `scripts/monitor/aggregator.py`, add to `_init_db()`:
```python
conn.execute("""
    CREATE TABLE IF NOT EXISTS workflow_runs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        workflow_id INTEGER,
        conclusion TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'completed',
        event TEXT,
        head_branch TEXT,
        head_sha TEXT,
        triggering_actor TEXT DEFAULT 'unknown',
        html_url TEXT,
        started_at TEXT,
        completed_at TEXT,
        duration_seconds REAL,
        pipeline_type TEXT,
        hardware_label TEXT,
        created_at TEXT,
        updated_at TEXT
    )
""")
conn.execute("""
    CREATE TABLE IF NOT EXISTS job_records (
        id INTEGER PRIMARY KEY,
        workflow_run_id INTEGER NOT NULL,
        workflow_name TEXT NOT NULL,
        job_name TEXT NOT NULL,
        conclusion TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'completed',
        started_at TEXT,
        completed_at TEXT,
        duration_seconds REAL,
        runner_name TEXT,
        runner_group_name TEXT,
        steps_count INTEGER DEFAULT 0,
        failed_step_name TEXT,
        hardware_label TEXT,
        FOREIGN KEY (workflow_run_id) REFERENCES workflow_runs(id)
    )
""")
for idx_sql in [
    "CREATE INDEX IF NOT EXISTS idx_job_workflow_run ON job_records(workflow_run_id)",
    "CREATE INDEX IF NOT EXISTS idx_job_workflow_name ON job_records(workflow_name)",
    "CREATE INDEX IF NOT EXISTS idx_job_conclusion ON job_records(conclusion)",
    "CREATE INDEX IF NOT EXISTS idx_workflow_conclusion ON workflow_runs(conclusion)",
    "CREATE INDEX IF NOT EXISTS idx_workflow_pipeline ON workflow_runs(pipeline_type)",
    "CREATE INDEX IF NOT EXISTS idx_workflow_created ON workflow_runs(created_at)",
    "CREATE INDEX IF NOT EXISTS idx_workflow_name ON workflow_runs(name)",
]:
    conn.execute(idx_sql)
```

Add `record_workflow_run()` and `record_job()` methods:
```python
def record_workflow_run(self, run: Dict[str, Any], pipeline_type: str = "", hardware_label: str = "") -> None:
    self._ensure_open()
    run_id = run.get("id")
    started_at = run.get("run_started_at", run.get("started_at"))
    completed_at = run.get("completed_at")
    duration = self._calc_duration(started_at, completed_at) if started_at and completed_at else 0
    actor = (run.get("triggering_actor") or {}).get("login", "unknown")
    conn = self._get_conn()
    try:
        conn.execute("""
            INSERT OR REPLACE INTO workflow_runs
            (id, name, workflow_id, conclusion, status, event, head_branch, head_sha,
             triggering_actor, html_url, started_at, completed_at, duration_seconds,
             pipeline_type, hardware_label, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            run_id, run.get("name", ""), run.get("workflow_id"), run.get("conclusion", ""),
            run.get("status", "completed"), run.get("event"), run.get("head_branch", ""),
            run.get("head_sha", ""), actor, run.get("html_url", ""),
            started_at, completed_at, duration,
            pipeline_type, hardware_label,
            run.get("created_at"), run.get("updated_at")
        ))
        conn.commit()
    finally:
        conn.close()

def record_job(self, job: Dict[str, Any]) -> None:
    self._ensure_open()
    job_id = job.get("id")
    started_at = job.get("started_at")
    completed_at = job.get("completed_at")
    duration = self._calc_duration(started_at, completed_at) if started_at and completed_at else 0
    steps = job.get("steps", [])
    failed_step = None
    for step in steps:
        if step.get("conclusion") == "failure":
            failed_step = step.get("name")
            break
    conn = self._get_conn()
    try:
        conn.execute("""
            INSERT OR REPLACE INTO job_records
            (id, workflow_run_id, workflow_name, job_name, conclusion, status,
             started_at, completed_at, duration_seconds, runner_name, runner_group_name,
             steps_count, failed_step_name, hardware_label)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job_id, job.get("workflow_run_id"), job.get("workflow_name", ""),
            job.get("job_name", job.get("name", "")), job.get("conclusion", ""),
            job.get("status", "completed"), started_at, completed_at, duration,
            job.get("runner_name", ""), job.get("runner_group_name", ""),
            len(steps), failed_step, job.get("hardware_label", "")
        ))
        conn.commit()
    finally:
        conn.close()
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_aggregator.py::TestBuildAggregator::test_workflow_runs_table_created tests/test_aggregator.py::TestBuildAggregator::test_record_workflow_run tests/test_aggregator.py::TestBuildAggregator::test_record_job -v`
Expected: PASS

**Step 5: Commit**

```bash
git add scripts/monitor/aggregator.py tests/test_aggregator.py
git commit -m "feat: add workflow_runs and job_records tables to SQLite"
```

---

### Task 2: Create sync_data.py — full/incremental GitHub data sync

**Files:**
- Create: `scripts/monitor/sync_data.py`
- Test: `tests/test_sync_data.py`

**Step 1: Write the failing test**

Create `tests/test_sync_data.py`:
```python
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
        agg = BuildAggregator(db_path=tempfile.mktemp(suffix=".db"))
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

    def test_sync_job_to_db(self):
        agg = BuildAggregator(db_path=tempfile.mktemp(suffix=".db"))
        agg.record_workflow_run({"id": 99999, "name": "Nightly-A2", "workflow_id": 100, "conclusion": "failure", "status": "completed", "event": "schedule", "head_branch": "main", "head_sha": "abc", "triggering_actor": {"login": "bot"}, "html_url": "...", "run_started_at": "2026-06-01T00:00:00Z", "completed_at": "2026-06-01T10:00:00Z", "created_at": "2026-06-01T00:00:00Z", "updated_at": "2026-06-01T10:00:00Z"}, pipeline_type="nightly", hardware_label="A2")
        agg.record_job({"id": 100001, "workflow_run_id": 99999, "workflow_name": "Nightly-A2", "job_name": "Build nightly-a2 image", "conclusion": "success", "status": "completed", "started_at": "2026-06-01T00:00:19Z", "completed_at": "2026-06-01T00:19:47Z", "runner_name": "self-hosted-A2", "runner_group_name": "Default", "steps": [{"name": "Checkout", "conclusion": "success"}, {"name": "Build", "conclusion": "success"}]})
        conn = agg._get_conn()
        row = conn.execute("SELECT job_name, conclusion, steps_count FROM job_records WHERE id=100001").fetchone()
        assert row[0] == "Build nightly-a2 image"
        assert row[1] == "success"
        assert row[2] == 2
        conn.close()
        agg.close()

    def test_success_rate_excludes_cancelled(self):
        agg = BuildAggregator(db_path=tempfile.mktemp(suffix=".db"))
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
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_sync_data.py -v`
Expected: FAIL — `sync_data.py` and `extract_hardware_label` don't exist

**Step 3: Create sync_data.py**

Create `scripts/monitor/sync_data.py`:
```python
"""Build-Eye 数据同步 - 从 GitHub API 全量/增量同步 workflow runs + jobs 到 SQLite。"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

from monitor.github_client import GitHubAPIClient
from monitor.aggregator import BuildAggregator
from monitor.pipeline_detector import PipelineDetector
from monitor.config_loader import config


def extract_hardware_label(name: str) -> str:
    match = re.search(r"[-_](A[23])", name)
    return match.group(1) if match else ""


def sync_runs_and_jobs(
    client: GitHubAPIClient,
    owner: str,
    repo: str,
    aggregator: BuildAggregator,
    detector: PipelineDetector,
    full_sync: bool = False,
    lookback_hours: int = None,
) -> dict:
    if full_sync or lookback_hours:
        cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours or 999999)
        created_filter = f">={cutoff.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    else:
        conn = aggregator._get_conn()
        try:
            last_sync = conn.execute("SELECT MAX(updated_at) FROM workflow_runs").fetchone()[0]
        finally:
            conn.close()
        if last_sync:
            created_filter = f">={last_sync}"
        else:
            cutoff = datetime.now(timezone.utc) - timedelta(hours=999999)
            created_filter = f">={cutoff.strftime('%Y-%m-%dT%H:%M:%SZ')}"

    runs = client.get_workflow_runs(
        owner=owner, repo=repo,
        status="completed",
        created=created_filter,
        per_page=100,
        max_pages=100
    )

    print(f"Fetched {len(runs)} workflow runs")

    new_runs = 0
    new_jobs = 0

    for run in runs:
        run_id = run.get("id")
        enriched = detector.detect_all([dict(run)])
        ptype = enriched[0].get("pipeline_info", {}).get("pipeline_type", "unknown")
        if ptype == "unmonitored":
            ptype = "other"
        hw = extract_hardware_label(run.get("name", ""))
        aggregator.record_workflow_run(run, pipeline_type=ptype, hardware_label=hw)
        new_runs += 1

        jobs = client.get_workflow_run_jobs(owner, repo, run_id)
        if jobs:
            wf_name = run.get("name", "")
            for job in jobs:
                job["workflow_run_id"] = run_id
                job["workflow_name"] = wf_name
                job["hardware_label"] = hw or extract_hardware_label(job.get("runner_name", ""))
                aggregator.record_job(job)
                new_jobs += 1

    print(f"Synced {new_runs} workflow runs, {new_jobs} jobs")
    return {"workflow_runs": new_runs, "jobs": new_jobs}


def main():
    parser = argparse.ArgumentParser(description="Sync GitHub workflow runs and jobs to SQLite")
    parser.add_argument("--db", default="data/build_metrics.db", help="SQLite database path")
    parser.add_argument("--full-sync", action="store_true", help="Full sync (no time window)")
    parser.add_argument("--lookback", type=int, default=None, help="Lookback hours for partial sync")
    parser.add_argument("--timeout", type=int, default=30, help="API timeout")
    args = parser.parse_args()

    client = GitHubAPIClient(timeout=args.timeout)
    target = config.target_repo
    owner = target["owner"]
    repo = target["repo"]

    aggregator = BuildAggregator(db_path=args.db)
    detector = PipelineDetector(config.pipeline_types)

    result = sync_runs_and_jobs(
        client, owner, repo, aggregator, detector,
        full_sync=args.full_sync,
        lookback_hours=args.lookback
    )

    aggregator.close()
    print(f"Sync complete: {result}")


if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_sync_data.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add scripts/monitor/sync_data.py tests/test_sync_data.py
git commit -m "feat: add sync_data.py for full/incremental GitHub data sync"
```

---

### Task 3: Run full data sync

**Step 1: Run the full sync**

Run: `python scripts/monitor/sync_data.py --db data/build_metrics.db --full-sync --timeout 60`
Expected: Fetches all workflow runs and jobs from vllm-project/vllm-ascend, stores in SQLite.

Note: This requires `GITHUB_TOKEN` or `VLLM_ASCEND_TOKEN` env var to be set for API access.

**Step 2: Verify data in SQLite**

Run: `python -c "from scripts.monitor.aggregator import BuildAggregator; a=BuildAggregator('data/build_metrics.db'); c=a._get_conn(); print('workflow_runs:', c.execute('SELECT COUNT(*) FROM workflow_runs').fetchone()); print('job_records:', c.execute('SELECT COUNT(*) FROM job_records').fetchone()); print('conclusions:', c.execute('SELECT conclusion, COUNT(*) FROM workflow_runs GROUP BY conclusion').fetchall()); c.close(); a.close()"`

**Step 3: Commit database**

```bash
git add data/build_metrics.db
git commit -m "data: full sync of workflow runs and jobs to SQLite"
```

---

### Task 4: Create export_dashboard.py — multi-range JSON export

**Files:**
- Create: `scripts/report/export_dashboard.py`
- Test: `tests/test_export_dashboard.py`

**Step 1: Write the failing test**

Create `tests/test_export_dashboard.py`:
```python
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
```

**Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_export_dashboard.py -v`
Expected: FAIL — `export_dashboard.py` doesn't exist

**Step 3: Create export_dashboard.py**

Create `scripts/report/export_dashboard.py` with the full multi-range export logic. Key structure:

```python
"""Build-Eye Dashboard JSON Export — 从 SQLite 导出多维时间范围的 dashboard JSON 文件。"""
import argparse
import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any


def _query_overview(conn, date_filter: str = None) -> Dict[str, Any]:
    base_where = "1=1"
    if date_filter:
        base_where += f" AND created_at {date_filter}"
    total = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base_where}").fetchone()[0]
    success = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base_where} AND conclusion='success'").fetchone()[0]
    failure = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base_where} AND conclusion='failure'").fetchone()[0]
    cancelled = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base_where} AND conclusion='cancelled'").fetchone()[0]
    skipped = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base_where} AND conclusion='skipped'").fetchone()[0]
    timed_out = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base_where} AND conclusion='timed_out'").fetchone()[0]
    success_rate = round(success / max(success + failure, 1) * 100, 1)
    avg_dur = conn.execute(f"SELECT AVG(duration_seconds) FROM workflow_runs WHERE {base_where} AND duration_seconds > 0").fetchone()[0] or 0
    avg_dur_min = round(avg_dur / 60, 1)
    # ... pipeline breakdown, job overview similarly
    return {
        "total_runs": total, "success_runs": success, "failure_runs": failure,
        "cancelled_runs": cancelled, "skipped_runs": skipped, "timed_out_runs": timed_out,
        "success_rate": success_rate, "avg_duration_minutes": avg_dur_min,
        "pipelines": _query_pipelines(conn, date_filter),
    }

def _query_pipelines(conn, date_filter: str = None) -> Dict[str, Any]:
    pipelines = {}
    for ptype in ["nightly", "weekly", "pr", "other"]:
        base = f"pipeline_type='{ptype}'"
        if date_filter:
            base += f" AND created_at {date_filter}"
        t = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base}").fetchone()[0]
        s = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base} AND conclusion='success'").fetchone()[0]
        f = conn.execute(f"SELECT COUNT(*) FROM workflow_runs WHERE {base} AND conclusion='failure'").fetchone()[0]
        pipelines[ptype] = {
            "total_runs": t, "success_runs": s, "failure_runs": f,
            "success_rate": round(s / max(s + f, 1) * 100, 1),
        }
    return pipelines

def _query_job_overview(conn, date_filter: str = None) -> Dict[str, Any]:
    base_where = "1=1"
    if date_filter:
        base_where = f"workflow_run_id IN (SELECT id FROM workflow_runs WHERE created_at {date_filter})"
    total = conn.execute(f"SELECT COUNT(*) FROM job_records WHERE {base_where}").fetchone()[0]
    success = conn.execute(f"SELECT COUNT(*) FROM job_records WHERE {base_where} AND conclusion='success'").fetchone()[0]
    failure = conn.execute(f"SELECT COUNT(*) FROM job_records WHERE {base_where} AND conclusion='failure'").fetchone()[0]
    cancelled = conn.execute(f"SELECT COUNT(*) FROM job_records WHERE {base_where} AND conclusion='cancelled'").fetchone()[0]
    # ... similar pattern
    return { ... }

def _query_job_stats(conn, date_filter: str = None) -> list:
    base_where = "1=1"
    if date_filter:
        base_where = f"workflow_run_id IN (SELECT id FROM workflow_runs WHERE created_at {date_filter})"
    rows = conn.execute(f"""
        SELECT workflow_name, job_name,
               COUNT(*) as total_runs,
               SUM(CASE WHEN conclusion='success' THEN 1 ELSE 0 END) as success_runs,
               SUM(CASE WHEN conclusion='failure' THEN 1 ELSE 0 END) as failure_runs,
               SUM(CASE WHEN conclusion='cancelled' THEN 1 ELSE 0 END) as cancelled_runs,
               ROUND(SUM(CASE WHEN conclusion='success' THEN 1 ELSE 0 END) * 100.0 / MAX(SUM(CASE WHEN conclusion IN ('success','failure') THEN 1 ELSE 0 END), 1), 1) as success_rate,
               ROUND(AVG(CASE WHEN duration_seconds > 0 THEN duration_seconds / 60 ELSE NULL END), 1) as avg_duration_min,
               ROUND(MIN(CASE WHEN duration_seconds > 0 THEN duration_seconds / 60 ELSE NULL END), 1) as min_duration_min,
               ROUND(MAX(CASE WHEN duration_seconds > 0 THEN duration_seconds / 60 ELSE NULL END), 1) as max_duration_min,
               MAX(started_at) as last_run_at,
               ... last_conclusion
        FROM job_records WHERE {base_where}
        GROUP BY workflow_name, job_name
        ORDER BY workflow_name, job_name
    """).fetchall()
    return [dict(zip([...column names...], row)) for row in rows]

def _query_workflow_runs(conn, date_filter: str = None) -> list:
    # ... similar, includes job_count per run via subquery

def _query_trends(conn) -> Dict:
    # Daily success rate and failure count trends for last 30 days

def _build_date_filter(range_type: str, start_date: str = None, end_date: str = None) -> str | None:
    if range_type == "all":
        return None
    elif range_type == "7d":
        cutoff = (datetime.now(timezone.utc) - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')
        return f">='{cutoff}'"
    elif range_type == "30d":
        cutoff = (datetime.now(timezone.utc) - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
        return f">='{cutoff}'"
    elif range_type == "custom" and start_date and end_date:
        return f">='{start_date}T00:00:00Z' AND created_at <= '{end_date}T23:59:59Z'"
    return None


def export_dashboard_json(db_path: str, output_path: str, range_type: str = "all", start_date: str = None, end_date: str = None) -> dict:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    date_filter = _build_date_filter(range_type, start_date, end_date)

    data = {
        "meta": {
            "time_range": range_type,
            "start_date": start_date or "",
            "end_date": end_date or "",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_workflows": conn.execute("SELECT COUNT(*) FROM workflow_runs").fetchone()[0],
            "total_jobs": conn.execute("SELECT COUNT(*) FROM job_records").fetchone()[0],
        },
        "workflow_overview": _query_overview(conn, date_filter),
        "job_overview": _query_job_overview(conn, date_filter),
        "workflow_runs": _query_workflow_runs(conn, date_filter),
        "job_stats": _query_job_stats(conn, date_filter),
        "categories": {},  # filled from classification data
        "health_scores": {"scores": []},
        "trends": _query_trends(conn),
        "notification_settings": {},  # filled from env vars
    }
    conn.close()

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return data


def main():
    parser = argparse.ArgumentParser(description="Export dashboard JSON from SQLite")
    parser.add_argument("--db", default="data/build_metrics.db")
    parser.add_argument("--output", required=True)
    parser.add_argument("--range", choices=["all", "7d", "30d", "custom"], default="all")
    parser.add_argument("--start-date", help="Start date (YYYY-MM-DD) for custom range")
    parser.add_argument("--end-date", help="End date (YYYY-MM-DD) for custom range")
    args = parser.parse_args()

    export_dashboard_json(args.db, args.output, args.range, args.start_date, args.end_date)
    print(f"Exported {args.range} range to {args.output}")


if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `python -m pytest tests/test_export_dashboard.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add scripts/report/export_dashboard.py tests/test_export_dashboard.py
git commit -m "feat: add export_dashboard.py for multi-range JSON export"
```

---

### Task 5: Rebuild frontend index.html — multi-page navigation

**Files:**
- Modify: `dashboard/index.html` (full rewrite)

This task replaces the current single-page dashboard with a multi-page navigation layout. The new index.html contains:

- Left sidebar navigation: Workflow看板, Job看板, 分类统计, 健康评分, 设置
- Top bar with time range selector (全历史/7天/30天/自定义)
- Each "page" is a div that shows/hides based on nav selection
- Data is loaded from the appropriate JSON file (dashboard_all.json, dashboard_7d.json, dashboard_30d.json)
- Custom time range loads dashboard_custom.json (or shows message to generate)

Key UI components per page:

**Workflow看板**:
- 4 stat cards: total_runs, success_rate, avg_duration, recent_runs_count
- Each card shows all-time and range-specific values
- Pipeline breakdown table (nightly/weekly/pr)
- Workflow runs table with filters (workflow name, conclusion, hardware)

**Job看板**:
- 4 stat cards: total_jobs, job_success_rate, avg_job_duration, job_failure_count
- Job stats table (grouped by workflow_name + job_name) with filters
- Columns: Workflow | Job名称 | 总运行 | 成功/失败 | 成功率 | 平均时长 | 最近运行

**分类统计**:
- Failure classification distribution (code/infrastructure/interference)
- Category pie chart or bar chart (CSS-based)

**健康评分**:
- Health score cards per pipeline type
- Trend chart (CSS-based sparklines)

**设置**:
- Email notification settings only (feishu/dingtalk removed)

Since this is a large single-file rewrite, implement directly rather than TDD.

**Step 1: Rewrite dashboard/index.html**

Write the complete new index.html with all pages, navigation, and data loading logic.

**Step 2: Verify in browser**

Open `dashboard/index.html` locally and verify navigation works and all pages render.

**Step 3: Commit**

```bash
git add dashboard/index.html
git commit -m "feat: rebuild dashboard with multi-page navigation and job-level stats"
```

---

### Task 6: Update deploy-dashboard.yml workflow

**Files:**
- Modify: `.github/workflows/deploy-dashboard.yml`

**Step 1: Update workflow steps**

Replace the current dashboard_data_generator.py step with:
1. `sync_data.py --db data/build_metrics.db --lookback 168` (incremental sync)
2. `export_dashboard.py` for all three ranges + optional custom range
3. Remove notification settings from env vars (already done)
4. Keep GitHub Pages deployment step

**Step 2: Add workflow_dispatch inputs for custom range**

Add `start_date` and `end_date` inputs to workflow_dispatch trigger.

**Step 3: Commit**

```bash
git add .github/workflows/deploy-dashboard.yml
git commit -m "feat: update deploy-dashboard workflow with sync+export pipeline"
```

---

### Task 7: Generate initial dashboard JSON files and verify end-to-end

**Step 1: Export all three range JSON files**

```bash
python scripts/report/export_dashboard.py --db data/build_metrics.db --range all --output dashboard/dashboard_all.json
python scripts/report/export_dashboard.py --db data/build_metrics.db --range 7d --output dashboard/dashboard_7d.json
python scripts/report/export_dashboard.py --db data/build_metrics.db --range 30d --output dashboard/dashboard_30d.json
```

**Step 2: Verify JSON content**

Check that each JSON contains:
- workflow_overview with success_rate, cancelled_runs, etc.
- job_overview with job-level stats
- job_stats array with per-job success rates
- workflow_runs array with per-run job_count breakdown

**Step 3: Run all tests**

```bash
python -m pytest tests/ -v
```

**Step 4: Commit**

```bash
git add dashboard/dashboard_all.json dashboard/dashboard_7d.json dashboard/dashboard_30d.json
git commit -m "data: initial dashboard JSON export for all/7d/30d ranges"
```