---
report_id: 82c5d4df
pr_number: null
group_key: run-26485459939
generated_at: 2026-05-27T01:42:17.893708+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26485459939

## 概要

run-26485459939 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26485459939) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26485459939)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26485459939)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26485459939/job/77991899454)

**日志片段**:
```
2026-05-27T01:38:48.8804653Z  # --- Mock the vllm model classes used by the module-under-test ---[m
2026-05-27T01:38:48.8804957Z  [m
2026-05-27T01:38:48.8805119Z [32m+[m
2026-05-27T01:38:48.8805519Z  # A plain class (NOT MagicMock) is critical â MagicMock auto-answers[m
2026-05-27T01:38:48.8806084Z  # hasattr with True, which would defeat the forward_qk / _normalize_qk[m
2026-05-27T01:38:48.8806632Z  # probes.  We use a real class so hasattr respects our runtime setup.[m
2026-05-27T01:3
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26485459939)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T01:42:17.893760+00:00
