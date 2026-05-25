---
report_id: 71a3eb88
pr_number: null
group_key: run-26363423201
generated_at: 2026-05-25T03:09:14.596254+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26363423201

## 概要

run-26363423201 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26363423201) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26363423201)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26363423201)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26363423201/job/77602871313)

**日志片段**:
```
2026-05-24T14:08:57.3910752Z [36m@@ -11,6 +11,7 @@[m
2026-05-24T14:08:57.3911184Z  [m
2026-05-24T14:08:57.3911697Z  import torch[m
2026-05-24T14:08:57.3912305Z  from vllm.triton_utils import tl, triton[m
2026-05-24T14:08:57.3912774Z [32m+[m
2026-05-24T14:08:57.3913404Z  from .utils import prepare_chunk_indices, safe_exp[m
2026-05-24T14:08:57.3913885Z  [m
2026-05-24T14:08:57.3914368Z  [m
2026-05-24T14:08:57.3914969Z [36m@@ -121,6 +122,7 @@[m [mdef chunk_scaled_dot_kkt_fwd([m
2026-05
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26363423201)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T03:09:14.596276+00:00
