"""数据聚合器 - 将构建指标存储到 SQLite 并提供趋势查询。"""
import gc
import sqlite3
import json
from pathlib import Path
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, List, Optional


class BuildAggregator:
    """构建数据聚合与趋势分析。使用 SQLite 存储聚合指标。"""

    def __init__(self, db_path: str | Path = "data/build_metrics.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._closed = False
        self._init_db()

    def close(self):
        """关闭聚合器，执行 WAL checkpoint 并释放资源。"""
        if not self._closed:
            try:
                conn = sqlite3.connect(str(self.db_path))
                conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
                conn.close()
            except Exception:
                pass
            self._closed = True
            gc.collect()

    def __del__(self):
        """析构时确保资源释放。"""
        self.close()

    def _ensure_open(self):
        if self._closed:
            raise RuntimeError("BuildAggregator has been closed")

    def _get_conn(self) -> sqlite3.Connection:
        self._ensure_open()
        conn = sqlite3.connect(str(self.db_path))
        conn.execute("PRAGMA journal_mode=WAL")
        return conn

    def _init_db(self):
        """初始化数据库表。"""
        conn = self._get_conn()
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS daily_aggregates (
                    date TEXT NOT NULL,
                    pipeline_type TEXT NOT NULL,
                    pipeline_name TEXT NOT NULL DEFAULT '',
                    total_runs INTEGER DEFAULT 0,
                    success_runs INTEGER DEFAULT 0,
                    failure_runs INTEGER DEFAULT 0,
                    avg_duration_seconds REAL DEFAULT 0,
                    health_score REAL DEFAULT 0,
                    category_counts TEXT DEFAULT '{}',
                    updated_at TEXT NOT NULL,
                    UNIQUE(date, pipeline_type, pipeline_name)
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS build_records (
                    workflow_run_id INTEGER PRIMARY KEY,
                    pipeline_type TEXT NOT NULL,
                    workflow_name TEXT NOT NULL,
                    pr_number INTEGER,
                    conclusion TEXT NOT NULL,
                    classification TEXT,
                    confidence TEXT,
                    duration_seconds REAL DEFAULT 0,
                    started_at TEXT,
                    completed_at TEXT,
                    recorded_at TEXT NOT NULL
                )
            """)
            conn.commit()
        finally:
            conn.close()

    def record_build(self, metadata: Dict[str, Any], classification: Dict[str, Any] | None = None):
        """记录单次构建结果。"""
        wf = metadata.get("workflow_run", {})
        pipeline_info = metadata.get("pipeline_info", {})
        pipeline_type = pipeline_info.get("pipeline_type", "pr")

        started = wf.get("started_at", "")
        completed = wf.get("completed_at", "")
        duration = self._calc_duration(started, completed)

        classification_data = classification or {}
        cat = classification_data.get("classification", "")
        conf = classification_data.get("confidence", "")

        pr = metadata.get("pr")
        pr_number = pr.get("number") if pr else None

        conn = self._get_conn()
        try:
            conn.execute("""
                INSERT OR REPLACE INTO build_records
                (workflow_run_id, pipeline_type, workflow_name, pr_number,
                 conclusion, classification, confidence, duration_seconds,
                 started_at, completed_at, recorded_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                wf.get("id"),
                pipeline_type,
                wf.get("name", ""),
                pr_number,
                wf.get("conclusion", ""),
                cat,
                conf,
                duration,
                started,
                completed,
                datetime.now(timezone.utc).isoformat()
            ))
            conn.commit()
        finally:
            conn.close()

    def record_builds_batch(self, metadata_list: List[Dict], classifications: List[Dict] | None = None):
        """批量记录构建结果。"""
        cls_map = {}
        if classifications:
            for c in classifications:
                run_id = c.get("workflow_run_id")
                if run_id:
                    cls_map[run_id] = c.get("classification", {})

        for metadata in metadata_list:
            run_id = metadata.get("workflow_run", {}).get("id")
            cls = cls_map.get(run_id) if run_id else None
            self.record_build(metadata, cls)

    def update_daily_aggregate(self, date: str, pipeline_type: str, pipeline_name: str = ""):
        """更新指定日期的聚合数据。"""
        conn = self._get_conn()
        try:
            rows = conn.execute("""
                SELECT conclusion, classification, duration_seconds
                FROM build_records
                WHERE pipeline_type = ? AND started_at LIKE ?
                AND workflow_name LIKE ?
            """, (pipeline_type, f"{date}%", f"%{pipeline_name}%")).fetchall()
        finally:
            conn.close()

        total = len(rows)
        success = sum(1 for r in rows if r[0] == "success")
        failure = total - success
        avg_duration = sum(r[2] for r in rows if r[2]) / max(total, 1)

        category_counts = {}
        for r in rows:
            cat = r[1] or "unknown"
            category_counts[cat] = category_counts.get(cat, 0) + 1

        health = self._calc_health_score(success, total, category_counts)

        conn2 = self._get_conn()
        try:
            conn2.execute("""
                INSERT OR REPLACE INTO daily_aggregates
                (date, pipeline_type, pipeline_name, total_runs, success_runs,
                 failure_runs, avg_duration_seconds, health_score,
                 category_counts, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                date, pipeline_type, pipeline_name, total, success,
                failure, avg_duration, health,
                json.dumps(category_counts),
                datetime.now(timezone.utc).isoformat()
            ))
            conn2.commit()
        finally:
            conn2.close()

    def get_daily_aggregates(self, pipeline_type: str | None = None, days: int = 7) -> List[Dict]:
        """获取最近 N 天的聚合数据。"""
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")

        conn = self._get_conn()
        try:
            conn.row_factory = sqlite3.Row
            if pipeline_type:
                rows = conn.execute("""
                    SELECT * FROM daily_aggregates
                    WHERE pipeline_type = ? AND date >= ?
                    ORDER BY date ASC
                """, (pipeline_type, cutoff)).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM daily_aggregates
                    WHERE date >= ? ORDER BY date ASC
                """, (cutoff,)).fetchall()
        finally:
            conn.close()

        return [dict(r) for r in rows]

    def get_trend_data(self, pipeline_type: str, days: int = 7) -> List[Dict]:
        """获取趋势数据（成功率、平均时长、分类分布）。"""
        aggregates = self.get_daily_aggregates(pipeline_type, days)

        trend = []
        for agg in aggregates:
            total = agg.get("total_runs", 0)
            success = agg.get("success_runs", 0)
            success_rate = (success / max(total, 1)) * 100

            trend.append({
                "date": agg.get("date"),
                "total_runs": total,
                "success_runs": success,
                "failure_runs": agg.get("failure_runs", 0),
                "success_rate": round(success_rate, 1),
                "avg_duration": round(agg.get("avg_duration_seconds", 0), 1),
                "health_score": round(agg.get("health_score", 0), 1),
                "category_counts": json.loads(agg.get("category_counts", "{}"))
            })

        return trend

    def get_recent_failures(self, pipeline_type: str | None = None, limit: int = 10) -> List[Dict]:
        """获取最近的构建失败记录。"""
        conn = self._get_conn()
        try:
            conn.row_factory = sqlite3.Row
            if pipeline_type:
                rows = conn.execute("""
                    SELECT * FROM build_records
                    WHERE conclusion = 'failure' AND pipeline_type = ?
                    ORDER BY recorded_at DESC LIMIT ?
                """, (pipeline_type, limit)).fetchall()
            else:
                rows = conn.execute("""
                    SELECT * FROM build_records
                    WHERE conclusion = 'failure'
                    ORDER BY recorded_at DESC LIMIT ?
                """, (limit,)).fetchall()
        finally:
            conn.close()

        return [dict(r) for r in rows]

    def get_consecutive_failures(self, pipeline_type: str, pipeline_name: str = "") -> int:
        """获取连续失败次数。"""
        conn = self._get_conn()
        try:
            if pipeline_name:
                rows = conn.execute("""
                    SELECT conclusion FROM build_records
                    WHERE pipeline_type = ? AND workflow_name LIKE ?
                    ORDER BY started_at DESC LIMIT 10
                """, (pipeline_type, f"%{pipeline_name}%")).fetchall()
            else:
                rows = conn.execute("""
                    SELECT conclusion FROM build_records
                    WHERE pipeline_type = ?
                    ORDER BY started_at DESC LIMIT 10
                """, (pipeline_type,)).fetchall()
        finally:
            conn.close()

        consecutive = 0
        for r in rows:
            if r[0] == "failure":
                consecutive += 1
            else:
                break

        return consecutive

    def _calc_duration(self, started: str, completed: str) -> float:
        """计算运行时长（秒）。"""
        if not started or not completed:
            return 0
        try:
            s = datetime.fromisoformat(started.replace("Z", "+00:00"))
            e = datetime.fromisoformat(completed.replace("Z", "+00:00"))
            return max((e - s).total_seconds(), 0)
        except (ValueError, TypeError):
            return 0

    def _calc_health_score(self, success_runs: int, total_runs: int, category_counts: Dict) -> float:
        """计算健康度评分。成功率(40%) + 稳定性(30%) + 效率(20%) + 覆盖率(10%)"""
        if total_runs == 0:
            return 0

        success_rate = (success_runs / total_runs) * 100
        stability = min(100, max(0, 100 - category_counts.get("infrastructure", 0) * 10))
        efficiency = min(100, max(0, 100 - category_counts.get("interference", 0) * 15))
        coverage = min(100, total_runs * 5)

        score = success_rate * 0.4 + stability * 0.3 + efficiency * 0.2 + coverage * 0.1
        return round(min(score, 100), 1)

    def get_health_rating(self, score: float) -> Dict[str, str]:
        """根据分数返回评级。"""
        if score >= 90:
            return {"rating": "优秀", "color": "green", "emoji": "🟢"}
        elif score >= 80:
            return {"rating": "良好", "color": "green", "emoji": "🟢"}
        elif score >= 70:
            return {"rating": "一般", "color": "yellow", "emoji": "🟡"}
        elif score >= 60:
            return {"rating": "较差", "color": "yellow", "emoji": "🟡"}
        else:
            return {"rating": "危险", "color": "red", "emoji": "🔴"}