---
report_id: 62b24e1e
pr_number: null
group_key: run-27534602776
generated_at: 2026-06-15T10:27:17.186114+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27534602776

## 概要

run-27534602776 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27534602776) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27534602776)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27534602776)
[查看 Job: e2e-upstream (linux-aarch64-a2b3-1, 0, 1, 2, 3, true, 4, e2e-upstream_singlecard_online, 23, uv p...](https://github.com/vllm-project/vllm-ascend/actions/runs/27534602776/job/81380885573)
[查看 Job: e2e-upstream (linux-aarch64-a2b3-1, 0, 1, 2, 3, false, 4, e2e-upstream_singlecard, 23, pip instal...](https://github.com/vllm-project/vllm-ascend/actions/runs/27534602776/job/81380885578)

**日志片段**:
```
2026-06-15T09:30:21.4913915Z                     [--auto-partition-id ID] [--auto-partition-size N]
2026-06-15T09:30:21.4915634Z                     [--auto-upgrade-estimated-times] [--continue-on-error]
2026-06-15T09:30:21.4916449Z                     [--timing-report-json TIMING_REPORT_JSON]
2026-06-15T09:30:21.4917351Z run_suite.py: error: argument --auto-partition-id: invalid int value: 'Array'
2026-06-15T09:30:21.5454350Z ##[error]Error: failed to run script step: Error: command terminated 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#27534602776)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-15T10:27:17.186148+00:00
