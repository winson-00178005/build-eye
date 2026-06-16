---
report_id: 8105991e
pr_number: null
group_key: run-27602650912
generated_at: 2026-06-16T09:30:40.046344+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27602650912

## 概要

run-27602650912 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27602650912) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27602650912)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912)
[查看 Job: e2e-upstream_online (0, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912/job/81608812076)
[查看 Job: e2e-upstream_multicard (0, 9.0.0-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912/job/81608812095)
[查看 Job: e2e-upstream_singlecard (3, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912/job/81608812111)
[查看 Job: e2e-upstream_singlecard (1, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912/job/81608812114)
[查看 Job: e2e-upstream_singlecard (2, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912/job/81608812149)
[查看 Job: e2e-upstream_multicard (0, 9.0.0-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/27602650912/job/81608812346)

**日志片段**:
```
2026-06-16T08:02:52.1116851Z (node:457) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-06-16T08:02:52.1118508Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-16T08:02:52.5577125Z /__w/_temp/c1b71978-b0f8-410d-9daa-e2fd170a0bc1.sh: line 1: npu-smi: command not found
2026-06-16T08:02:52.5728436Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#27602650912)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-16T09:30:40.046363+00:00
