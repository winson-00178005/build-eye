---
report_id: f14ac252
pr_number: null
group_key: run-26890445311
generated_at: 2026-06-03T14:31:44.776448+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26890445311

## 概要

run-26890445311 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26890445311) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26890445311)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26890445311)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26890445311/job/79314622786)

**日志片段**:
```
2026-06-03T14:13:06.8969131Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-03T14:13:07.3191578Z ============================
2026-06-03T14:13:07.3203550Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-06-03T14:13:19.0289121Z ##[error]vllm_ascend/spec_decode/llm_base_proposer.py:431: error: Item "None" of "Any | None" has no attribute "sas_metadata"  [union-attr]
2026-06-03T14:13:20.4181934Z Found 1 error in 1 file (checked 385 source fil
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26890445311)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-03T14:31:44.776476+00:00
