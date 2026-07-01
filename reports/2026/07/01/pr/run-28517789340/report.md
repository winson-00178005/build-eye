---
report_id: 5417e8dc
pr_number: null
group_key: run-28517789340
generated_at: 2026-07-01T17:57:39.723815+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28517789340

## 概要

run-28517789340 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28517789340) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28517789340)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28517789340)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/28517789340/job/84533788971)

**日志片段**:
```
2026-07-01T12:34:38.8775881Z   token: ***
...
2026-07-01T12:34:38.8776401Z   fail_on_initial_diff_error: false
2026-07-01T12:34:38.8776653Z   fail_on_submodule_diff_error: false
2026-07-01T12:34:38.8776903Z   negation_patterns_first: false
2026-07-01T12:34:38.8777134Z   matrix: false
2026-07-01T12:34:38.8777336Z   exclude_submodules: false
...
2026-07-01T12:34:48.6419225Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
...
2026-07-01T12:34:53.1451196Z 
2026-07-01T12:34:53.1459216Z ERROR: 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28517789340)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-01T17:57:39.723836+00:00
