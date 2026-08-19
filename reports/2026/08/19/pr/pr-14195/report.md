---
report_id: bce62730
pr_number: 14195
group_key: pr-14195
generated_at: 2026-08-19T04:38:09.277550+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #14195

## 概要

PR #14195 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#32206073025) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #32206073025)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #14195 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/32206073025)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/32206073025/job/95929504640)

**日志片段**:
```
2026-08-19T01:47:38.6937340Z   token: ***
...
2026-08-19T01:47:38.6937884Z   fail_on_initial_diff_error: false
2026-08-19T01:47:38.6938296Z   fail_on_submodule_diff_error: false
2026-08-19T01:47:38.6938551Z   negation_patterns_first: false
2026-08-19T01:47:38.6938779Z   matrix: false
2026-08-19T01:47:38.6938975Z   exclude_submodules: false
...
2026-08-19T01:47:52.6685210Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
...
2026-08-19T01:47:59.4965886Z 
2026-08-19T01:47:59.4973011Z ERROR: 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#32206073025)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-08-19T04:38:09.277605+00:00
