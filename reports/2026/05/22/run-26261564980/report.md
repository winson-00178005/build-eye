---
report_id: ff9bff21
pr_number: null
group_key: run-26226133718
generated_at: 2026-05-22T03:55:44.684096+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26226133718

## 概要

run-26226133718 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26226133718) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #26226133718)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26226133718)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26226133718/job/77174098171)
[查看 Job: e2e-full (v0.20.2) / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26226133718/job/77174098193)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26226133718/job/77174098221)
[查看 Job: e2e-full (v0.20.2) / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26226133718/job/77174098223)

**日志片段**:
```
2026-05-21T13:00:04.2291518Z   UV_NO_CACHE: 1
2026-05-21T13:00:04.2291708Z   UV_SYSTEM_PYTHON: 1
2026-05-21T13:00:04.2291909Z ##[endgroup]
2026-05-21T13:00:04.2384054Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T13:00:04.2384892Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T13:00:04.2385176Z ##[endgroup]
2026-05-21T13:00:04.6971690Z (node:1418) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26226133718)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T03:55:44.684112+00:00
