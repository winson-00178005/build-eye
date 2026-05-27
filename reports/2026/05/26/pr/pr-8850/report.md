---
report_id: e2623ed1
pr_number: 8850
group_key: pr-8850
generated_at: 2026-05-26T09:58:18.454214+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #8850

## 概要

PR #8850 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26445062191) | PR代码问题 | 中 | 编译错误 |
| 2 | E2E-Light (#26441924115) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26445062191)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #8850 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26445062191)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/26445062191/job/77849134036)

**日志片段**:
```
2026-05-26T09:49:32.5841213Z Checking PR title: [Future] [P/D] support hybrid attention for mooncake connector
2026-05-26T09:49:32.5865278Z ##[error]PR title must contain one of the following prefixes: [BugFix], [Performance], [Test], [CI], [Feature], [Doc], [Misc], [Community], [Refactor]
2026-05-26T09:49:32.5874033Z ##[error]Example: '[Feature] Add new optimization pass' or 'Add new feature [Feature]'
2026-05-26T09:49:32.5987403Z ##[error]Error: failed to run script step: Error: command termin
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Light (Run #26441924115)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #8850 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26441924115)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/26441924115/job/77838271747)

**日志片段**:
```
2026-05-26T08:43:29.4827920Z Checking PR title: [Future] [P/D] support hybrid attention for mooncake connector
2026-05-26T08:43:29.4852955Z ##[error]PR title must contain one of the following prefixes: [BugFix], [Performance], [Test], [CI], [Feature], [Doc], [Misc], [Community], [Refactor]
2026-05-26T08:43:29.4861575Z ##[error]Example: '[Feature] Add new optimization pass' or 'Add new feature [Feature]'
2026-05-26T08:43:29.4971134Z ##[error]Error: failed to run script step: Error: command termin
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26445062191)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26441924115)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-26T09:58:18.454274+00:00
