---
report_id: 9d8fd829
pr_number: null
group_key: run-27285344621
generated_at: 2026-06-10T23:28:43.788878+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27285344621

## 概要

run-27285344621 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27285344621) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27285344621)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27285344621)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27285344621/job/80590880336)

**日志片段**:
```
2026-06-10T15:00:33.9249149Z      def full_graph_pa([m
2026-06-10T15:00:33.9249489Z          self,[m
2026-06-10T15:00:33.9249851Z          query: torch.Tensor,[m
2026-06-10T15:00:33.9725106Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-10T15:00:33.9784302Z ##[error]Process completed with exit code 1.
2026-06-10T15:00:33.9899503Z ##[error]Executing the custom container implementation failed. Please con
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27285344621)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-10T23:28:43.788915+00:00
