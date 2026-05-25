---
report_id: 823f0df7
pr_number: 9449
group_key: pr-9449
generated_at: 2026-05-25T19:41:29.359503+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9449

## 概要

PR #9449 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#26399894622) | PR代码问题 | 中 | 编译错误 |
| 2 | E2E-Light (#26399894794) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #26399894622)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9449 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26399894622)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/26399894622/job/77709396599)

**日志片段**:
```
2026-05-25T12:19:59.8040978Z [2K[01mreading sources... [39;49;00m[ 92%] [35muser_guide/feature_guide/sequence_parallelism[39;49;00m
2026-05-25T12:19:59.8127908Z [2K[01mreading sources... [39;49;00m[ 93%] [35muser_guide/feature_guide/sleep_mode[39;49;00m
2026-05-25T12:19:59.8275650Z [2K[01mreading sources... [39;49;00m[ 94%] [35muser_guide/feature_guide/speculative_decoding[39;49;00m
2026-05-25T12:19:59.8326805Z [2K[01mreading sources... [39;49;00m[ 94%] [35muser_guide/feature_
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Light (Run #26399894794)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9449 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26399894794)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/26399894794/job/77709397118)

**日志片段**:
```
ï»¿2026-05-25T12:14:25.0545429Z Current runner version: '2.334.0'
2026-05-25T12:14:25.0551859Z Runner name: 'linux-amd64-cpu-8-hk-frp8k-runner-8xg99'
2026-05-25T12:14:25.0552680Z Runner group name: 'Default'
2026-05-25T12:14:25.0553857Z Machine name: 'linux-amd64-cpu-8-hk-frp8k-runner-8xg99'
2026-05-25T12:14:25.0556530Z ##[group]GITHUB_TOKEN Permissions
2026-05-25T12:14:25.0559006Z Contents: read
2026-05-25T12:14:25.0559538Z Metadata: read
2026-05-25T12:14:25.0559992Z ##[endgroup]
2026-05-25T12:
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#26399894622)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26399894794)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T19:41:29.359527+00:00
