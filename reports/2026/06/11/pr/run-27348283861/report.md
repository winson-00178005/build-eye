---
report_id: 48566b96
pr_number: null
group_key: run-27348283861
generated_at: 2026-06-11T14:02:37.464036+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27348283861

## 概要

run-27348283861 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27348283861) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27348283861)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27348283861)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/27348283861/job/80802906399)

**日志片段**:
```
2026-06-11T12:56:34.4349027Z ##[group]Run '/home/runner/k8s/index.js'
2026-06-11T12:56:34.4358313Z shell: /home/runner/externals/node20/bin/node {0}
2026-06-11T12:56:34.4359698Z ##[endgroup]
2026-06-11T12:56:50.0685900Z ##[error]Error: pod failed to come online with error: Error: Pod linux-amd64-cpu-8-hk-frp8k-runner-7c268-workflow is unhealthy with phase status Failed: {}
2026-06-11T12:56:50.0751827Z ##[error]Process completed with exit code 1.
2026-06-11T12:56:50.0790801Z ##[error]Executing th
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27348283861)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-11T14:02:37.464058+00:00
