---
report_id: b421985d
pr_number: 9514
group_key: pr-9514
generated_at: 2026-05-25T10:08:18.225925+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9514

## 概要

PR #9514 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26392364002) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26392364002)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9514 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26392364002)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26392364002/job/77684938889)

**日志片段**:
```
2026-05-25T09:00:07.1975725Z              for state, state_copy_func in zip(kv_caches, mamba_state_copy_funcs):[m
2026-05-25T09:00:07.1976337Z [31m-                copy_spec = state_copy_func([m
2026-05-25T09:00:07.1976972Z [31m-                    state, block_ids, src_block_idx, accept_token_bias + 1[m
2026-05-25T09:00:07.1977525Z [31m-                )[m
2026-05-25T09:00:07.1978011Z [31m-                src_state = _tensor_view_from_data_ptr([m
2026-05-25T09:00:07.1978930Z [31m-    
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26392364002)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T10:08:18.225944+00:00
