---
report_id: 5991929d
pr_number: null
group_key: run-36121018458
generated_at: 2026-09-25T19:52:34.315944+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-36121018458

## 概要

run-36121018458 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#36121018458) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #36121018458)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458)
[查看 Job: e2e-upstream_online (0, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458/job/108027514383)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458/job/108027514418)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458/job/108027514440)
[查看 Job: e2e-upstream_singlecard (1, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458/job/108027514458)
[查看 Job: e2e-upstream_singlecard (3, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458/job/108027514500)
[查看 Job: e2e-upstream_singlecard (2, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36121018458/job/108027514547)

**日志片段**:
```
2026-09-25T09:59:23.2803899Z (node:402) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-09-25T09:59:23.2804683Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-09-25T09:59:23.6357954Z /__w/_temp/6a32a16b-569e-43cf-ae01-34c04a27c95d.sh: line 1: npu-smi: command not found
2026-09-25T09:59:23.6413561Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#36121018458)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-09-25T19:52:34.315975+00:00
