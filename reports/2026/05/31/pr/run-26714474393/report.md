---
report_id: 69d15438
pr_number: null
group_key: run-26714474393
generated_at: 2026-05-31T17:08:02.446540+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26714474393

## 概要

run-26714474393 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26714474393) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26714474393)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26714474393)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26714474393/job/78730533103)

**日志片段**:
```
2026-05-31T13:54:24.3903352Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-31T13:54:24.7842549Z ============================
2026-05-31T13:54:24.7853096Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-31T13:54:36.8864601Z ##[error]vllm_ascend/spec_decode/llm_base_proposer.py:134: error: Cannot determine type of "hidden_size"  [has-type]
2026-05-31T13:54:36.8872663Z ##[error]vllm_ascend/spec_decode/llm_base_proposer.py:478: error: Cann
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26714474393)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-31T17:08:02.446568+00:00
