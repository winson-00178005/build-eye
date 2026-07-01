---
report_id: 963ed231
pr_number: null
group_key: run-28516791872
generated_at: 2026-07-01T17:57:39.724037+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28516791872

## 概要

run-28516791872 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28516791872) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28516791872)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28516791872)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/28516791872/job/84530423253)

**日志片段**:
```
2026-07-01T12:17:32.4136029Z   token: ***
...
2026-07-01T12:17:32.4136507Z   fail_on_initial_diff_error: false
2026-07-01T12:17:32.4136769Z   fail_on_submodule_diff_error: false
2026-07-01T12:17:32.4137021Z   negation_patterns_first: false
2026-07-01T12:17:32.4137246Z   matrix: false
2026-07-01T12:17:32.4137441Z   exclude_submodules: false
...
2026-07-01T12:17:42.2142316Z Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
...
2026-07-01T12:17:46.5978852Z 
2026-07-01T12:17:46.5985082Z ERROR: 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28516791872)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-01T17:57:39.724060+00:00
