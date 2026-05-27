---
report_id: 028ff87b
pr_number: null
group_key: run-26485347387
generated_at: 2026-05-27T02:45:58.541843+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26485347387

## 概要

run-26485347387 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26485347387) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26485347387)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26485347387)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26485347387/job/77991580277)

**日志片段**:
```
2026-05-27T01:35:19.5932049Z  # --- Mock the vllm model classes used by the module-under-test ---[m
2026-05-27T01:35:19.5932402Z  [m
2026-05-27T01:35:19.5932632Z [32m+[m
2026-05-27T01:35:19.5933070Z  # A plain class (NOT MagicMock) is critical â MagicMock auto-answers[m
2026-05-27T01:35:19.5933835Z  # hasattr with True, which would defeat the forward_qk / _normalize_qk[m
2026-05-27T01:35:19.5934412Z  # probes.  We use a real class so hasattr respects our runtime setup.[m
2026-05-27T01:3
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26485347387)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T02:45:58.541867+00:00
