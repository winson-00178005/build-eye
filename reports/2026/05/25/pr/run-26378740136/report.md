---
report_id: d29d6c67
pr_number: null
group_key: run-26378740136
generated_at: 2026-05-25T03:52:16.816619+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26378740136

## 概要

run-26378740136 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26378740136) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26378740136)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26378740136)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26378740136/job/77643824579)

**日志片段**:
```
2026-05-25T01:38:21.4505434Z [31m-                                        and vllm_config.kv_transfer_config[m
2026-05-25T01:38:21.4505924Z [32m+[m[32m        using_kv_transfer_with_hybrid = ([m
2026-05-25T01:38:21.4506771Z [32m+[m[32m            not vllm_config.scheduler_config.disable_hybrid_kv_cache_manager and vllm_config.kv_transfer_config[m
2026-05-25T01:38:21.4507308Z [32m+[m[32m        )[m
2026-05-25T01:38:21.4507630Z          cache_config = vllm_config.cache_config[m
2026
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26378740136)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T03:52:16.816652+00:00
