---
report_id: 65ec1077
pr_number: null
group_key: run-26806809204
generated_at: 2026-06-02T08:33:04.388488+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26806809204

## 概要

run-26806809204 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26806809204) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26806809204)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26806809204)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26806809204/job/79026372037)

**日志片段**:
```
2026-06-02T08:06:31.1044113Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-02T08:06:31.5427917Z ============================
2026-06-02T08:06:31.5438944Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-06-02T08:06:42.7585489Z ##[error]vllm_ascend/device/device_op.py:312: error: "BaseDeviceAdaptor" has no attribute "W_UK_T"  [attr-defined]
2026-06-02T08:06:42.7593902Z ##[error]vllm_ascend/device/device_op.py:317: error: "BaseDeviceAdaptor"
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26806809204)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-02T08:33:04.388509+00:00
