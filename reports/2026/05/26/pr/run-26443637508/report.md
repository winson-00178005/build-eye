---
report_id: dadbe25d
pr_number: null
group_key: run-26443637508
generated_at: 2026-05-26T09:58:18.454472+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26443637508

## 概要

run-26443637508 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26443637508) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26443637508)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26443637508)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26443637508/job/77844350458)

**日志片段**:
```
2026-05-26T09:21:44.0992938Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-26T09:21:44.5505405Z ============================
2026-05-26T09:21:44.5506679Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-26T09:21:56.1368446Z ##[error]vllm_ascend/attention/dsa_v1.py:2595: error: Unsupported operand types for + ("int" and "None")  [operator]
2026-05-26T09:21:56.1376568Z vllm_ascend/attention/dsa_v1.py:2595: note: Right operand is of type "
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26443637508)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-26T09:58:18.454505+00:00
