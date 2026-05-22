---
report_id: c2530e9a
pr_number: null
group_key: run-26266075621
generated_at: 2026-05-22T03:50:13.211347+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26266075621

## 概要

run-26266075621 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26266075621) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26266075621)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075621)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075621/job/77309548000)

**日志片段**:
```
2026-05-22T03:08:45.3890105Z  from vllm_ascend.ops.triton.layernorm_gated import layer_norm_fwd_npu[m
2026-05-22T03:08:45.3890702Z  from vllm_ascend.utils import enable_custom_op, get_weight_prefetch_method[m
2026-05-22T03:08:45.3891028Z  [m
2026-05-22T03:08:45.3891784Z [1mdiff --git a/vllm_ascend/ops/triton/fla/chunk_scaled_dot_kkt.py b/vllm_ascend/ops/triton/fla/chunk_scaled_dot_kkt.py[m
2026-05-22T03:08:45.3892376Z [1mindex d37527e..55822ea 100644[m
2026-05-22T03:08:45.3892836Z [1m---
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26266075621)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T03:50:13.211380+00:00
