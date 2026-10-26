---
report_id: 19cdb231
pr_number: null
group_key: run-40300610761
generated_at: 2026-10-26T09:47:05.272182+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-40300610761

## 概要

run-40300610761 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#40300610761) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. Docs link check (Run #40300610761)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `AssertionError`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/40300610761)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/40300610761/job/121497266154)

**日志片段**:
```
2026-10-26T09:35:43.4113313Z   token: ***
...
2026-10-26T09:35:43.4113837Z   fail_on_initial_diff_error: false
2026-10-26T09:35:43.4114109Z   fail_on_submodule_diff_error: false
2026-10-26T09:35:43.4114377Z   negation_patterns_first: false
2026-10-26T09:35:43.4114644Z   matrix: false
2026-10-26T09:35:43.4114928Z   exclude_submodules: false
...
2026-10-26T09:35:50.0576144Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
2026-10-26T09:35:50.0677558Z Using cached tzdata-2026.5-py2.py3-none-a
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#40300610761)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-10-26T09:47:05.272210+00:00
