---
report_id: 11515100
pr_number: null
group_key: run-28497786909
generated_at: 2026-07-01T08:15:41.959883+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28497786909

## 概要

run-28497786909 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28497786909) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28497786909)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28497786909)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/28497786909/job/84467692936)

**日志片段**:
```
2026-07-01T06:19:56.4402341Z   token: ***
...
2026-07-01T06:19:56.4402806Z   fail_on_initial_diff_error: false
2026-07-01T06:19:56.4403062Z   fail_on_submodule_diff_error: false
2026-07-01T06:19:56.4403319Z   negation_patterns_first: false
2026-07-01T06:19:56.4403805Z   matrix: false
2026-07-01T06:19:56.4404004Z   exclude_submodules: false
...
2026-07-01T06:20:05.1113457Z Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
...
2026-07-01T06:20:09.2804064Z 
2026-07-01T06:20:09.2
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28497786909)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-01T08:15:41.959906+00:00
