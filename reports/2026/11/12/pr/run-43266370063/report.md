---
report_id: b9c3fc9b
pr_number: null
group_key: run-43266370063
generated_at: 2026-11-12T22:06:20.767011+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-43266370063

## 概要

run-43266370063 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#43266370063) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #43266370063)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/43266370063)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/43266370063/job/131350904080)

**日志片段**:
```
2026-11-12T17:10:22.1072720Z   token: ***
...
2026-11-12T17:10:22.1073705Z   fail_on_initial_diff_error: false
2026-11-12T17:10:22.1074213Z   fail_on_submodule_diff_error: false
2026-11-12T17:10:22.1074672Z   negation_patterns_first: false
2026-11-12T17:10:22.1075095Z   matrix: false
2026-11-12T17:10:22.1075532Z   exclude_submodules: false
...
2026-11-12T17:10:34.3870090Z     Result: broken - HTTP 404
2026-11-12T17:10:34.3870498Z     Sources: docs/source/user_guide/feature_guide/sleep_mode.md
20
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#43266370063)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-11-12T22:06:20.767032+00:00
