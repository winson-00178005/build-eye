"""构建元数据收集 - PR详情、workflow详情、job/step信息。"""
import argparse
import json
import sys
import os
from pathlib import Path

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

from monitor.github_client import GitHubAPIClient


def collect_build_metadata(
    client: GitHubAPIClient,
    owner: str,
    repo: str,
    workflow_runs: list
) -> list:
    """
    为每个失败的 workflow run 收集完整元数据。
    
    收集内容:
    - PR 信息 (number, title, author, merged_at)
    - Workflow run 信息 (id, name, started_at, completed_at)
    - Job 信息 (每个失败 job 的 steps)
    - 日志片段 (失败 step 的输出)
    """
    metadata_list = []
    
    for run in workflow_runs:
        run_id = run["id"]
        pr = run.get("associated_pr")
        
        print(f"收集 {run_id} ({run['name']}) 的元数据...")
        
        metadata = {
            "workflow_run": {
                "id": run_id,
                "name": run.get("name", ""),
                "workflow_id": run.get("workflow_id"),
                "status": run.get("status", ""),
                "conclusion": run.get("conclusion", ""),
                "started_at": run.get("run_started_at", run.get("started_at")),
                "completed_at": run.get("updated_at", run.get("completed_at")),
                "head_sha": run.get("head_sha", ""),
                "head_branch": run.get("head_branch", ""),
                "url": run.get("html_url", ""),
                "triggering_actor": (run.get("triggering_actor") or {}).get("login", "unknown")
            },
            "pr": None,
            "jobs": [],
            "failed_jobs": []
        }
        
        if pr:
            metadata["pr"] = {
                "number": pr.get("number"),
                "title": pr.get("title", ""),
                "author": (pr.get("user") or {}).get("login", "unknown"),
                "merged_at": pr.get("merged_at"),
                "merge_commit_sha": pr.get("merge_commit_sha"),
                "url": pr.get("html_url", ""),
                "base_ref": (pr.get("base") or {}).get("ref", ""),
                "head_ref": (pr.get("head") or {}).get("ref", "")
            }
        
        jobs = client.get_workflow_run_jobs(owner, repo, run_id)
        
        for job in jobs:
            job_data = {
                "id": job.get("id"),
                "name": job.get("name", ""),
                "status": job.get("status", ""),
                "conclusion": job.get("conclusion", ""),
                "started_at": job.get("started_at"),
                "completed_at": job.get("completed_at"),
                "runner_name": job.get("runner_name", "unknown"),
                "runner_group": job.get("runner_group_name", "unknown"),
                "steps": [],
                "url": job.get("html_url", "")
            }
            
            if job.get("steps"):
                for step in job["steps"]:
                    step_data = {
                        "name": step.get("name", ""),
                        "number": step.get("number", 0),
                        "status": step.get("status", ""),
                        "conclusion": step.get("conclusion", ""),
                        "started_at": step.get("started_at"),
                        "completed_at": step.get("completed_at")
                    }
                    job_data["steps"].append(step_data)
            
            metadata["jobs"].append(job_data)
            
            if job.get("conclusion") == "failure":
                metadata["failed_jobs"].append(job_data)
        
        metadata_list.append(metadata)
    
    return metadata_list


def extract_failed_step_logs(
    client: GitHubAPIClient,
    owner: str,
    repo: str,
    metadata_list: list,
    max_lines: int = 100
) -> list:
    """提取失败 job 的日志片段。"""
    
    for metadata in metadata_list:
        for failed_job in metadata["failed_jobs"]:
            job_id = failed_job["id"]
            
            logs = client.get_job_logs(owner, repo, job_id)
            
            if logs:
                lines = logs.split('\n')
                failed_job["log_excerpt"] = '\n'.join(lines[-max_lines:])
                failed_job["log_url"] = f"https://github.com/{owner}/{repo}/actions/runs/{metadata['workflow_run']['id']}/job/{job_id}"
    
    return metadata_list


def main():
    parser = argparse.ArgumentParser(description='收集构建元数据')
    parser.add_argument('--input', type=str, default='data/workflow_runs.json',
                        help='输入 workflow runs 文件')
    parser.add_argument('--output', type=str, default='data/build_metadata.json',
                        help='输出元数据文件')
    parser.add_argument('--max-log-lines', type=int, default=100,
                        help='日志片段最大行数')
    parser.add_argument('--max-runs', type=int, default=20,
                        help='最大处理 workflow runs 数')
    parser.add_argument('--timeout', type=int, default=30,
                        help='API 请求超时时间（秒）')
    
    args = parser.parse_args()
    
    client = GitHubAPIClient(timeout=args.timeout)
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"输入文件不存在: {input_path}")
        sys.exit(1)
    
    workflow_runs = json.loads(input_path.read_text(encoding='utf-8'))
    
    if not workflow_runs:
        print("没有 workflow runs 需要处理，写入空结果")
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        sys.exit(0)
    
    if len(workflow_runs) > args.max_runs:
        print(f"workflow runs 数量 ({len(workflow_runs)}) 超过上限 ({args.max_runs})，仅处理前 {args.max_runs} 个")
        workflow_runs = workflow_runs[:args.max_runs]
    
    runtime_config_path = Path("data/config.json")
    if runtime_config_path.exists():
        runtime_config = json.loads(runtime_config_path.read_text(encoding='utf-8'))
        owner = runtime_config["target_repository"]["owner"]
        repo = runtime_config["target_repository"]["repo"]
    else:
        owner, repo = "vllm-project", "vllm-ascend"
    
    print(f"正在收集 {len(workflow_runs)} 个 workflow runs 的元数据...")
    
    metadata = collect_build_metadata(client, owner, repo, workflow_runs)
    
    metadata = extract_failed_step_logs(
        client, owner, repo, metadata,
        args.max_log_lines
    )
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"已保存 {len(metadata)} 条元数据到 {output_path}")


if __name__ == "__main__":
    main()