---
report_id: 0f63fc50
pr_number: null
group_key: run-28232692954
generated_at: 2026-06-26T12:15:01.766867+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28232692954

## 概要

run-28232692954 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28232692954) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28232692954)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28232692954)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/28232692954/job/83640005390)

**日志片段**:
```
2026-06-26T10:35:32.4659506Z   token: ***
...
2026-06-26T10:35:32.4659995Z   fail_on_initial_diff_error: false
2026-06-26T10:35:32.4660266Z   fail_on_submodule_diff_error: false
2026-06-26T10:35:32.4660517Z   negation_patterns_first: false
2026-06-26T10:35:32.4660951Z   matrix: false
2026-06-26T10:35:32.4661149Z   exclude_submodules: false
...
2026-06-26T10:35:44.4727115Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-26T10:35:50.9526610Z 
2026-06-26T10:35:50.9539081Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28232692954)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-26T12:15:01.766879+00:00
