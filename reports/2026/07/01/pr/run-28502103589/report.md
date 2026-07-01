---
report_id: 809852c9
pr_number: null
group_key: run-28502103589
generated_at: 2026-07-01T08:15:41.958258+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28502103589

## 概要

run-28502103589 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28502103589) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28502103589)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28502103589)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/28502103589/job/84481614014)

**日志片段**:
```
2026-07-01T07:49:57.8631069Z   token: ***
...
2026-07-01T07:49:57.8631534Z   fail_on_initial_diff_error: false
2026-07-01T07:49:57.8631793Z   fail_on_submodule_diff_error: false
2026-07-01T07:49:57.8632049Z   negation_patterns_first: false
2026-07-01T07:49:57.8632324Z   matrix: false
2026-07-01T07:49:57.8632521Z   exclude_submodules: false
...
2026-07-01T07:50:23.4666789Z Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
...
2026-07-01T07:50:27.7271198Z 
2026-07-01T07:50:27.7
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28502103589)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-01T08:15:41.958293+00:00
