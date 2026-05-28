---
report_id: 3bc5ed48
pr_number: null
group_key: run-26575244573
generated_at: 2026-05-28T13:54:07.146165+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26575244573

## 概要

run-26575244573 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26575244573) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26575244573)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `ImportError`
- import_error: `AttributeError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26575244573)
[查看 Job: smart test (7e1b45a09252a5b513cd83116aa7a2f310220c34) / smart-ut (a2 x1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26575244573/job/78293390394)
[查看 Job: smart test (7e1b45a09252a5b513cd83116aa7a2f310220c34) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26575244573/job/78293390397)

**日志片段**:
```
2026-05-28T13:09:20.4140686Z     [32m-[0m tests/ut/ops/test_gdn_chunk_meta.py::test_chunk_gated_delta_rule_fwd_threads_prebuilt_chunk_offsets
2026-05-28T13:09:20.4141712Z     [32m-[0m tests/ut/worker/test_model_runner_v1_with_device.py::test_determine_batch_execution_and_padding
2026-05-28T13:09:20.4142251Z [1;34m====================[0m
2026-05-28T13:09:58.0033382Z ImportError while loading conftest '/__w/vllm-ascend/vllm-ascend/tests/ut/conftest.py'.
2026-05-28T13:09:58.1546079Z tests/ut/
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26575244573)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-28T13:54:07.146187+00:00
