---
report_id: 15428f25
pr_number: null
group_key: run-26393407426
generated_at: 2026-05-25T10:08:18.225615+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26393407426

## 概要

run-26393407426 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26393407426) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26393407426)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26393407426)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26393407426/job/77688341207)

**日志片段**:
```
2026-05-25T09:28:11.2049457Z [1mdiff --git a/vllm_ascend/ops/dsa.py b/vllm_ascend/ops/dsa.py[m
2026-05-25T09:28:11.2050431Z [1mindex 2a1e879..8a71447 100644[m
2026-05-25T09:28:11.2050823Z [1m--- a/vllm_ascend/ops/dsa.py[m
2026-05-25T09:28:11.2051199Z [1m+++ b/vllm_ascend/ops/dsa.py[m
2026-05-25T09:28:11.2051733Z [36m@@ -293,9 +293,7 @@[m [mdef dsa_forward([m
2026-05-25T09:28:11.2052110Z          decode_compressed_kv = None[m
2026-05-25T09:28:11.2052418Z          if has_decode:[m
20
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26393407426)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T10:08:18.225635+00:00
