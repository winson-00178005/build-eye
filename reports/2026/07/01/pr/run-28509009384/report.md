---
report_id: e401aaf9
pr_number: null
group_key: run-28509009384
generated_at: 2026-07-01T12:36:49.592943+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28509009384

## 概要

run-28509009384 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28509009384) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28509009384)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28509009384)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/28509009384/job/84504433685)

**日志片段**:
```
2026-07-01T09:54:14.8150262Z   token: ***
...
2026-07-01T09:54:14.8150751Z   fail_on_initial_diff_error: false
2026-07-01T09:54:14.8151015Z   fail_on_submodule_diff_error: false
2026-07-01T09:54:14.8151283Z   negation_patterns_first: false
2026-07-01T09:54:14.8151527Z   matrix: false
2026-07-01T09:54:14.8151730Z   exclude_submodules: false
...
2026-07-01T09:54:24.5834213Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
...
2026-07-01T09:54:28.9228373Z 
2026-07-01T09:54:28.9234988Z ERROR: 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28509009384)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-01T12:36:49.592967+00:00
