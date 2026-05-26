"""Dashboard data generator - builds rich JSON with URLs, error excerpts, and report links."""
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_URL = "https://github.com/winson-00178005/build-eye"
VLLM_REPO = "https://github.com/vllm-project/vllm-ascend"

TYPE_LABELS = {"pr": "PR CI", "nightly": "Nightly", "weekly": "Weekly"}

_INFRA_WRAPPER_RE = re.compile(
    r"Error:\s+command terminated with non-zero exit code"
    r"|failed to run script step"
    r"|gh.*CLI not found"
    r"|Process completed with exit code"
    r"|The operation was canceled",
    re.IGNORECASE,
)

_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m|\x1b\].*?\x07|\[[0-9;]*m')


def _extract_key_errors_from_excerpt(log_excerpt: str, max_errors: int = 3) -> list:
    if not log_excerpt:
        return []
    key_patterns = [
        re.compile(r"ModuleNotFoundError:\s+(.{5,80})"),
        re.compile(r"ImportError:\s+(.{5,80})"),
        re.compile(r"cannot\s+import\s+(.{5,60})"),
        re.compile(r"AssertionError:\s+(.{5,80})"),
        re.compile(r"AttributeError:\s+(.{5,80})"),
        re.compile(r"RuntimeError:\s+(.{5,80})"),
        re.compile(r"FAILED\s+(.{5,60})", re.IGNORECASE),
        re.compile(r"HCCL\w*[:\s]+(.{5,60})", re.IGNORECASE),
        re.compile(r"npu.*error[:\s]+(.{5,60})", re.IGNORECASE),
        re.compile(r"cache-service[.\w]+[:\s]+(.{5,60})", re.IGNORECASE),
        re.compile(r"compilation\s+failed[:\s]+(.{5,60})", re.IGNORECASE),
        re.compile(r"timeout[:\s]+(.{5,60})", re.IGNORECASE),
        re.compile(r"error:\s+(.{5,80})", re.IGNORECASE),
        re.compile(r"\bError:\s+(.{5,80})"),
    ]
    errors = []
    for line in log_excerpt.split('\n')[:50]:
        clean = _ANSI_RE.sub('', line)
        clean = re.sub(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z\s+', '', clean).strip()
        if not clean or len(clean) < 5 or _INFRA_WRAPPER_RE.search(clean):
            continue
        for pattern in key_patterns:
            m = pattern.search(clean)
            if m:
                err = (m.group(1) if m.lastindex else m.group(0)).strip()[:120]
                if err not in errors:
                    errors.append(err)
                break
    return errors[:max_errors]


def _report_url(date_str: str, pipeline_type: str, sub_dir: str = "") -> str:
    parts = date_str.split('-')
    if len(parts) == 3:
        y, m, d = parts
        base = f"{REPO_URL}/blob/main/reports/{y}/{m}/{d}/{pipeline_type}"
        if sub_dir:
            return f"{base}/{sub_dir}/report.md"
        return f"{base}/report.md"
    return ""


def _scan_reports(reports_dir: Path, max_days: int = 7) -> dict:
    result = {"nightly": [], "weekly": [], "pr": []}
    if not reports_dir.exists():
        return result

    date_paths = {}
    for year_dir in reports_dir.iterdir():
        if not year_dir.is_dir():
            continue
        for month_dir in year_dir.iterdir():
            if not month_dir.is_dir():
                continue
            for day_dir in month_dir.iterdir():
                if not day_dir.is_dir():
                    continue
                date_str = f"{year_dir.name}-{month_dir.name}-{day_dir.name}"
                date_paths[date_str] = day_dir

    sorted_dates = sorted(date_paths.keys(), reverse=True)[:max_days]

    for date_str in sorted_dates:
        dp = date_paths[date_str]
        y, m, d = date_str.split('-')

        for ptype in ["nightly", "weekly", "pr"]:
            type_dir = dp / ptype
            if not type_dir.exists():
                continue

            if ptype in ("nightly", "weekly"):
                report_file = type_dir / "report.md"
                if report_file.exists():
                    entry = {
                        "date": date_str,
                        "url": f"{REPO_URL}/blob/main/reports/{y}/{m}/{d}/{ptype}/report.md",
                        "raw_url": f"{REPO_URL}/raw/main/reports/{y}/{m}/{d}/{ptype}/report.md",
                        "type": ptype,
                    }
                    content = report_file.read_text(encoding='utf-8')
                    fm_data = _parse_frontmatter(content)
                    if fm_data:
                        entry["total_runs"] = int(fm_data.get("total_runs", 0))
                        entry["success_runs"] = int(fm_data.get("success_runs", 0))
                        entry["failure_runs"] = int(fm_data.get("failure_runs", 0))
                    entry["preview"] = _extract_preview(content)
                    result[ptype].append(entry)
            else:
                for pr_dir in sorted(type_dir.iterdir(), reverse=True)[:10]:
                    if not pr_dir.is_dir():
                        continue
                    report_file = pr_dir / "report.md"
                    if not report_file.exists():
                        continue
                    pr_name = pr_dir.name
                    entry = {
                        "date": date_str,
                        "url": f"{REPO_URL}/blob/main/reports/{y}/{m}/{d}/pr/{pr_name}/report.md",
                        "raw_url": f"{REPO_URL}/raw/main/reports/{y}/{m}/{d}/pr/{pr_name}/report.md",
                        "type": "pr",
                        "name": pr_name,
                    }
                    content = report_file.read_text(encoding='utf-8')
                    fm_data = _parse_frontmatter(content)
                    if fm_data:
                        entry["overall_classification"] = fm_data.get("overall_classification", "")
                        entry["workflow_name"] = fm_data.get("workflow_name", "")
                    entry["preview"] = _extract_preview(content)
                    result["pr"].append(entry)

    return result


def _parse_frontmatter(content: str) -> dict:
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end < 0:
        return {}
    fm_text = content[3:end]
    data = {}
    for line in fm_text.strip().split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            data[k.strip()] = v.strip()
    return data


def _extract_preview(content: str, max_chars: int = 300) -> str:
    body_start = 0
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            body_start = end + 3
    body = content[body_start:].strip()
    lines = []
    for line in body.split('\n')[:10]:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('|') and not stripped.startswith('---'):
            lines.append(stripped)
    preview = ' '.join(lines)[:max_chars]
    return preview if preview else body[:max_chars]


def generate_dashboard_data(
    metadata_path: str = "data/build_metadata.json",
    classifications_path: str = "data/classifications.json",
    db_path: str = "data/build_metrics.db",
    reports_dir: str = "reports",
    output_path: str = "dashboard/dashboard_data.json",
) -> dict:
    metadata_list = []
    cls_list = []
    metadata_path_p = Path(metadata_path)
    classifications_path_p = Path(classifications_path)

    if metadata_path_p.exists():
        metadata_list = json.loads(metadata_path_p.read_text(encoding='utf-8'))
    if classifications_path_p.exists():
        cls_list = json.loads(classifications_path_p.read_text(encoding='utf-8'))

    cls_by_run_id = {}
    for c in cls_list:
        run_id = c.get("workflow_run_id")
        if run_id:
            cls_by_run_id[run_id] = c

    meta_by_run_id = {}
    for m in metadata_list:
        run_id = m.get("workflow_run", {}).get("id")
        if run_id:
            meta_by_run_id[run_id] = m

    pipeline_groups = {}
    for m in metadata_list:
        ptype = m.get("pipeline_info", {}).get("pipeline_type", "pr")
        wf = m.get("workflow_run", {})
        conclusion = wf.get("conclusion", "")
        if ptype not in pipeline_groups:
            pipeline_groups[ptype] = {"total": 0, "success": 0, "failure": 0, "runs": []}
        pipeline_groups[ptype]["total"] += 1
        if conclusion == "success":
            pipeline_groups[ptype]["success"] += 1
        else:
            pipeline_groups[ptype]["failure"] += 1
        pipeline_groups[ptype]["runs"].append(m)

    total_all = sum(d["total"] for d in pipeline_groups.values())
    success_all = sum(d["success"] for d in pipeline_groups.values())

    overview = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_runs": total_all,
            "success_runs": success_all,
            "failure_runs": total_all - success_all,
            "overall_success_rate": round((success_all / max(total_all, 1)) * 100, 1),
        },
        "pipelines": {},
    }

    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for ptype, pg in pipeline_groups.items():
        rate = round((pg["success"] / max(pg["total"], 1)) * 100, 1)
        y, m, d = today_str.split('-')
        latest_report_url = ""
        if ptype == "pr":
            pr_dirs = sorted(Path(f"reports/{y}/{m}/{d}/pr").iterdir(), reverse=True) if Path(f"reports/{y}/{m}/{d}/pr").exists() else []
            if pr_dirs:
                latest_report_url = f"{REPO_URL}/blob/main/reports/{y}/{m}/{d}/pr/{pr_dirs[0].name}/report.md"
        elif ptype in ("nightly", "weekly"):
            rp = Path(f"reports/{y}/{m}/{d}/{ptype}/report.md")
            if rp.exists():
                latest_report_url = f"{REPO_URL}/blob/main/reports/{y}/{m}/{d}/{ptype}/report.md"

        overview["pipelines"][ptype] = {
            "total_runs": pg["total"],
            "success_runs": pg["success"],
            "failure_runs": pg["failure"],
            "success_rate": rate,
            "latest_report_url": latest_report_url,
            "vllm_actions_url": f"{VLLM_REPO}/actions",
        }

    failures = []
    for m in metadata_list:
        wf = m.get("workflow_run", {})
        conclusion = wf.get("conclusion", "")
        if conclusion == "success":
            continue

        run_id = wf.get("id")
        name = wf.get("name", "")
        started_at = wf.get("started_at", "")
        url = wf.get("url", "")
        ptype = m.get("pipeline_info", {}).get("pipeline_type", "pr")

        cls_data = cls_by_run_id.get(run_id, {})
        classification_obj = cls_data.get("classification", {}) if cls_data else {}
        cat = classification_obj.get("classification", "") if classification_obj else ""
        confidence = classification_obj.get("confidence", "low") if classification_obj else "low"
        detail = classification_obj.get("category_detail", "") if classification_obj else ""

        if not cat:
            if conclusion == "skipped":
                cat = "infrastructure"
                detail = "Skipped by CI runner (dependency or scheduling issue)"
                confidence = "medium"
            elif conclusion == "cancelled":
                cat = "infrastructure"
                detail = "Cancelled (user abort or newer push superseded)"
                confidence = "medium"
            elif conclusion == "timed_out":
                cat = "infrastructure"
                detail = "Timed out (runner overload or slow environment)"
                confidence = "medium"
            elif conclusion == "action_required":
                cat = "infrastructure"
                detail = "Action required (manual approval needed)"
                confidence = "low"
            else:
                cat = "infrastructure"
                detail = f"Status: {conclusion}"
                confidence = "low"

        key_errors = []
        for fj in m.get("failed_jobs", []):
            excerpt = fj.get("log_excerpt", "")
            if excerpt:
                key_errors = _extract_key_errors_from_excerpt(excerpt)
                if key_errors:
                    break

        report_anchor = ""
        y, mo, d_day = (started_at[:10] if started_at else today_str).split('-') if started_at else today_str.split('-')
        if ptype in ("nightly", "weekly"):
            report_url = f"{REPO_URL}/blob/main/reports/{y}/{mo}/{d_day}/{ptype}/report.md"
        else:
            pr_number = m.get("pr", {})
            pr_name = f"pr-{pr_number.get('number', run_id)}" if pr_number else f"run-{run_id}"
            report_url = f"{REPO_URL}/blob/main/reports/{y}/{mo}/{d_day}/pr/{pr_name}/report.md"

        failure_entry = {
            "run_id": run_id,
            "workflow_name": name,
            "pipeline_type": ptype,
            "status": conclusion,
            "classification": cat,
            "confidence": confidence,
            "detail": detail,
            "started_at": started_at,
            "key_errors": key_errors,
            "run_url": url,
            "report_url": report_url,
            "pr_number": (m.get("pr") or {}).get("number"),
        }
        failures.append(failure_entry)

    failures.sort(key=lambda f: f.get("started_at", ""), reverse=True)

    dist = {}
    for c in cls_list:
        cls_obj = c.get("classification", {})
        cat = cls_obj.get("classification", "unknown")
        dist[cat] = dist.get(cat, 0) + 1

    health_scores = {}
    for ptype, pg in pipeline_groups.items():
        rate = round((pg["success"] / max(pg["total"], 1)) * 100, 1)
        stability = min(100, max(0, 100 - dist.get("infrastructure", 0) * 10))
        efficiency = min(100, max(0, 100 - dist.get("interference", 0) * 15))
        coverage = min(100, pg["total"] * 5)
        score = round(rate * 0.4 + stability * 0.3 + efficiency * 0.2 + coverage * 0.1, 1)

        rating = "danger" if score < 60 else "warning" if score < 70 else "fair" if score < 80 else "good" if score < 90 else "excellent"
        emoji = {"excellent": "🟢", "good": "🟢", "fair": "🟡", "warning": "🟡", "danger": "🔴"}[rating]

        health_scores[ptype] = {"score": score, "rating": rating, "emoji": emoji, "trend": "stable"}

    reports_data = _scan_reports(Path(reports_dir), max_days=7)

    trends = {"timestamp": datetime.now(timezone.utc).isoformat(), "pipelines": {}}
    db_path_p = Path(db_path)
    if db_path_p.exists() and db_path_p.stat().st_size > 0:
        try:
            sys.path.insert(0, str(Path(__file__).parent.parent))
            from monitor.aggregator import BuildAggregator
            agg = BuildAggregator(str(db_path_p))
            for ptype in ["pr", "nightly", "weekly"]:
                trend_data = agg.get_trend_data(ptype, 7)
                if trend_data:
                    trends["pipelines"][ptype] = {
                        "success_rate_trend": [t.get("success_rate", 0) for t in trend_data],
                        "failure_count_trend": [t.get("failure_runs", 0) for t in trend_data],
                        "health_score_trend": [t.get("health_score", 0) for t in trend_data],
                        "dates": [t.get("date", "") for t in trend_data],
                    }
            agg.close()
        except Exception:
            pass

    pr_lookup = {}
    for m in metadata_list:
        pr_number = (m.get("pr") or {}).get("number")
        if pr_number:
            wf = m.get("workflow_run", {})
            conclusion = wf.get("conclusion", "")
            cls_data = cls_by_run_id.get(wf.get("id"), {})
            cls_obj = cls_data.get("classification", {}) if cls_data else {}
            cat = cls_obj.get("classification", "") if cls_obj else ""
            if not cat:
                if conclusion == "failure":
                    cat = "code"
                elif conclusion in ("skipped", "cancelled"):
                    cat = "infrastructure"
                else:
                    cat = "unknown"
            key_errors = []
            for fj in m.get("failed_jobs", []):
                excerpt = fj.get("log_excerpt", "")
                if excerpt:
                    key_errors = _extract_key_errors_from_excerpt(excerpt)
                    if key_errors:
                        break
            entry = {
                "run_id": wf.get("id"),
                "workflow_name": wf.get("name", ""),
                "status": conclusion,
                "classification": cat,
                "key_errors": key_errors,
                "started_at": wf.get("started_at", ""),
                "run_url": wf.get("url", ""),
            }
            if pr_number not in pr_lookup:
                pr_lookup[pr_number] = []
            pr_lookup[pr_number].append(entry)

    alerts = []
    for ptype, pg in pipeline_groups.items():
        rate = round((pg["success"] / max(pg["total"], 1)) * 100, 1)
        if rate < 20:
            alerts.append({"level": "critical", "pipeline": ptype, "message": f"{TYPE_LABELS.get(ptype,ptype)} success rate critically low ({rate}%). Immediate attention required."})
        elif rate < 50:
            alerts.append({"level": "warning", "pipeline": ptype, "message": f"{TYPE_LABELS.get(ptype,ptype)} success rate below 50% ({rate}%). Needs investigation."})

    consecutive_failures = {}
    for ptype in ["pr", "nightly", "weekly"]:
        runs_sorted = sorted(pipeline_groups.get(ptype, {}).get("runs", []), key=lambda r: r.get("workflow_run", {}).get("started_at", ""), reverse=True)
        count = 0
        for r in runs_sorted[:10]:
            if r.get("workflow_run", {}).get("conclusion") == "failure":
                count += 1
            else:
                break
        if count >= 2:
            level = "critical" if count >= 5 else "warning"
            alerts.append({"level": level, "pipeline": ptype, "message": f"{TYPE_LABELS.get(ptype,ptype)} has {count} consecutive failures."})

    data = {
        "overview": overview,
        "trends": trends,
        "categories": {"distribution": dist},
        "recent_failures": {"failures": failures},
        "health_scores": {"scores": health_scores},
        "reports": reports_data,
        "pr_lookup": pr_lookup,
        "alerts": alerts,
    }

    output_path_p = Path(output_path)
    output_path_p.parent.mkdir(parents=True, exist_ok=True)
    output_path_p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

    print(f"Dashboard data generated: {len(failures)} failures, {len(reports_data['nightly'])} nightly reports, {len(reports_data['pr'])} pr reports")
    return data


if __name__ == "__main__":
    generate_dashboard_data()