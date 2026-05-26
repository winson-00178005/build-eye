---
report_id: 6d4a562f
pr_number: 9567
group_key: pr-9567
generated_at: 2026-05-26T09:58:18.454653+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9567

## 概要

PR #9567 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26443505544) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26443505544)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9567 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26443505544)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26443505544/job/77843848484)

**日志片段**:
```
2026-05-26T09:18:36.5019991Z          features.append("async_scheduling")[m
2026-05-26T09:18:36.5020458Z      if "--enable-expert-parallel" in cmd_list:[m
2026-05-26T09:18:36.5020881Z          features.append("expert_parallel")[m
2026-05-26T09:18:36.5207137Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-26T09:18:36.5330420Z ##[error]Process completed with exit code 1.
2026-05-26T09:18:36.5432112Z ##[er
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26443505544)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-26T09:58:18.454680+00:00
