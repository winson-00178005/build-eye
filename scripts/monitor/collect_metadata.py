"""构建元数据收集 - PR详情、workflow详情、job/step信息。"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

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
                "name": run["name"],
                "workflow_id": run["workflow_id"],
                "status": run["status"],
                "conclusion": run["conclusion"],
                "started_at": run["started_at"],
                "completed_at": run["completed_at"],
                "head_sha": run["head_sha"],
                "head_branch": run["head_branch"],
                "url": run["html_url"],
                "triggering_actor": run.get("triggering_actor", {}).get("login", "unknown")
            },
            "pr": None,
            "jobs": [],
            "failed_jobs": []
        }
        
        if pr:
            metadata["pr"] = {
                "number": pr["number"],
                "title": pr["title"],
                "author": pr["user"]["login"],
                "merged_at": pr.get("merged_at"),
                "merge_commit_sha": pr.get("merge_commit_sha"),
                "url": pr["html_url"],
                "base_ref": pr["base"]["ref"],
                "head_ref": pr["head"]["ref"]
            }
        
        jobs = client.get_workflow_run_jobs(owner, repo, run_id)
        
        for job in jobs:
            job_data = {
                "id": job["id"],
                "name": job["name"],
                "status": job["status"],
                "conclusion": job["conclusion"],
                "started_at": job.get("started_at"),
                "completed_at": job.get("completed_at"),
                "runner_name": job.get("runner_name", "unknown"),
                "runner_group": job.get("runner_group_name", "unknown"),
                "steps": [],
                "url": job["html_url"]
            }
            
            if job.get("steps"):
                for step in job["steps"]:
                    step_data = {
                        "name": step["name"],
                        "number": step["number"],
                        "status": step["status"],
                        "conclusion": step["conclusion"],
                        "started_at": step.get("started_at"),
                        "completed_at": step.get("completed_at")
                    }
                    job_data["steps"].append(step_data)
            
            metadata["jobs"].append(job_data)
            
            if job["conclusion"] == "failure":
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
    
    args = parser.parse_args()
    
    client = GitHubAPIClient()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"输入文件不存在: {input_path}")
        return
    
    workflow_runs = json.loads(input_path.read_text())
    
    if not workflow_runs:
        print("没有 workflow runs 需要处理")
        return
    
    target = workflow_runs[0].get("repository", {}).get("full_name", "vllm-project/vllm-ascend")
    owner, repo = target.split('/')
    
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