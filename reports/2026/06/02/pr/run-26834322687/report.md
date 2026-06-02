---
report_id: 2d406d67
pr_number: null
group_key: run-26834322687
generated_at: 2026-06-02T19:44:50.037096+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26834322687

## 概要

run-26834322687 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26834322687) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26834322687)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26834322687)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26834322687/job/79123985127)

**日志片段**:
```
2026-06-02T16:44:43.7333812Z ##[error]PR title must contain one of the following prefixes: [BugFix], [Performance], [Test], [CI], [Feature], [Doc], [Misc], [Community], [Refactor]
2026-06-02T16:44:43.7343117Z ##[error]Example: '[Feature] Add new optimization pass' or 'Add new feature [Feature]'
2026-06-02T16:44:43.7466077Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-02T16:44:43.7565200Z ##[error]Process
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26834322687)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-02T19:44:50.037123+00:00
