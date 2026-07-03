---
report_id: 20e960a9
pr_number: null
group_key: run-28637426940
generated_at: 2026-07-03T07:22:39.970500+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28637426940

## 概要

run-28637426940 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28637426940) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28637426940)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28637426940)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/28637426940/job/84926581366)

**日志片段**:
```
2026-07-03T03:59:57.0532067Z   token: ***
...
2026-07-03T03:59:57.0532502Z   fail_on_initial_diff_error: false
2026-07-03T03:59:57.0532743Z   fail_on_submodule_diff_error: false
2026-07-03T03:59:57.0532989Z   negation_patterns_first: false
2026-07-03T03:59:57.0533403Z   matrix: false
2026-07-03T03:59:57.0533593Z   exclude_submodules: false
...
2026-07-03T04:00:09.2849814Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-07-03T04:00:15.9356016Z 
2026-07-03T04:00:15.9363552Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28637426940)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-03T07:22:39.970539+00:00
