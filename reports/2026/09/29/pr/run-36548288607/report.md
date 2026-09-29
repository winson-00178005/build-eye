---
report_id: 7cbc7a1d
pr_number: null
group_key: run-36548288607
generated_at: 2026-09-29T10:28:15.564080+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-36548288607

## 概要

run-36548288607 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#36548288607) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #36548288607)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/36548288607)
[查看 Job: e2e-upstream_online (0, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36548288607/job/109341121165)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/36548288607/job/109341121173)
[查看 Job: e2e-upstream_singlecard (3, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36548288607/job/109341121224)
[查看 Job: e2e-upstream_singlecard (1, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/36548288607/job/109341121337)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/36548288607/job/109341121344)

**日志片段**:
```
2026-09-29T09:23:02.8109330Z (node:403) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-09-29T09:23:02.8110001Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-09-29T09:23:03.2738985Z /__w/_temp/50fd33a7-36b8-476b-87dd-c96714a6f0b0.sh: line 1: npu-smi: command not found
2026-09-29T09:23:03.2887353Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#36548288607)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-09-29T10:28:15.564125+00:00
