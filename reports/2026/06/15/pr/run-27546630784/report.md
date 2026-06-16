---
report_id: 4c1e5200
pr_number: null
group_key: run-27546630784
generated_at: 2026-06-15T23:49:27.189543+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27546630784

## 概要

run-27546630784 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27546630784) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27546630784)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27546630784)
[查看 Job: e2e-upstream_a2_2 (0, v0.21.0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27546630784/job/81421597191)
[查看 Job: e2e-upstream_singlecard (2, v0.21.0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27546630784/job/81421597196)
[查看 Job: e2e-upstream_a2_4 (0, v0.21.0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27546630784/job/81421597203)
[查看 Job: e2e-upstream_singlecard (1, v0.21.0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27546630784/job/81421597276)
[查看 Job: e2e-upstream_singlecard (3, v0.21.0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27546630784/job/81421597323)

**日志片段**:
```
2026-06-15T12:36:40.9638923Z (node:236) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-06-15T12:36:41.2078954Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-15T12:36:41.4524454Z /__w/_temp/2e63e64b-73b4-4798-ac4d-e972e3fa7847.sh: line 1: npu-smi: command not found
2026-06-15T12:36:41.4710642Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#27546630784)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-15T23:49:27.189571+00:00
