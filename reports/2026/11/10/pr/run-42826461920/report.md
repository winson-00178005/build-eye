---
report_id: f26bc9c1
pr_number: null
group_key: run-42826461920
generated_at: 2026-11-10T21:43:23.007294+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-42826461920

## 概要

run-42826461920 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#42826461920) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #42826461920)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/42826461920)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/42826461920/job/129864960245)

**日志片段**:
```
2026-11-10T13:44:27.9516910Z sh: 1: cd: can't cd to /__w/_temp
2026-11-10T13:44:29.0033841Z cp: cannot stat '/__w/_temp/_github_home': No such file or directory
2026-11-10T13:44:29.0641577Z sh: 0: cannot open /__w/_temp/d05c9330-dd0c-11f1-a52e-012790597a39.sh: No such file
2026-11-10T13:44:29.0694209Z ##[error]Error: failed to run script step:
  â exit code: 2
  â your script exited with a non-zero code; please check your script for errors
----------------------------------------------------
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#42826461920)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-11-10T21:43:23.007319+00:00
