---
report_id: 838ebc2e
pr_number: null
group_key: run-28579485925
generated_at: 2026-07-02T12:12:36.776955+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28579485925

## 概要

run-28579485925 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#28579485925) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #28579485925)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28579485925)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/28579485925/job/84736040836)

**日志片段**:
```
2026-07-02T09:23:31.9386601Z ##[error]PR title must contain one of the following prefixes: [BugFix], [Performance], [Test], [CI], [Feature], [Doc], [Misc], [Community], [Refactor]
2026-07-02T09:23:31.9395081Z ##[error]Example: '[Feature] Add new optimization pass' or 'Add new feature [Feature]'
2026-07-02T09:23:31.9500146Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-07-02T09:23:31.9567820Z ##[error]Process
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#28579485925)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-02T12:12:36.776984+00:00
