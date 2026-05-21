# Build-Eye CI 监测系统

**构建鹰眼** - vLLM-Ascend CI 构建自动化监测与根因分析系统

## 系统概述

Build-Eye 是专为 vLLM-Ascend 项目设计的 CI 构建监测系统，能够：

- **自动监测** vllm-project/vllm-ascend 仓库的 CI 构建
- **智能分类** 构建失败根因（代码问题/基础设施问题/干扰问题）
- **生成建议** 低成本可落地的修复方案
- **归档报告** 标准化报告自动归档到 build-eye 仓库

## 监测目标

- 主力监测仓: https://github.com/vllm-project/vllm-ascend
- 归档托管仓: https://github.com/winson-00178005/build-eye.git

## 失败根因分类

### 1. PR 代码问题

- 测试断言失败
- 编译错误（CMake、clang）
- Python 导入错误
- vLLM API 不兼容
- Ascend kernel 编译问题

### 2. 基础设施问题

- K8s cache-service 失败（cache-service.nginx-pypi-cache）
- Runner 不可用
- NPU 硬件问题（910B/910C/310P）
- CANN toolkit 问题
- HCCL 多卡通信失败
- Docker 镜像拉取失败
- Csrc 缓存失败
- 构建超时

### 3. 多 PR 并发干扰

- 短时间内多个 PR 合入
- vLLM 版本矩阵差异
- Runner 资源竞争
- CANN 镜像更新影响

## 快速开始

### 1. 配置 GitHub Token

参见 `docs/token-setup.md` 配置必需的密钥。

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 手动触发监测

```bash
python scripts/monitor/fetch_runs.py --output data/workflow_runs.json
python scripts/monitor/collect_metadata.py --input data/workflow_runs.json --output data/build_metadata.json
python scripts/classify/classifier.py --input data/build_metadata.json --output data/classifications.json
python scripts/recommend/recommender.py --input data/classifications.json --output data/recommendations.json
python scripts/report/generator.py --input data/recommendations.json --output reports/
```

### 4. 归档报告

```bash
python scripts/archive/archiver.py --input reports/ --repo https://github.com/winson-00178005/build-eye.git
```

## GitHub Actions 工作流

系统支持两种触发模式：

### 定时轮询

每 6 小时自动检查最近的构建失败。

工作流文件: `.github/workflows/monitor.yml`

### 手动触发

通过 GitHub Actions 的 `workflow_dispatch` 手动触发。

可选参数：
- `lookback_hours`: 检查过去多少小时（默认 24）
- `dry_run`: 试运行模式（不归档）
- `target_repo`: 目标仓库

## 项目结构

```
build-eye/
├── .github/workflows/
│   └── monitor.yml          # GitHub Actions 工作流
├── scripts/
│   ├── monitor/             # CI 监控模块
│   │   ├── github_client.py # GitHub API 客户端
│   │   ├── fetch_runs.py    # 获取 workflow runs
│   │   ├── collect_metadata.py # 收集元数据
│   │   └── config_loader.py # 配置加载
│   ├── classify/            # 失败分类模块
│   │   ├── classifier.py    # 分类引擎
│   │   ├── code_detector.py # 代码问题检测
│   │   ├── infra_detector.py # 基础设施检测
│   │   └── interference_detector.py # 干扰检测
│   ├── recommend/           # 修复建议模块
│   │   ├── recommender.py   # 建议生成器
│   │   └── templates.py     # 建议模板
│   ├── report/              # 报告生成模块
│   │   ├── generator.py     # 报告生成器
│   │   ├── formatter.py     # 格式化工具
│   │   └── summary.py       # 摘要生成
│   └── archive/             # 报告归档模块
│       ├── archiver.py      # 归档器
│       └── git_client.py    # Git 客户端
├── config/
│   └── config.yaml          # 系统配置
├── templates/
│   └ example_reports.py     # 报告示例
├── tests/                   # 测试目录
├── docs/
│   └ token-setup.md         # Token 配置指南
├── reports/                 # 报告输出目录
└ requirements.txt           # Python 依赖
└ requirements-dev.txt       # 开发依赖
└ README.md                  # 本文档
```

## 配置选项

### config/config.yaml

```yaml
target_repository:
  owner: vllm-project
  repo: vllm-ascend
  url: https://github.com/vllm-project/vllm-ascend
  branch: main
  monitored_workflows:
    - pr_test_full.yaml
    - pr_test_light.yaml

archive_repository:
  owner: winson-00178005
  repo: build-eye
  url: https://github.com/winson-00178005/build-eye.git

monitoring:
  polling_interval_hours: 6
  lookback_hours: 24
```

### 环境变量

- `GITHUB_TOKEN`: GitHub API 访问 token
- `ARCHIVE_TOKEN`: 归档仓库写入 token
- `TARGET_REPO_OWNER`: 目标仓库 owner
- `TARGET_REPO_NAME`: 目标仓库名称

## 报告格式

每个报告包含：

- YAML frontmatter（元数据）
- 概要（1-2句话）
- 根因分析（分类、置信度、推理）
- 证据（匹配模式、链接、日志片段）
- 修复建议（优先建议、详细步骤）
- 相关 PR（仅干扰分类）

报告归档路径: `reports/YYYY/MM/DD/<分类>-pr-<编号>.md`

## 运行测试

```bash
pip install -r requirements-dev.txt
pytest tests/
```

## 扩展 nightly 流水线

系统已设计支持 nightly 流水线监测，只需在配置中添加：

```yaml
target_repository:
  monitored_workflows:
    - schedule_nightly_test_a2.yaml
    - schedule_nightly_test_a3.yaml
```

## 维护和扩展

### 添加新的分类规则

在 `scripts/classify/` 中添加新的检测器：

```python
def detect_new_pattern(log_excerpt: str) -> dict:
    patterns = [...]
    # 实现检测逻辑
```

然后在 `classifier.py` 中调用。

### 添加新的建议模板

在 `scripts/recommend/templates.py` 中添加新模板。

## 许可证

Apache License 2.0 - 详情参见 LICENSE 文件

## 联系方式

问题反馈: https://github.com/winson-00178005/build-eye/issues