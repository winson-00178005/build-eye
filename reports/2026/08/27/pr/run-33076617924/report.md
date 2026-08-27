---
report_id: decd088b
pr_number: null
group_key: run-33076617924
generated_at: 2026-08-27T15:03:00.575561+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-33076617924

## 概要

run-33076617924 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#33076617924) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #33076617924)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/33076617924)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/33076617924/job/98532357346)

**日志片段**:
```
2026-08-27T13:24:49.2572061Z   token: ***
...
2026-08-27T13:24:49.2572530Z   fail_on_initial_diff_error: false
2026-08-27T13:24:49.2572784Z   fail_on_submodule_diff_error: false
2026-08-27T13:24:49.2573036Z   negation_patterns_first: false
2026-08-27T13:24:49.2573262Z   matrix: false
2026-08-27T13:24:49.2573455Z   exclude_submodules: false
...
2026-08-27T13:24:57.2818843Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
...
2026-08-27T13:25:03.8859419Z 
2026-08-27T13:25:03.8865704Z ERROR: 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#33076617924)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-08-27T15:03:00.575595+00:00
