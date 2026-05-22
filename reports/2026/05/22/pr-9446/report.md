---
report_id: 450b41d6
pr_number: 9394
group_key: pr-9394
generated_at: 2026-05-22T06:47:34.503414+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9394

## 概要

PR #9394 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | vLLM Main Schedule Test (#26271314173) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. vLLM Main Schedule Test (Run #26271314173)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9394 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173)
[查看 PR #9394](https://github.com/vllm-project/vllm-ascend/pull/9394)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189839)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189849)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189867)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189883)

**日志片段**:
```
2026-05-22T06:18:49.9029998Z   UV_HTTP_TIMEOUT: 120
2026-05-22T06:18:49.9030270Z   UV_NO_CACHE: 1
2026-05-22T06:18:49.9030456Z   UV_SYSTEM_PYTHON: 1
2026-05-22T06:18:49.9030664Z ##[endgroup]
2026-05-22T06:18:49.9127344Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T06:18:49.9128239Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T06:18:49.9128535Z ##[endgroup]
2026-05-22T06:18:50.3643904Z (node:1508) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **vLLM Main Schedule Test (#26271314173)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T06:47:34.503445+00:00
