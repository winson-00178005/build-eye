---
report_id: 6bd1708c
pr_number: null
group_key: run-36118175314
generated_at: 2026-09-25T19:52:34.316092+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-36118175314

## 概要

run-36118175314 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#36118175314) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #36118175314)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314)
[查看 Job: e2e-upstream_online (0, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017960998)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017961017)
[查看 Job: e2e-upstream_singlecard (1, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017961114)
[查看 Job: e2e-upstream_singlecard (3, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017961146)
[查看 Job: e2e-upstream_singlecard (0, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017961156)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017961171)
[查看 Job: e2e-upstream_singlecard (2, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36118175314/job/108017961214)

**日志片段**:
```
2026-09-25T09:27:27.1155031Z (node:401) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-09-25T09:27:27.1155745Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-09-25T09:27:27.5582301Z /__w/_temp/3bd95f13-b632-46a8-bb36-82ed4d743d7a.sh: line 1: npu-smi: command not found
2026-09-25T09:27:27.5725484Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#36118175314)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-09-25T19:52:34.316123+00:00
