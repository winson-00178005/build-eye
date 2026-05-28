---
report_id: d08465df
pr_number: null
group_key: run-26586195108
generated_at: 2026-05-28T18:39:39.982805+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26586195108

## 概要

run-26586195108 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26586195108) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26586195108)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26586195108)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26586195108/job/78332851332)

**日志片段**:
```
2026-05-28T16:01:55.9248910Z [31m-vllm.v1.attention.backends.mla.sparse_swa.DeepseekV4SWACache = AscendDeepseekV4SWACache[m
2026-05-28T16:01:55.9249416Z \ No newline at end of file[m
2026-05-28T16:01:55.9250145Z [32m+[m[32mvllm.v1.attention.backends.mla.sparse_swa.DeepseekV4SWACache = AscendDeepseekV4SWACache[m
2026-05-28T16:01:55.9806979Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-28T16:01:55.9
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26586195108)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-28T18:39:39.982831+00:00
