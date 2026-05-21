"""配置脚本 - 根据工作流输入参数动态配置监测系统。"""
import argparse
import json
from pathlib import Path
from config_loader import config, Config

def main():
    parser = argparse.ArgumentParser(description='配置 Build-Eye 监测参数')
    parser.add_argument('--lookback', type=int, default=24, help='检查过去多少小时')
    parser.add_argument('--target', type=str, default='vllm-project/vllm-ascend', help='目标仓库')
    parser.add_argument('--dry-run', type=str, default='false', help='试运行模式')
    parser.add_argument('--output', type=str, default='data/config.json', help='配置输出路径')
    
    args = parser.parse_args()
    
    owner, repo = args.target.split('/')
    
    config_data = {
        "lookback_hours": args.lookback,
        "target_repository": {
            "owner": owner,
            "repo": repo,
            "url": f"https://github.com/{owner}/{repo}"
        },
        "dry_run": args.dry_run.lower() == 'true',
        "archive_repository": config.archive_repo
    }
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=2, ensure_ascii=False)
    
    print(f"配置已保存到 {output_path}")
    print(f"目标仓库: {owner}/{repo}")
    print(f"检查时间范围: {args.lookback} 小时")
    print(f"试运行模式: {args.dry_run}")

if __name__ == "__main__":
    main()