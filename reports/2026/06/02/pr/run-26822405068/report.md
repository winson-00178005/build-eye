---
report_id: 9c260c83
pr_number: null
group_key: run-26822405068
generated_at: 2026-06-02T14:06:32.876343+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26822405068

## 概要

run-26822405068 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26822405068) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26822405068)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26822405068)
[查看 Job: run-selected-tests (9090368b650896bf5fc990c921df7eb4c20355a5) / cpu-0](https://github.com/vllm-project/vllm-ascend/actions/runs/26822405068/job/79081936408)
[查看 Job: run-selected-tests (v0.20.2) / cpu-0](https://github.com/vllm-project/vllm-ascend/actions/runs/26822405068/job/79081936544)

**日志片段**:
```
2026-06-02T13:32:46.6668627Z     Uninstalling transformers-5.9.0:
...
2026-06-02T13:32:53.1284426Z 
2026-06-02T13:32:53.1295936Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-06-02T13:32:53.1297401Z ms-service-profiler 26.0.0 requires matplotlib, which is not installed.
2026-06-02T13:32:53.1297933Z ms-service-profiler 26.0.0 requires msguard, which is not installe
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26822405068)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-02T14:06:32.876365+00:00
