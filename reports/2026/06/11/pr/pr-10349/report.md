---
report_id: ae86c84c
pr_number: 10349
group_key: pr-10349
generated_at: 2026-06-11T14:02:37.462868+00:00
overall_classification: code
total_failed_workflows: 6
category_counts:
  code: 2
  infrastructure: 4
  interference: 0
---

# 构建失败报告: PR #10349

## 概要

PR #10349 触发了 6 个 workflow，均失败。

- **代码问题**: 2 次
- **基础设施问题**: 4 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27351087704) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27351087924) | PR代码问题 | 中 | 编译错误 |
| 3 | E2E-Full (#27350617848) | 基础设施问题 | 低 | 无失败job信息 |
| 4 | E2E-Light (#27350617824) | PR代码问题 | 中 | 编译错误 |
| 5 | E2E-Full (#27346031187) | 基础设施问题 | 低 | 无失败job信息 |
| 6 | E2E-Light (#27346031186) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. E2E-Full (Run #27351087704)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27351087704)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #27351087924)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27351087924)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/27351087924/job/80812866612)

**日志片段**:
```
2026-06-11T13:42:57.6132045Z ##[group]Run '/home/runner/k8s/index.js'
2026-06-11T13:42:57.6141170Z shell: /home/runner/externals/node20/bin/node {0}
2026-06-11T13:42:57.6142397Z ##[endgroup]
2026-06-11T13:43:05.3140875Z ##[error]Error: pod failed to come online with error: Error: Pod linux-amd64-cpu-8-hk-frp8k-runner-jtnzs-workflow is unhealthy with phase status Failed: {}
2026-06-11T13:43:05.3227372Z ##[error]Process completed with exit code 1.
2026-06-11T13:43:05.3268642Z ##[error]Executing th
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Full (Run #27350617848)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27350617848)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 4. E2E-Light (Run #27350617824)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27350617824)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/27350617824/job/80811174123)

**日志片段**:
```
2026-06-11T13:35:10.2515638Z ##[group]Run '/home/runner/k8s/index.js'
2026-06-11T13:35:10.2524885Z shell: /home/runner/externals/node20/bin/node {0}
2026-06-11T13:35:10.2526055Z ##[endgroup]
2026-06-11T13:35:25.9377598Z ##[error]Error: pod failed to come online with error: Error: Pod linux-amd64-cpu-8-hk-frp8k-runner-ddhbt-workflow is unhealthy with phase status Failed: {}
2026-06-11T13:35:25.9436085Z ##[error]Process completed with exit code 1.
2026-06-11T13:35:25.9475391Z ##[error]Executing th
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. E2E-Full (Run #27346031187)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27346031187)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 6. E2E-Light (Run #27346031186)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27346031186)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#27351087704)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27351087924)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#27350617848)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27350617824)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#27346031187)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27346031186)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-06-11T14:02:37.462979+00:00
