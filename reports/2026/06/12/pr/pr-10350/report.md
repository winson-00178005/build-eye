---
report_id: 52c32840
pr_number: 10350
group_key: pr-10350
generated_at: 2026-06-12T23:20:59.580915+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 1
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #10350

## 概要

PR #10350 触发了 2 个 workflow，均失败。

- **代码问题**: 1 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27423189842) | PR代码问题 | 中 | 编译错误 |
| 2 | E2E-Full (#27423189723) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. E2E-Light (Run #27423189842)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10350 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27423189842)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27423189842/job/81054488375)

**日志片段**:
```
2026-06-12T14:52:05.5904981Z [31m-        for g in kv_cache_config.kv_cache_groups[m
2026-06-12T14:52:05.5905497Z [31m-    ):[m
2026-06-12T14:52:05.5906358Z [32m+[m[32m    if not any(isinstance(g.kv_cache_spec, _SLIDING_WINDOW_SPECS) for g in kv_cache_config.kv_cache_groups):[m
2026-06-12T14:52:05.5906981Z          raise ValueError([m
2026-06-12T14:52:05.5907525Z              "VLLM_ASCEND_PREFIX_CACHE_RETENTION_INTERVAL is set but this "[m
2026-06-12T14:52:05.5908207Z              "mod
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Full (Run #27423189723)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27423189723)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27423189842)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#27423189723)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-06-12T23:20:59.580990+00:00
