---
report_id: 99f23a6d
pr_number: 9547
group_key: pr-9547
generated_at: 2026-06-28T23:03:21.706109+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9547

## 概要

PR #9547 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28313993852) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28313993852)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9547 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28313993852)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/28313993852/job/83883721069)

**日志片段**:
```
2026-06-28T06:37:35.4823289Z   token: ***
...
2026-06-28T06:37:35.4824017Z   fail_on_initial_diff_error: false
2026-06-28T06:37:35.4824266Z   fail_on_submodule_diff_error: false
2026-06-28T06:37:35.4824521Z   negation_patterns_first: false
2026-06-28T06:37:35.4824944Z   matrix: false
2026-06-28T06:37:35.4825141Z   exclude_submodules: false
...
2026-06-28T06:37:48.1335363Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-28T06:37:55.0214569Z 
2026-06-28T06:37:55.0220757Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28313993852)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-28T23:03:21.706145+00:00
