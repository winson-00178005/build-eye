---
report_id: d5b6ced6
pr_number: 9650
group_key: pr-9650
generated_at: 2026-05-28T13:54:07.144494+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9650

## 概要

PR #9650 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26578045735) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26578045735)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9650 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26578045735)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26578045735/job/78302981056)

**日志片段**:
```
2026-05-28T13:38:16.5653585Z [31m-vllm.v1.attention.backends.mla.sparse_swa.DeepseekV4SWACache = AscendDeepseekV4SWACache[m
2026-05-28T13:38:16.5654127Z \ No newline at end of file[m
2026-05-28T13:38:16.5654874Z [32m+[m[32mvllm.v1.attention.backends.mla.sparse_swa.DeepseekV4SWACache = AscendDeepseekV4SWACache[m
2026-05-28T13:38:16.6137191Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-28T13:38:16.6
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26578045735)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-28T13:54:07.144529+00:00
