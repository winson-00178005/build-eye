---
report_id: c8b56e16
pr_number: null
group_key: run-27491942638
generated_at: 2026-06-14T11:59:27.905129+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27491942638

## 概要

run-27491942638 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#27491942638) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #27491942638)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27491942638)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/27491942638/job/81258662305)

**日志片段**:
```
2026-06-14T07:30:26.7944043Z   token: ***
...
2026-06-14T07:30:26.7944502Z   fail_on_initial_diff_error: false
2026-06-14T07:30:26.7944748Z   fail_on_submodule_diff_error: false
2026-06-14T07:30:26.7944999Z   negation_patterns_first: false
2026-06-14T07:30:26.7945219Z   matrix: false
2026-06-14T07:30:26.7945593Z   exclude_submodules: false
...
2026-06-14T07:30:39.3544095Z Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
2026-06-14T07:30:39.3711389Z Using cached wheel-0.47.0-py3-none-any.whl (
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#27491942638)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-14T11:59:27.905154+00:00
