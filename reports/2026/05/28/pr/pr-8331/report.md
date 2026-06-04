---
report_id: b517962e
pr_number: 8331
group_key: pr-8331
generated_at: 2026-05-28T23:19:23.881170+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #8331

## 概要

PR #8331 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26590975931) | PR代码问题 | 高 | 编译错误 |
| 2 | E2E-Full (#26590975735) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26590975931)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #8331 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975931)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975931/job/78349664489)

**日志片段**:
```
2026-05-28T17:31:09.7583196Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-28T17:31:10.1679443Z ============================
2026-05-28T17:31:10.1691100Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-28T17:31:21.6030900Z ##[error]vllm_ascend/ops/gdn.py:24: error: Cannot find implementation or library stub for module named "vllm.model_executor.layers.mamba.gdn_linear_attn"  [import-not-found]
2026-05-28T17:31:21.6039785Z vllm_ascend/o
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Full (Run #26590975735)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error。 问题出现在 PR #8331 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `ModuleNotFoundError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975735)
[查看 Job: e2e-full (7e1b45a09252a5b513cd83116aa7a2f310220c34) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975735/job/78354411732)
[查看 Job: e2e-full (7e1b45a09252a5b513cd83116aa7a2f310220c34) / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975735/job/78354411744)
[查看 Job: e2e-full (7e1b45a09252a5b513cd83116aa7a2f310220c34) / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975735/job/78354411779)
[查看 Job: e2e-full (7e1b45a09252a5b513cd83116aa7a2f310220c34) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26590975735/job/78354411896)

**日志片段**:
```
2026-05-28T17:55:55.5194310Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-28T17:55:55.5194763Z   type: full
2026-05-28T17:55:55.5195364Z   contains_310: false
2026-05-28T17:55:55.5195591Z   continue_on_error: false
2026-05-28T17:55:55.5195816Z   ref: 
2026-05-28T17:55:55.5196016Z   singlecard_tests: 
2026-05-28T17:55:55.5196236Z   multicard_2_tests: 
...
2026-05-28T18:02:51.9215113Z [2026-05-28 18:02:51.920184][UC][I] Initiali
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26590975931)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#26590975735)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-28T23:19:23.881223+00:00
