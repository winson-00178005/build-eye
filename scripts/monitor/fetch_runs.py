"""获取 workflow runs - 分页和过滤。"""
import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from monitor.github_client import GitHubAPIClient
from monitor.config_loader import config


def fetch_failed_workflow_runs(
    client: GitHubAPIClient,
    owner: str,
    repo: str,
    lookback_hours: int = 24,
    branch: str = "main"
) -> list:
    """
    获取失败的 workflow runs 列表。
    
    过滤条件:
    - status = completed
    - conclusion = failure
    - branch = main
    - 时间范围 = 最近 N 小时
    """
    runs = client.get_workflow_runs(
        owner=owner,
        repo=repo,
        branch=branch,
        status="completed"
    )
    
    cutoff_time = datetime.now() - timedelta(hours=lookback_hours)
    
    failed_runs = []
    for run in runs:
        if run.get("conclusion") == "failure":
            completed_at_str = run.get("completed_at")
            if completed_at_str:
                completed_at = datetime.fromisoformat(completed_at_str.replace("Z", "+00:00"))
                if completed_at > cutoff_time:
                    failed_runs.append(run)
            else:
                failed_runs.append(run)
    
    return failed_runs


def filter_by_workflow(runs: list, workflow_names: list | None) -> list:
    """按 workflow 名称过滤。"""
    if not workflow_names:
        return runs
    return [r for r in runs if r.get("name") in workflow_names]


def filter_by_pr_association(runs: list, client: GitHubAPIClient, owner: str, repo: str) -> list:
    """只保留关联 PR 的 workflow runs。"""
    pr_runs = []
    
    for run in runs:
        commit_sha = run.get("head_sha")
        if commit_sha:
            pr = client.get_pr_for_commit(owner, repo, commit_sha)
            if pr:
                run["associated_pr"] = pr
                pr_runs.append(run)
    
    return pr_runs


def main():
    parser = argparse.ArgumentParser(description='获取失败的 workflow runs')
    parser.add_argument('--output', type=str, default='data/workflow_runs.json',
                        help='输出文件路径')
    parser.add_argument('--lookback', type=int, default=None,
                        help='检查过去多少小时（可选，从config读取）')
    parser.add_argument('--config', type=str, default='data/config.json',
                        help='运行时配置文件（由 configure.py 生成）')
    
    args = parser.parse_args()
    
    client = GitHubAPIClient()
    
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
    
    print(f"正在获取 {owner}/{repo} 的失败构建...")
    
    failed_runs = fetch_failed_workflow_runs(
        client, owner, repo, lookback
    )
    
    print(f"找到 {len(failed_runs)} 个失败的 workflow runs")
    
    pr_runs = filter_by_pr_association(failed_runs, client, owner, repo)
    
    print(f"其中 {len(pr_runs)} 个关联 PR")
    
    monitored_workflows = target.get("monitored_workflows")
    if monitored_workflows and isinstance(monitored_workflows, list):
        pr_runs = filter_by_workflow(pr_runs, monitored_workflows)
        print(f"监控范围内: {len(pr_runs)} 个")
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(pr_runs, f, indent=2, ensure_ascii=False)
    
    print(f"已保存到 {output_path}")


if __name__ == "__main__":
    main()