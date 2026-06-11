---
report_id: a9cca80a
pr_number: null
group_key: run-27348521537
generated_at: 2026-06-11T14:02:37.463796+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27348521537

## 概要

run-27348521537 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27348521537) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27348521537)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27348521537)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/27348521537/job/80803643823)

**日志片段**:
```
2026-06-11T13:00:08.6024335Z ##[group]Run '/home/runner/k8s/index.js'
2026-06-11T13:00:08.6033369Z shell: /home/runner/externals/node20/bin/node {0}
2026-06-11T13:00:08.6034543Z ##[endgroup]
2026-06-11T13:00:24.2757813Z ##[error]Error: pod failed to come online with error: Error: Pod linux-amd64-cpu-8-hk-frp8k-runner-dpmc8-workflow is unhealthy with phase status Failed: {}
2026-06-11T13:00:24.2826835Z ##[error]Process completed with exit code 1.
2026-06-11T13:00:24.2866193Z ##[error]Executing th
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27348521537)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-11T14:02:37.463819+00:00
