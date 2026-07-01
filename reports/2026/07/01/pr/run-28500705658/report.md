---
report_id: 4d5e4d7e
pr_number: null
group_key: run-28500705658
generated_at: 2026-07-01T08:15:41.958633+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28500705658

## 概要

run-28500705658 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28500705658) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28500705658)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28500705658)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/28500705658/job/84477091160)

**日志片段**:
```
2026-07-01T07:22:43.5082047Z   token: ***
...
2026-07-01T07:22:43.5082611Z   fail_on_initial_diff_error: false
2026-07-01T07:22:43.5083088Z   fail_on_submodule_diff_error: false
2026-07-01T07:22:43.5083362Z   negation_patterns_first: false
2026-07-01T07:22:43.5083617Z   matrix: false
2026-07-01T07:22:43.5083830Z   exclude_submodules: false
...
2026-07-01T07:23:09.1590103Z Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
...
2026-07-01T07:23:13.4153635Z 
2026-07-01T07:23:13.4
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28500705658)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-01T08:15:41.958657+00:00
