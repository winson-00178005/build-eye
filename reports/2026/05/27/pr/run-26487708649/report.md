---
report_id: ed3b48bb
pr_number: null
group_key: run-26487708649
generated_at: 2026-05-27T05:14:43.377076+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26487708649

## 概要

run-26487708649 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26487708649) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26487708649)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26487708649)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26487708649/job/77998657286)

**日志片段**:
```
2026-05-27T02:51:16.6080361Z [0;32mRunning mypy for examples on python version: 3.10[0m
2026-05-27T02:51:18.4839048Z Success: no issues found in 28 source files
2026-05-27T02:51:18.4918890Z [0;32mRunning mypy for tests on python version: 3.10[0m
2026-05-27T02:51:21.0616058Z ##[error]tests/ut/patch/worker/test_patch_minimax_m2_linear_attn.py:49: error: Module has no attribute "HAS_TRITON"  [attr-defined]
2026-05-27T02:51:21.0695906Z ##[error]tests/ut/patch/worker/test_patch_gqa_c8.py:49: erro
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26487708649)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T05:14:43.377096+00:00
