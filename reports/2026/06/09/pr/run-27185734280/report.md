---
report_id: af4c180c
pr_number: null
group_key: run-27185734280
generated_at: 2026-06-09T07:50:59.285098+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27185734280

## 概要

run-27185734280 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27185734280) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27185734280)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27185734280)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27185734280/job/80254135658)

**日志片段**:
```
2026-06-09T05:33:38.8765057Z  M = TypeVar("M", bound=AscendSFAMetadata)[m
2026-06-09T05:33:38.8765335Z  [m
2026-06-09T05:33:38.8765508Z  [m
2026-06-09T05:33:38.9243009Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-09T05:33:38.9295002Z ##[error]Process completed with exit code 1.
2026-06-09T05:33:38.9503907Z ##[error]Executing the custom container implementation failed. Please contact your self hosted 
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27185734280)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-09T07:50:59.285121+00:00
