---
report_id: 90df6e9d
pr_number: null
group_key: run-26895462784
generated_at: 2026-06-03T19:52:17.199926+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26895462784

## 概要

run-26895462784 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26895462784) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26895462784)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26895462784)
[查看 Job: run-selected-tests (v0.20.2) / a3-4card](https://github.com/vllm-project/vllm-ascend/actions/runs/26895462784/job/79335016380)

**日志片段**:
```
2026-06-03T18:19:18.0106749Z [2026-06-03 18:19:18.009707][UC][I] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). [236847,236847][shm_broadcast.py:681,acquire_read]
2026-06-03T18:20:18.0700881Z [2026-06-03 18:20:18.069105][UC][I] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hangi
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26895462784)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-03T19:52:17.199952+00:00
