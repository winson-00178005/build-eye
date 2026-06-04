---
report_id: 5f4b3b10
pr_number: null
group_key: run-26834550146
generated_at: 2026-06-02T23:49:25.408841+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26834550146

## 概要

run-26834550146 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26834550146) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26834550146)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `AttributeError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26834550146)
[查看 Job: run-selected-tests (9090368b650896bf5fc990c921df7eb4c20355a5) / a2-1](https://github.com/vllm-project/vllm-ascend/actions/runs/26834550146/job/79125659683)
[查看 Job: run-selected-tests (v0.20.2) / cpu-0](https://github.com/vllm-project/vllm-ascend/actions/runs/26834550146/job/79125659736)
[查看 Job: run-selected-tests (9090368b650896bf5fc990c921df7eb4c20355a5) / cpu-0](https://github.com/vllm-project/vllm-ascend/actions/runs/26834550146/job/79125659790)

**日志片段**:
```
2026-06-02T17:06:51.7685116Z tests/ut/worker/a2/test_worker_v1.py::TestNPUWorker::test_wake_up_mode_enabled [32mPASSED[0m
2026-06-02T17:06:51.7685590Z 
2026-06-02T17:06:51.7685742Z ==================================== ERRORS ====================================
2026-06-02T17:06:51.7686274Z [31m[1m__ ERROR at setup of test_determine_batch_execution_and_padding[decode_eager] __[0m
2026-06-02T17:06:51.7686600Z 
2026-06-02T17:06:51.7686993Z     [0m[37m@pytest[39;49;00m.fixture[90m[39;49;00
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26834550146)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-02T23:49:25.408870+00:00
