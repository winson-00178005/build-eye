---
report_id: c12a7570
pr_number: null
group_key: run-27295074701
generated_at: 2026-06-10T18:34:05.226021+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27295074701

## 概要

run-27295074701 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#27295074701) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #27295074701)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27295074701)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/27295074701/job/80625505132)

**日志片段**:
```
2026-06-10T17:50:15.0672024Z   token: ***
...
2026-06-10T17:50:15.0672508Z   fail_on_initial_diff_error: false
2026-06-10T17:50:15.0672776Z   fail_on_submodule_diff_error: false
2026-06-10T17:50:15.0673038Z   negation_patterns_first: false
2026-06-10T17:50:15.0673267Z   matrix: false
2026-06-10T17:50:15.0673988Z   exclude_submodules: false
...
2026-06-10T17:50:26.5213460Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-10T17:50:32.8905975Z 
2026-06-10T17:50:32.8911532Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#27295074701)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-10T18:34:05.226078+00:00
