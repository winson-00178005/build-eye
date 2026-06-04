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


def extract_hardware_label(name: str | None) -> str:
    if not name:
        return ""
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
    skip_jobs: bool = False,
) -> dict:
    if full_sync:
        created_filter = None
    elif lookback_hours:
        cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
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

    kwargs = {
        "owner": owner, "repo": repo,
        "status": "completed",
        "per_page": 100,
        "max_pages": 100
    }
    if created_filter:
        kwargs["created"] = created_filter
    runs = client.get_workflow_runs(**kwargs)

    print(f"Fetched {len(runs)} workflow runs")

    new_runs = 0
    new_jobs = 0

    for run in runs:
        run_id = run.get("id") or 0
        enriched = detector.detect_all([dict(run)])
        ptype = enriched[0].get("pipeline_info", {}).get("pipeline_type", "unknown")
        if ptype == "unmonitored":
            ptype = "other"
        hw = extract_hardware_label(run.get("name", ""))
        aggregator.record_workflow_run(run, pipeline_type=ptype, hardware_label=hw)
        new_runs += 1

        if not run_id:
            continue
        if skip_jobs:
            continue
        jobs = client.get_workflow_run_jobs(owner, repo, run_id)
        if jobs:
            wf_name = run.get("name", "") or ""
            for job in jobs:
                job["workflow_run_id"] = run_id
                job["workflow_name"] = wf_name
                job["hardware_label"] = hw or extract_hardware_label(job.get("runner_name") or "")
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
    parser.add_argument("--skip-jobs", action="store_true", help="Skip job fetching (only sync workflow runs)")
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
        lookback_hours=args.lookback,
        skip_jobs=args.skip_jobs
    )

    aggregator.close()
    print(f"Sync complete: {result}")


if __name__ == "__main__":
    main()