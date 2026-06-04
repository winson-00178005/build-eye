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


def _fetch_runs_batch(client, owner, repo, created_filter, max_pages=100):
    kwargs = {
        "owner": owner, "repo": repo,
        "status": "completed",
        "per_page": 100,
        "max_pages": max_pages,
    }
    if created_filter:
        kwargs["created"] = created_filter
    return client.get_workflow_runs(**kwargs)


def _generate_week_ranges(start_date, end_date):
    ranges = []
    current = start_date
    while current < end_date:
        range_end = min(current + timedelta(days=7), end_date + timedelta(days=1))
        ranges.append((current, range_end))
        current = range_end
    return ranges


def sync_runs_and_jobs(
    client: GitHubAPIClient,
    owner: str,
    repo: str,
    aggregator: BuildAggregator,
    detector: PipelineDetector,
    full_sync: bool = False,
    lookback_hours: int | None = None,
    skip_jobs: bool = False,
    months_back: int = 6,
) -> dict:
    total_runs = 0
    total_jobs = 0

    if full_sync:
        end_date = datetime.now(timezone.utc)
        start_date = end_date - timedelta(days=30 * months_back)
        week_ranges = _generate_week_ranges(start_date, end_date)
        print(f"Full sync: fetching {len(week_ranges)} week ranges from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        for range_start, range_end in week_ranges:
            created_filter = f"{range_start.strftime('%Y-%m-%dT%H:%M:%SZ')}..{range_end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
            runs = _fetch_runs_batch(client, owner, repo, created_filter)
            print(f"  Week {range_start.strftime('%Y-%m-%d')}: fetched {len(runs)} runs")
            new_runs, new_jobs = _process_runs(runs, client, owner, repo, aggregator, detector, skip_jobs)
            total_runs += new_runs
            total_jobs += new_jobs
    elif lookback_hours:
        cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
        created_filter = f">={cutoff.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        runs = _fetch_runs_batch(client, owner, repo, created_filter)
        new_runs, new_jobs = _process_runs(runs, client, owner, repo, aggregator, detector, skip_jobs)
        total_runs += new_runs
        total_jobs += new_jobs
    else:
        conn = aggregator._get_conn()
        try:
            last_sync = conn.execute("SELECT MAX(updated_at) FROM workflow_runs").fetchone()[0]
        finally:
            conn.close()
        if last_sync:
            created_filter = f">={last_sync}"
        else:
            cutoff = datetime.now(timezone.utc) - timedelta(hours=168)
            created_filter = f">={cutoff.strftime('%Y-%m-%dT%H:%M:%SZ')}"
        runs = _fetch_runs_batch(client, owner, repo, created_filter)
        new_runs, new_jobs = _process_runs(runs, client, owner, repo, aggregator, detector, skip_jobs)
        total_runs += new_runs
        total_jobs += new_jobs

    print(f"Synced {total_runs} workflow runs, {total_jobs} jobs total")
    return {"workflow_runs": total_runs, "jobs": total_jobs}


def _process_runs(runs, client, owner, repo, aggregator, detector, skip_jobs):
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

        if not run_id or skip_jobs:
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

    return new_runs, new_jobs


def main():
    parser = argparse.ArgumentParser(description="Sync GitHub workflow runs and jobs to SQLite")
    parser.add_argument("--db", default="data/build_metrics.db", help="SQLite database path")
    parser.add_argument("--full-sync", action="store_true", help="Full sync (no time window)")
    parser.add_argument("--lookback", type=int, default=None, help="Lookback hours for partial sync")
    parser.add_argument("--months-back", type=int, default=6, help="Months of history for full sync")
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
        skip_jobs=args.skip_jobs,
        months_back=args.months_back,
    )

    aggregator.close()
    print(f"Sync complete: {result}")


if __name__ == "__main__":
    main()