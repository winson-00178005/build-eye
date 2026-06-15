---
report_id: c29f537e
pr_number: null
group_key: run-27538823854
generated_at: 2026-06-15T19:51:37.193767+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27538823854

## 概要

run-27538823854 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27538823854) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27538823854)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854)
[查看 Job: e2e-upstream_a2_2 (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854/job/81395073933)
[查看 Job: e2e-upstream_singlecard (3)](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854/job/81395074013)
[查看 Job: e2e-upstream_a2_4 (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854/job/81395074014)
[查看 Job: e2e-upstream_singlecard (2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854/job/81395074078)
[查看 Job: e2e-upstream_singlecard (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854/job/81395074094)
[查看 Job: e2e-upstream_singlecard (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27538823854/job/81395074246)

**日志片段**:
```
2026-06-15T10:05:21.1076016Z (node:306) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-06-15T10:05:21.1076878Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-15T10:05:21.5871598Z /__w/_temp/9bae3e47-e637-454a-abf8-c91199dd6e3f.sh: line 1: npu-smi: command not found
2026-06-15T10:05:21.6068979Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#27538823854)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-15T19:51:37.193794+00:00
