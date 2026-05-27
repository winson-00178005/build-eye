---
report_id: 1a843fea
pr_number: null
group_key: run-26526658098
generated_at: 2026-05-27T18:33:57.231040+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26526658098

## 概要

run-26526658098 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26526658098) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26526658098)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26526658098)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26526658098/job/78132164905)

**日志片段**:
```
2026-05-27T17:14:35.7911054Z          )[m
2026-05-27T17:14:35.7911257Z  [m
2026-05-27T17:14:35.7911602Z          max_kv_len = max(kv_lens) if kv_lens else 0[m
2026-05-27T17:14:35.8410196Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-27T17:14:35.8464670Z ##[error]Process completed with exit code 1.
2026-05-27T17:14:35.8585099Z ##[error]Executing the custom container implementation failed. Please contac
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26526658098)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T18:33:57.231069+00:00
