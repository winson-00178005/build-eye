---
report_id: 50d91ee7
pr_number: null
group_key: run-26623992733
generated_at: 2026-05-29T07:58:27.953053+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26623992733

## 概要

run-26623992733 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26623992733) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26623992733)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26623992733)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26623992733/job/78456379709)

**日志片段**:
```
2026-05-29T07:24:22.0828272Z          processed_logits = apply_sampling_constraints([m
2026-05-29T07:24:22.0829172Z              processed_logits, metadata.cu_num_draft_tokens, sampling_metadata, rejection_sampler.top_k[m
2026-05-29T07:24:22.0829626Z          )[m
2026-05-29T07:24:22.1264191Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-29T07:24:22.1328113Z ##[error]Process completed with exit code 1.

```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26623992733)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-29T07:58:27.953075+00:00
