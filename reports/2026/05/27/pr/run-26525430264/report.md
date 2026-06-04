---
report_id: e285de3d
pr_number: null
group_key: run-26525430264
generated_at: 2026-05-27T23:21:13.830126+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26525430264

## 概要

run-26525430264 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26525430264) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26525430264)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26525430264)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26525430264/job/78127800132)

**日志片段**:
```
2026-05-27T16:51:12.8672753Z                  nar=num_available_replicas: ([m
2026-05-27T16:51:12.8673693Z                      get_score(_lpt_deployment, X_row, deployed_replicas, ci, crf[mid], ri, rrf[nar - mid])[m
2026-05-27T16:51:12.8674313Z                  ),[m
2026-05-27T16:51:12.9124728Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-27T16:51:12.9186385Z ##[error]Process completed with exit code
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26525430264)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T23:21:13.830153+00:00
