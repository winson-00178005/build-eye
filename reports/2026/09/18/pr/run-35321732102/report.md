---
report_id: 05270d03
pr_number: null
group_key: run-35321732102
generated_at: 2026-09-18T08:49:07.579484+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-35321732102

## 概要

run-35321732102 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#35321732102) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #35321732102)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/35321732102)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/35321732102/job/105525518395)

**日志片段**:
```
2026-09-18T07:56:07.3802310Z   token: ***
...
2026-09-18T07:56:07.3802950Z   fail_on_initial_diff_error: false
2026-09-18T07:56:07.3803295Z   fail_on_submodule_diff_error: false
2026-09-18T07:56:07.3803644Z   negation_patterns_first: false
2026-09-18T07:56:07.3803953Z   matrix: false
2026-09-18T07:56:07.3804418Z   exclude_submodules: false
...
2026-09-18T07:56:14.8946788Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
...
2026-09-18T07:56:19.7601500Z 
2026-09-18T07:56:19.7608273Z ERROR: 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#35321732102)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-09-18T08:49:07.579507+00:00
