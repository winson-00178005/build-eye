---
report_id: 72fd96ab
pr_number: null
group_key: run-26807140439
generated_at: 2026-06-02T08:33:04.387381+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26807140439

## 概要

run-26807140439 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26807140439) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26807140439)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26807140439)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26807140439/job/79027422485)

**日志片段**:
```
2026-06-02T08:13:03.5408674Z [0;32mRunning mypy for examples on python version: 3.10[0m
2026-06-02T08:13:05.5294155Z Success: no issues found in 28 source files
2026-06-02T08:13:05.5422991Z [0;32mRunning mypy for tests on python version: 3.10[0m
2026-06-02T08:13:07.5560181Z ##[error]tests/ut/conftest.py:56: error: Module has no attribute "npu"  [attr-defined]
2026-06-02T08:13:07.5568992Z ##[error]tests/ut/conftest.py:57: error: Module has no attribute "profiler"  [attr-defined]
2026-06-02T08
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26807140439)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-02T08:33:04.387406+00:00
