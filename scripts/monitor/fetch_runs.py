"""获取 workflow runs - 分页、过滤、流水线类型识别。"""
import argparse
import json
import sys
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

from monitor.github_client import GitHubAPIClient
from monitor.config_loader import config
from monitor.pipeline_detector import PipelineDetector


def fetch_workflow_runs(
    client: GitHubAPIClient,
    owner: str,
    repo: str,
    lookback_hours: int = 24,
    branch: str | None = None,
    status_filter: str = "failure"
) -> list:
    """
    获取 workflow runs 列表。
    
    status_filter:
      - "failure": 只返回失败的 run (PR 流水线默认)
      - "all": 返回所有已完成的 run (Nightly/Weekly 需要成功率数据)
    
    branch:
      - None: 不按分支过滤（推荐，跨仓库监控时 PR 在各分支运行）
      - "main": 只获取 main 分支的 run
    """
    cutoff_time = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    created_filter = f">={cutoff_time.strftime('%Y-%m-%dT%H:%M:%SZ')}"
    
    runs = client.get_workflow_runs(
        owner=owner,
        repo=repo,
        branch=branch,
        status="completed",
        created=created_filter,
        max_pages=5
    )
    
    if status_filter == "failure":
        runs = [r for r in runs if r.get("conclusion") == "failure"]
    
    return runs


def fetch_failed_workflow_runs(client, owner, repo, lookback_hours=24, branch=None):
    """兼容旧调用: 只获取失败的 run。"""
    return fetch_workflow_runs(client, owner, repo, lookback_hours, branch, "failure")


def filter_by_workflow(runs: list, workflow_names: list | None) -> list:
    """按 workflow 名称过滤。"""
    if not workflow_names:
        return runs
    return [r for r in runs if r.get("name") in workflow_names]


def enrich_pr_association(runs: list, client: GitHubAPIClient, owner: str, repo: str) -> list:
    """尝试为 workflow runs 添加 PR 关联信息（不过滤）。"""
    if not client.token:
        print("未配置 Token，跳过 PR 关联查询")
        return runs
    
    enriched = []
    
    for run in runs:
        run_data = dict(run)
        
        pull_requests = run.get("pull_requests", [])
        if pull_requests:
            pr_ref = pull_requests[0]
            pr_number = pr_ref.get("number")
            if pr_number:
                pr_detail = client.get_pr(owner, repo, pr_number)
                if pr_detail:
                    run_data["associated_pr"] = pr_detail
                    enriched.append(run_data)
                    continue
        
        commit_sha = run.get("head_sha")
        if commit_sha:
            pr = client.get_pr_for_commit(owner, repo, commit_sha)
            if pr:
                run_data["associated_pr"] = pr
                enriched.append(run_data)
                continue
        
        display_title = run.get("display_title", "")
        if display_title:
            pr = client.search_pr_by_title(owner, repo, display_title)
            if pr:
                run_data["associated_pr"] = pr
        
        enriched.append(run_data)
    
    return enriched


def main():
    parser = argparse.ArgumentParser(description='获取 workflow runs')
    parser.add_argument('--output', type=str, default='data/workflow_runs.json',
                        help='输出文件路径')
    parser.add_argument('--lookback', type=int, default=None,
                        help='检查过去多少小时')
    parser.add_argument('--config', type=str, default='data/config.json',
                        help='运行时配置文件')
    parser.add_argument('--timeout', type=int, default=30,
                        help='API 请求超时时间（秒）')
    parser.add_argument('--pipeline-type', type=str, default=None,
                        choices=['pr', 'nightly', 'weekly', 'all'],
                        help='只获取指定流水线类型的 run (all=不过滤)')
    parser.add_argument('--status', type=str, default='failure',
                        choices=['failure', 'all'],
                        help='获取状态: failure=只失败, all=全部(含成功)')
    
    args = parser.parse_args()
    
    client = GitHubAPIClient(timeout=args.timeout)
    
    target = config.target_repo
    owner = target["owner"]
    repo = target["repo"]
    
    lookback = args.lookback
    if lookback is None:
        config_path = Path(args.config)
        if config_path.exists():
            runtime_config = json.loads(config_path.read_text(encoding='utf-8'))
            lookback = runtime_config.get("lookback_hours", 24)
        else:
            lookback = 24
    
    print(f"正在获取 {owner}/{repo} 的构建 (status={args.status})...")
    
    runs = fetch_workflow_runs(
        client, owner, repo, lookback, status_filter=args.status
    )
    
    print(f"找到 {len(runs)} 个 workflow runs")
    
    if args.pipeline_type in ("nightly", "weekly"):
        print(f"Nightly/Weekly 流水线跳过 PR 关联查询（避免 rate limit）")
        enriched_runs = runs
    elif args.pipeline_type == 'all':
        enriched_runs = enrich_pr_association(runs, client, owner, repo)
        runs_with_pr = [r for r in enriched_runs if r.get("associated_pr")]
        runs_without_pr = [r for r in enriched_runs if not r.get("associated_pr")]
        print(f"其中 {len(runs_with_pr)} 个关联 PR, {len(runs_without_pr)} 个无 PR 关联")
    else:
        enriched_runs = enrich_pr_association(runs, client, owner, repo)
        runs_with_pr = [r for r in enriched_runs if r.get("associated_pr")]
        runs_without_pr = [r for r in enriched_runs if not r.get("associated_pr")]
        print(f"其中 {len(runs_with_pr)} 个关联 PR, {len(runs_without_pr)} 个无 PR 关联")
    
    monitored_workflows = target.get("monitored_workflows")
    if monitored_workflows and isinstance(monitored_workflows, list):
        enriched_runs = filter_by_workflow(enriched_runs, monitored_workflows)
        print(f"监控范围内: {len(enriched_runs)} 个")
    
    detector = PipelineDetector(config.pipeline_types)
    enriched_runs = detector.detect_all(enriched_runs)
    
    unmonitored_count = sum(1 for r in enriched_runs if r.get("pipeline_info", {}).get("pipeline_type") == "unmonitored")
    nightly_count = sum(1 for r in enriched_runs if r.get("pipeline_info", {}).get("pipeline_type") == "nightly")
    weekly_count = sum(1 for r in enriched_runs if r.get("pipeline_info", {}).get("pipeline_type") == "weekly")
    pr_count = sum(1 for r in enriched_runs if r.get("pipeline_info", {}).get("pipeline_type") == "pr")
    print(f"流水线类型: PR={pr_count}, Nightly={nightly_count}, Weekly={weekly_count}, 不监控={unmonitored_count}")
    
    enriched_runs = detector.filter_by_type(enriched_runs, "unmonitored", exclude=True)
    print(f"排除不监控的 run 后: {len(enriched_runs)} 个")
    
    if args.pipeline_type and args.pipeline_type != 'all':
        enriched_runs = detector.filter_by_type(enriched_runs, args.pipeline_type)
        print(f"过滤为 {args.pipeline_type} 类型: {len(enriched_runs)} 个")
    elif args.pipeline_type == 'all':
        print(f"保留所有流水线类型: {len(enriched_runs)} 个")
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(enriched_runs, f, indent=2, ensure_ascii=False)
    
    print(f"已保存到 {output_path}")


if __name__ == "__main__":
    main()