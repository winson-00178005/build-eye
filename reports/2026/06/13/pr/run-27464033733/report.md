---
report_id: 371d49d9
pr_number: null
group_key: run-27464033733
generated_at: 2026-06-13T11:56:39.627089+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27464033733

## 概要

run-27464033733 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27464033733) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27464033733)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27464033733)
[查看 Job: unit test (v0.18.0) / unit test](https://github.com/vllm-project/vllm-ascend/actions/runs/27464033733/job/81183210447)

**日志片段**:
```
2026-06-13T10:28:34.5513736Z   ERROR: Could not install packages due to an OSError.
2026-06-13T10:28:34.5514118Z   Traceback (most recent call last):
2026-06-13T10:28:34.5514668Z     File "/usr/local/python3.11.15/lib/python3.11/site-packages/pip/_vendor/urllib3/connection.py", line 204, in _new_conn
2026-06-13T10:28:34.5515185Z       sock = connection.create_connection(
2026-06-13T10:28:34.5515448Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
...
2026-06-13T10:28:34.5516491Z       raise err
2026-
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27464033733)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-13T11:56:39.627111+00:00
