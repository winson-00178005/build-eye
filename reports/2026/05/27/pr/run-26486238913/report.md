---
report_id: b973d56e
pr_number: null
group_key: run-26486238913
generated_at: 2026-05-27T03:28:41.238196+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26486238913

## 概要

run-26486238913 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#26486238913) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #26486238913)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26486238913)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/26486238913/job/77994212470)

**日志片段**:
```
2026-05-27T02:02:07.8318575Z   token: ***
...
2026-05-27T02:02:07.8318978Z   fail_on_initial_diff_error: false
2026-05-27T02:02:07.8319203Z   fail_on_submodule_diff_error: false
2026-05-27T02:02:07.8319434Z   negation_patterns_first: false
2026-05-27T02:02:07.8319629Z   matrix: false
2026-05-27T02:02:07.8319802Z   exclude_submodules: false
...
2026-05-27T02:02:20.3192622Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-05-27T02:02:25.5575052Z 
2026-05-27T02:02:25.5584346Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#26486238913)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T03:28:41.238218+00:00
