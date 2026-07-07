---
report_id: d5b5766d
pr_number: null
group_key: run-28857383715
generated_at: 2026-07-07T23:04:07.361388+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28857383715

## 概要

run-28857383715 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#28857383715) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #28857383715)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28857383715)
[查看 Job: Markdown link check](https://github.com/vllm-project/vllm-ascend/actions/runs/28857383715/job/85587197907)

**日志片段**:
```
2026-07-07T09:53:14.4524802Z ##[endgroup]
2026-07-07T09:53:14.4525342Z ##[group]Fetching the repository
...
2026-07-07T09:55:22.9222360Z ##[error]fatal: unable to access 'https://github.com/vllm-project/vllm-ascend/': Failed to connect to github.com port 443 after 128456 ms: Connection timed out
2026-07-07T09:55:22.9230653Z The process '/usr/bin/git' failed with exit code 128
...
2026-07-07T09:55:37.0238174Z From https://github.com/vllm-project/vllm-ascend
...
2026-07-07T09:55:38.6654456Z   toke
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#28857383715)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-07T23:04:07.361417+00:00
