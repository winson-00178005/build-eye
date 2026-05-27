---
report_id: 2ca8296b
pr_number: null
group_key: run-26523708392
generated_at: 2026-05-27T18:33:57.232630+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26523708392

## 概要

run-26523708392 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26523708392) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26523708392)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26523708392)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26523708392/job/78121678053)

**日志片段**:
```
2026-05-27T16:19:03.2588599Z [32m+[m
2026-05-27T16:19:03.2589078Z              # Adjust cur_kv based on actual KV data size (mimics NPU operator behavior)[m
2026-05-27T16:19:03.2589785Z              # NPU operator internally checks block_table and truncates to actual available length[m
2026-05-27T16:19:03.2590481Z              # This prevents RuntimeError when requested length exceeds cached tokens[m
2026-05-27T16:19:03.2591075Z              actual_kv_tokens = k_i.numel() // (num_kv_heads *
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26523708392)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T18:33:57.232650+00:00
