---
report_id: 56bde93b
pr_number: 10439
group_key: pr-10439
generated_at: 2026-06-13T11:56:39.626577+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 1
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #10439

## 概要

PR #10439 触发了 2 个 workflow，均失败。

- **代码问题**: 1 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27464192927) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27464192914) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #27464192927)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27464192927)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #27464192914)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10439 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27464192914)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27464192914/job/81183559473)

**日志片段**:
```
2026-06-13T10:32:22.6144168Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-13T10:32:23.0598370Z ============================
2026-06-13T10:32:23.0612699Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-06-13T10:32:40.0652305Z ##[error]vllm_ascend/distributed/kv_transfer/kv_pool/ascend_store/config_data.py:160: error: "Callable[[Any], Any | None]" has no attribute "_registry"  [attr-defined]
2026-06-13T10:32:40.0660896Z ##[error]vllm_ascen
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#27464192927)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27464192914)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-13T11:56:39.626618+00:00
