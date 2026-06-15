---
report_id: 1c0de329
pr_number: null
group_key: run-27549637549
generated_at: 2026-06-15T19:51:37.192626+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27549637549

## 概要

run-27549637549 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27549637549) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27549637549)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549)
[查看 Job: e2e-upstream_a2_4 (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549/job/81432363768)
[查看 Job: e2e-upstream_a2_2 (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549/job/81432363815)
[查看 Job: e2e-upstream_singlecard (2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549/job/81432363836)
[查看 Job: e2e-upstream_singlecard (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549/job/81432363881)
[查看 Job: e2e-upstream_singlecard (3)](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549/job/81432363912)
[查看 Job: e2e-upstream_singlecard (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/27549637549/job/81432363936)

**日志片段**:
```
2026-06-15T13:30:23.6001745Z (node:303) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-06-15T13:30:23.6002587Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-15T13:30:24.1202772Z /__w/_temp/eb0475ed-53d7-4cec-ac4f-dcfa1ce6c36c.sh: line 1: npu-smi: command not found
2026-06-15T13:30:24.1349609Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#27549637549)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-15T19:51:37.192659+00:00
