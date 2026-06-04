"""Build-Eye Dashboard JSON Export — 从 SQLite 导出多维时间范围的 dashboard JSON 文件。"""
import argparse
import json
import os
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any


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


def _wf_where(date_filter: str | None, extra: str = "") -> str:
    base = "1=1"
    if date_filter:
        base += f" AND created_at {date_filter}"
    if extra:
        base += f" AND {extra}"
    return base


def _job_where(date_filter: str | None, extra: str = "") -> str:
    base = "1=1"
    if date_filter:
        base = f"workflow_run_id IN (SELECT id FROM workflow_runs WHERE created_at {date_filter})"
    if extra:
        if base == "1=1":
            base += f" AND {extra}"
        else:
            base += f" AND {extra}"
    return base


def _count(conn, table: str, where: str, extra_cond: str = "") -> int:
    cond = where
    if extra_cond:
        cond += f" AND {extra_cond}"
    return conn.execute(f"SELECT COUNT(*) FROM {table} WHERE {cond}").fetchone()[0]


def _query_overview(conn, date_filter: str | None) -> Dict[str, Any]:
    wf_where = _wf_where(date_filter)
    total = _count(conn, "workflow_runs", wf_where)
    success = _count(conn, "workflow_runs", wf_where, "conclusion='success'")
    failure = _count(conn, "workflow_runs", wf_where, "conclusion='failure'")
    cancelled = _count(conn, "workflow_runs", wf_where, "conclusion='cancelled'")
    skipped = _count(conn, "workflow_runs", wf_where, "conclusion='skipped'")
    timed_out = _count(conn, "workflow_runs", wf_where, "conclusion='timed_out'")
    action_req = _count(conn, "workflow_runs", wf_where, "conclusion='action_required'")
    success_rate = round(success / max(success + failure, 1) * 100, 1)
    avg_dur = conn.execute(f"SELECT COALESCE(AVG(duration_seconds),0) FROM workflow_runs WHERE {wf_where} AND duration_seconds > 0").fetchone()[0]
    avg_dur_min = round(avg_dur / 60, 1)
    return {
        "total_runs": total, "success_runs": success, "failure_runs": failure,
        "cancelled_runs": cancelled, "skipped_runs": skipped, "timed_out_runs": timed_out,
        "action_required_runs": action_req,
        "success_rate": success_rate, "avg_duration_minutes": avg_dur_min,
        "pipelines": _query_pipelines(conn, date_filter),
    }


def _query_pipelines(conn, date_filter: str | None) -> Dict[str, Any]:
    pipelines = {}
    for ptype in ["nightly", "weekly", "pr", "other"]:
        wf_where = _wf_where(date_filter, f"pipeline_type='{ptype}'")
        t = _count(conn, "workflow_runs", wf_where)
        s = _count(conn, "workflow_runs", wf_where, "conclusion='success'")
        f = _count(conn, "workflow_runs", wf_where, "conclusion='failure'")
        c = _count(conn, "workflow_runs", wf_where, "conclusion='cancelled'")
        avg = conn.execute(f"SELECT COALESCE(AVG(duration_seconds),0) FROM workflow_runs WHERE {wf_where} AND duration_seconds > 0").fetchone()[0]
        pipelines[ptype] = {
            "total_runs": t, "success_runs": s, "failure_runs": f,
            "cancelled_runs": c,
            "success_rate": round(s / max(s + f, 1) * 100, 1),
            "avg_duration_minutes": round(avg / 60, 1),
        }
    return pipelines


def _query_job_overview(conn, date_filter: str | None) -> Dict[str, Any]:
    job_where = _job_where(date_filter)
    total = _count(conn, "job_records", job_where)
    success = _count(conn, "job_records", job_where, "conclusion='success'")
    failure = _count(conn, "job_records", job_where, "conclusion='failure'")
    cancelled = _count(conn, "job_records", job_where, "conclusion='cancelled'")
    skipped = _count(conn, "job_records", job_where, "conclusion='skipped'")
    timed_out = _count(conn, "job_records", job_where, "conclusion='timed_out'")
    success_rate = round(success / max(success + failure, 1) * 100, 1)
    avg_dur = conn.execute(f"SELECT COALESCE(AVG(duration_seconds),0) FROM job_records WHERE {job_where} AND duration_seconds > 0").fetchone()[0]
    return {
        "total_jobs": total, "success_jobs": success, "failure_jobs": failure,
        "cancelled_jobs": cancelled, "skipped_jobs": skipped, "timed_out_jobs": timed_out,
        "job_success_rate": success_rate, "avg_job_duration_minutes": round(avg_dur / 60, 1),
    }


def _query_workflow_runs(conn, date_filter: str | None) -> list:
    wf_where = _wf_where(date_filter)
    rows = conn.execute(f"""
        SELECT wr.id, wr.name, wr.conclusion, wr.started_at, wr.completed_at,
               wr.duration_seconds, wr.pipeline_type, wr.hardware_label,
               wr.html_url, wr.event, wr.head_branch, wr.triggering_actor,
               wr.created_at,
               (SELECT COUNT(*) FROM job_records jr WHERE jr.workflow_run_id = wr.id) as job_count,
               (SELECT COUNT(*) FROM job_records jr WHERE jr.workflow_run_id = wr.id AND jr.conclusion='success') as job_success,
               (SELECT COUNT(*) FROM job_records jr WHERE jr.workflow_run_id = wr.id AND jr.conclusion='failure') as job_failure,
               (SELECT COUNT(*) FROM job_records jr WHERE jr.workflow_run_id = wr.id AND jr.conclusion='cancelled') as job_cancelled
        FROM workflow_runs wr
        WHERE {wf_where}
        ORDER BY wr.created_at DESC
        LIMIT 200
    """).fetchall()
    col_names = ["id", "name", "conclusion", "started_at", "completed_at",
                 "duration_seconds", "pipeline_type", "hardware_label",
                 "html_url", "event", "head_branch", "triggering_actor",
                 "created_at", "job_count", "job_success", "job_failure", "job_cancelled"]
    result = []
    for row in rows:
        d = dict(zip(col_names, row))
        d["duration_minutes"] = round(d["duration_seconds"] / 60, 1) if d["duration_seconds"] else 0
        result.append(d)
    return result


def _query_job_stats(conn, date_filter: str | None) -> list:
    job_where = _job_where(date_filter)
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
               (SELECT wr2.conclusion FROM workflow_runs wr2 WHERE wr2.id = (SELECT jr2.workflow_run_id FROM job_records jr2 WHERE jr2.workflow_name = j.workflow_name AND jr2.job_name = j.job_name ORDER BY jr2.started_at DESC LIMIT 1)) as wf_last_conclusion
        FROM job_records j
        WHERE {job_where}
        GROUP BY workflow_name, job_name
        ORDER BY workflow_name, job_name
    """).fetchall()
    col_names = ["workflow_name", "job_name", "total_runs", "success_runs",
                 "failure_runs", "cancelled_runs", "success_rate",
                 "avg_duration_min", "min_duration_min", "max_duration_min",
                 "last_run_at", "wf_last_conclusion"]
    return [dict(zip(col_names, row)) for row in rows]


def _query_trends(conn) -> Dict[str, Any]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=30)).strftime('%Y-%m-%d')
    rows = conn.execute(f"""
        SELECT DATE(created_at) as date,
               COUNT(*) as total,
               SUM(CASE WHEN conclusion='success' THEN 1 ELSE 0 END) as success,
               SUM(CASE WHEN conclusion='failure' THEN 1 ELSE 0 END) as failure
        FROM workflow_runs
        WHERE created_at >= '{cutoff}'
        GROUP BY DATE(created_at)
        ORDER BY date
    """).fetchall()
    dates = [r[0] for r in rows]
    success_rates = [round(r[2] / max(r[2] + r[3], 1) * 100, 1) for r in rows]
    failure_counts = [r[3] for r in rows]
    job_rows = conn.execute(f"""
        SELECT DATE(jr.started_at) as date,
               COUNT(*) as total,
               SUM(CASE WHEN jr.conclusion='success' THEN 1 ELSE 0 END) as success,
               SUM(CASE WHEN jr.conclusion='failure' THEN 1 ELSE 0 END) as failure
        FROM job_records jr
        WHERE jr.started_at >= '{cutoff}'
        GROUP BY DATE(jr.started_at)
        ORDER BY date
    """).fetchall()
    job_success_rates = [round(r[2] / max(r[2] + r[3], 1) * 100, 1) for r in job_rows]
    return {
        "workflow_success_rate_trend": success_rates,
        "job_success_rate_trend": job_success_rates,
        "failure_count_trend": failure_counts,
        "dates": dates,
    }


def _load_notification_settings() -> Dict[str, Any]:
    return {
        "email_enabled": bool(os.environ.get("SMTP_HOST", "") and os.environ.get("SMTP_TO", "")),
        "smtp_host": os.environ.get("SMTP_HOST", ""),
        "smtp_port": os.environ.get("SMTP_PORT", "465"),
        "smtp_user": os.environ.get("SMTP_USER", ""),
        "smtp_password": "configured" if os.environ.get("SMTP_PASSWORD") else "",
        "smtp_to": os.environ.get("SMTP_TO", ""),
        "smtp_ssl": os.environ.get("SMTP_SSL", "true"),
    }


def export_dashboard_json(db_path: str, output_path: str, range_type: str = "all", start_date: str = None, end_date: str = None) -> dict:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    date_filter = _build_date_filter(range_type, start_date, end_date)

    wf_total = conn.execute("SELECT COUNT(*) FROM workflow_runs").fetchone()[0]
    job_total = conn.execute("SELECT COUNT(*) FROM job_records").fetchone()[0]

    data = {
        "meta": {
            "time_range": range_type,
            "start_date": start_date or "",
            "end_date": end_date or "",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_workflows": wf_total,
            "total_jobs": job_total,
        },
        "workflow_overview": _query_overview(conn, date_filter),
        "job_overview": _query_job_overview(conn, date_filter),
        "workflow_runs": _query_workflow_runs(conn, date_filter),
        "job_stats": _query_job_stats(conn, date_filter),
        "categories": {},
        "health_scores": {"scores": []},
        "trends": _query_trends(conn),
        "notification_settings": _load_notification_settings(),
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