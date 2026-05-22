"""聚合器 CLI - 将构建数据写入 SQLite 聚合表。"""
import json
import argparse
import sys
from pathlib import Path

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

from monitor.aggregator import BuildAggregator


def main():
    parser = argparse.ArgumentParser(description='聚合构建指标到数据库')
    parser.add_argument('--metadata', type=str, default='data/build_metadata.json',
                        help='构建元数据文件')
    parser.add_argument('--classifications', type=str, default='data/classifications.json',
                        help='分类结果文件')
    parser.add_argument('--db', type=str, default='data/build_metrics.db',
                        help='SQLite 数据库路径')

    args = parser.parse_args()

    aggregator = BuildAggregator(args.db)

    metadata_path = Path(args.metadata)
    if metadata_path.exists():
        metadata_list = json.loads(metadata_path.read_text(encoding='utf-8'))

        classifications = None
        cls_path = Path(args.classifications)
        if cls_path.exists():
            classifications = json.loads(cls_path.read_text(encoding='utf-8'))

        aggregator.record_builds_batch(metadata_list, classifications)

        today = metadata_path.parent.parent / "data" / "config.json"
        from datetime import datetime, timezone
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

        for ptype in ["pr", "nightly", "weekly"]:
            aggregator.update_daily_aggregate(date_str, ptype)

        print(f"已聚合 {len(metadata_list)} 条构建数据到 {args.db}")
    else:
        print(f"元数据文件不存在: {metadata_path}")


if __name__ == "__main__":
    main()