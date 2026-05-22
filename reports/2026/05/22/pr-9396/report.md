---
report_id: 759cccec
pr_number: null
group_key: run-26261565025
generated_at: 2026-05-22T03:10:53.556662+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26261565025

## 概要

run-26261565025 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26261565025) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #26261565025)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025)
[查看 Job: e2e-full (0d4d334eaa583b9c09aa4eb7538c22db99fd84b3) / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140195)
[查看 Job: e2e-full (0d4d334eaa583b9c09aa4eb7538c22db99fd84b3) / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140197)
[查看 Job: e2e-full (0d4d334eaa583b9c09aa4eb7538c22db99fd84b3) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140199)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140219)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140225)
[查看 Job: e2e-full (v0.20.2) / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140234)
[查看 Job: e2e-full (v0.20.2) / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26261565025/job/77296140242)

**日志片段**:
```
2026-05-22T00:59:05.8434379Z   UV_HTTP_TIMEOUT: 120
2026-05-22T00:59:05.8434681Z   UV_NO_CACHE: 1
2026-05-22T00:59:05.8434915Z   UV_SYSTEM_PYTHON: 1
2026-05-22T00:59:05.8435182Z ##[endgroup]
2026-05-22T00:59:05.8527942Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T00:59:05.8529032Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T00:59:05.8529398Z ##[endgroup]
2026-05-22T00:59:06.3390795Z (node:1528) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26261565025)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T03:10:53.556688+00:00
