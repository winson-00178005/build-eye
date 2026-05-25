---
report_id: 2da4ae6c
pr_number: 9340
group_key: pr-9340
generated_at: 2026-05-25T14:55:27.549710+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9340

## 概要

PR #9340 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26405794147) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26405794147)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9340 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26405794147)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26405794147/job/77728789183)

**日志片段**:
```
2026-05-25T14:37:04.1737952Z [31m-                original_seq_lens = original_seq_lens - num_rejected_tokens_gpu[:batch_size] [m
2026-05-25T14:37:04.1739129Z [32m+[m[32m                original_seq_lens = original_seq_lens - num_rejected_tokens_gpu[:batch_size][m
2026-05-25T14:37:04.1739853Z  [m
2026-05-25T14:37:04.1740442Z          copy_and_expand_dflash_inputs_kernel_single_grid[1,]([m
2026-05-25T14:37:04.1741231Z              # Inputs[m
2026-05-25T14:37:04.1742104Z [36m@@ -134,9 +1
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26405794147)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T14:55:27.549756+00:00
