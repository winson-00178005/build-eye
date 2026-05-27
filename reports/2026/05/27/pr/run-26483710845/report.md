---
report_id: 0f776673
pr_number: null
group_key: run-26483710845
generated_at: 2026-05-27T01:42:17.894770+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26483710845

## 概要

run-26483710845 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26483710845) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26483710845)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26483710845)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26483710845/job/77986514735)

**日志片段**:
```
2026-05-27T00:46:24.6748611Z [0;32mRunning mypy for examples on python version: 3.10[0m
2026-05-27T00:46:26.5956425Z Success: no issues found in 28 source files
2026-05-27T00:46:26.6071642Z [0;32mRunning mypy for tests on python version: 3.10[0m
2026-05-27T00:46:29.1298149Z ##[error]tests/ut/patch/worker/test_patch_minimax_m2_linear_attn.py:27: error: Module has no attribute "npu"  [attr-defined]
2026-05-27T00:46:29.1305771Z ##[error]tests/ut/patch/worker/test_patch_minimax_m2_linear_attn.py
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26483710845)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T01:42:17.894797+00:00
