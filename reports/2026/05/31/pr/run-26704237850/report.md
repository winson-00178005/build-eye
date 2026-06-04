---
report_id: 623c48a1
pr_number: null
group_key: run-26704237850
generated_at: 2026-05-31T07:48:41.053542+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26704237850

## 概要

run-26704237850 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26704237850) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26704237850)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `ImportError`
- import_error: `ModuleNotFoundError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26704237850)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26704237850/job/78702673289)
[查看 Job: smart test (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26704237850/job/78702673301)

**日志片段**:
```
2026-05-31T05:37:23.8929139Z     Found existing installation: transformers 5.9.0
2026-05-31T05:37:24.0416537Z     Uninstalling transformers-5.9.0:
...
2026-05-31T05:37:30.4941048Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-05-31T05:37:30.4941886Z ms-service-profiler 26.0.0 requires matplotlib, which is not installed.
2026-05-31T05:37:30.4942344Z ms-service-prof
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26704237850)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-31T07:48:41.053566+00:00
