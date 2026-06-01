---
report_id: 4d33cc5b
pr_number: null
group_key: run-26744971168
generated_at: 2026-06-01T09:31:01.328521+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26744971168

## 概要

run-26744971168 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26744971168) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26744971168)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26744971168)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26744971168/job/78818229814)

**日志片段**:
```
2026-06-01T08:55:58.9044746Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-01T08:55:59.3134081Z ============================
2026-06-01T08:55:59.3143436Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-06-01T08:56:10.6565403Z ##[error]vllm_ascend/ops/rotary_embedding.py:139: error: Item "None" of "Any | None" has no attribute "modules"  [union-attr]
2026-06-01T08:56:12.1838357Z Found 1 error in 1 file (checked 377 source files)
2026-06-01
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26744971168)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-01T09:31:01.328547+00:00
