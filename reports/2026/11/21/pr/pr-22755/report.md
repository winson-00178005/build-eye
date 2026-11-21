---
report_id: 1f835dc6
pr_number: 22755
group_key: pr-22755
generated_at: 2026-11-21T21:30:24.403388+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #22755

## 概要

PR #22755 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#44909781598) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #44909781598)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #22755 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/44909781598)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/44909781598/job/136862956377)

**日志片段**:
```
2026-11-21T13:38:15.2556565Z   token: ***
...
2026-11-21T13:38:15.2557547Z   fail_on_initial_diff_error: false
2026-11-21T13:38:15.2558024Z   fail_on_submodule_diff_error: false
2026-11-21T13:38:15.2558519Z   negation_patterns_first: false
2026-11-21T13:38:15.2558961Z   matrix: false
2026-11-21T13:38:15.2559270Z   exclude_submodules: false
...
2026-11-21T13:38:28.9504208Z     Result: broken - HTTP 404
2026-11-21T13:38:28.9504694Z     Sources: docs/source/user_guide/configuration/additional_confi
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#44909781598)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-11-21T21:30:24.403418+00:00
