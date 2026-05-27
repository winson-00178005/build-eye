---
report_id: 5cb7606c
pr_number: null
group_key: run-26485685534
generated_at: 2026-05-27T02:45:58.541230+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26485685534

## 概要

run-26485685534 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26485685534) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26485685534)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26485685534)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26485685534/job/77992527122)

**日志片段**:
```
2026-05-27T01:45:11.7337588Z [1m--- a/vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_connector.py[m
2026-05-27T01:45:11.7338569Z [1m+++ b/vllm_ascend/distributed/kv_transfer/kv_p2p/mooncake_connector.py[m
2026-05-27T01:45:11.7339319Z [36m@@ -2018,4 +2018,4 @@[m [mdef get_prefill_pp_indices([m
2026-05-27T01:45:11.7340044Z              raise ValueError(f"{sum(partitions)=} does not match {num_hidden_layers=}.")[m
2026-05-27T01:45:11.7340681Z          start_layer = sum(partitions[:pp_
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26485685534)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T02:45:58.541251+00:00
