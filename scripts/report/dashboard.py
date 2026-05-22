"""可视化报表数据服务 - 生成 Dashboard JSON 数据供前端消费。"""
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional


class DashboardService:
    """Dashboard 数据生成服务。"""

    def __init__(self, aggregator=None):
        self.aggregator = aggregator

    def generate_overview(self, metadata_list: List[Dict] = None) -> Dict[str, Any]:
        """生成概览数据。"""
        overview = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pipelines": {},
            "summary": {
                "total_runs": 0,
                "success_runs": 0,
                "failure_runs": 0,
                "overall_success_rate": 0
            }
        }

        if metadata_list:
            pipeline_groups = {}
            for m in metadata_list:
                ptype = m.get("pipeline_info", {}).get("pipeline_type", "pr")
                if ptype not in pipeline_groups:
                    pipeline_groups[ptype] = {"total": 0, "success": 0, "failure": 0}
                wf = m.get("workflow_run", {})
                conclusion = wf.get("conclusion", "")
                pipeline_groups[ptype]["total"] += 1
                if conclusion == "success":
                    pipeline_groups[ptype]["success"] += 1
                else:
                    pipeline_groups[ptype]["failure"] += 1

            for ptype, data in pipeline_groups.items():
                rate = (data["success"] / max(data["total"], 1)) * 100
                overview["pipelines"][ptype] = {
                    "total_runs": data["total"],
                    "success_runs": data["success"],
                    "failure_runs": data["failure"],
                    "success_rate": round(rate, 1)
                }

            total_all = sum(d["total"] for d in pipeline_groups.values())
            success_all = sum(d["success"] for d in pipeline_groups.values())
            overview["summary"]["total_runs"] = total_all
            overview["summary"]["success_runs"] = success_all
            overview["summary"]["failure_runs"] = total_all - success_all
            overview["summary"]["overall_success_rate"] = round((success_all / max(total_all, 1)) * 100, 1)

        if self.aggregator:
            for ptype in ["pr", "nightly", "weekly"]:
                agg = self.aggregator.get_daily_aggregates(ptype, 1)
                if agg:
                    overview["pipelines"][ptype] = {
                        "total_runs": agg[0].get("total_runs", 0),
                        "success_runs": agg[0].get("success_runs", 0),
                        "failure_runs": agg[0].get("failure_runs", 0),
                        "success_rate": round((agg[0].get("success_runs", 0) / max(agg[0].get("total_runs", 1), 1)) * 100, 1),
                        "health_score": agg[0].get("health_score", 0)
                    }

        return overview

    def generate_trends(self, days: int = 30) -> Dict[str, Any]:
        """生成趋势数据。"""
        trends = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "period_days": days,
            "pipelines": {}
        }

        if not self.aggregator:
            return trends

        for ptype in ["pr", "nightly", "weekly"]:
            trend_data = self.aggregator.get_trend_data(ptype, days)
            if trend_data:
                trends["pipelines"][ptype] = {
                    "success_rate_trend": [t.get("success_rate", 0) for t in trend_data],
                    "failure_count_trend": [t.get("failure_runs", 0) for t in trend_data],
                    "duration_trend": [t.get("avg_duration", 0) for t in trend_data],
                    "health_score_trend": [t.get("health_score", 0) for t in trend_data],
                    "dates": [t.get("date", "") for t in trend_data]
                }

        return trends

    def generate_categories(self, metadata_list: List[Dict] = None, days: int = 7) -> Dict[str, Any]:
        """生成分类统计数据。"""
        categories = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "distribution": {},
            "by_pipeline_type": {}
        }

        if metadata_list:
            for m in metadata_list:
                cls = m.get("classification", {})
                if cls:
                    cat = cls.get("classification", "unknown")
                    categories["distribution"][cat] = categories["distribution"].get(cat, 0) + 1

                    ptype = m.get("pipeline_info", {}).get("pipeline_type", "pr")
                    if ptype not in categories["by_pipeline_type"]:
                        categories["by_pipeline_type"][ptype] = {}
                    categories["by_pipeline_type"][ptype][cat] = categories["by_pipeline_type"][ptype].get(cat, 0) + 1

        if self.aggregator:
            agg = self.aggregator.get_daily_aggregates(None, days)
            for a in agg:
                cat_counts = json.loads(a.get("category_counts", "{}"))
                ptype = a.get("pipeline_type", "")
                for cat, count in cat_counts.items():
                    categories["distribution"][cat] = categories["distribution"].get(cat, 0) + count

        return categories

    def generate_recent_failures(self, limit: int = 10) -> Dict[str, Any]:
        """生成最近失败列表。"""
        result = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "failures": []
        }

        if self.aggregator:
            failures = self.aggregator.get_recent_failures(None, limit)
            result["failures"] = failures

        return result

    def generate_health_scores(self) -> Dict[str, Any]:
        """生成各流水线类型的健康评分。"""
        result = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "scores": {}
        }

        if not self.aggregator:
            return result

        for ptype in ["pr", "nightly", "weekly"]:
            agg = self.aggregator.get_daily_aggregates(ptype, 1)
            if agg:
                score = agg[0].get("health_score", 0)
                rating = self.aggregator.get_health_rating(score)
                result["scores"][ptype] = {
                    "score": score,
                    "rating": rating["rating"],
                    "emoji": rating["emoji"],
                    "trend": "stable"
                }

                trend = self.aggregator.get_trend_data(ptype, 7)
                if len(trend) >= 2:
                    diff = trend[-1].get("health_score", 0) - trend[-2].get("health_score", 0)
                    if diff > 2:
                        result["scores"][ptype]["trend"] = "improving"
                    elif diff < -2:
                        result["scores"][ptype]["trend"] = "declining"

        return result

    def generate_full_dashboard(self, metadata_list: List[Dict] = None) -> Dict[str, Any]:
        """生成完整 Dashboard 数据。"""
        return {
            "overview": self.generate_overview(metadata_list),
            "trends": self.generate_trends(),
            "categories": self.generate_categories(metadata_list),
            "recent_failures": self.generate_recent_failures(),
            "health_scores": self.generate_health_scores()
        }

    def save_dashboard(self, dashboard_data: Dict, output_path: Path):
        """保存 Dashboard 数据到 JSON 文件。"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(dashboard_data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )