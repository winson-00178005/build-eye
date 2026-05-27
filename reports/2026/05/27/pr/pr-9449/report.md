---
report_id: 261d5399
pr_number: 9449
group_key: pr-9449
generated_at: 2026-05-27T01:10:15.294105+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9449

## 概要

PR #9449 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26484167819) | PR代码问题 | 中 | 编译错误 |
| 2 | Docs link check (#26450490466) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26484167819)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9449 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26484167819)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/26484167819/job/77987936561)

**日志片段**:
```
2026-05-27T00:58:37.6555429Z Checking PR title: [ci][Nightly] Add the external_dp test framework
2026-05-27T00:58:37.6581503Z ##[error]PR title must contain one of the following prefixes: [BugFix], [Performance], [Test], [CI], [Feature], [Doc], [Misc], [Community], [Refactor]
2026-05-27T00:58:37.6590494Z ##[error]Example: '[Feature] Add new optimization pass' or 'Add new feature [Feature]'
2026-05-27T00:58:37.6695375Z ##[error]Error: failed to run script step: Error: command terminated with non-
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. Docs link check (Run #26450490466)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9449 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26450490466)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/26450490466/job/77869551694)

**日志片段**:
```
2026-05-26T13:21:12.0344150Z   token: ***
2026-05-26T13:21:12.0344337Z   api_url: https://api.github.com
2026-05-26T13:21:12.0344564Z   fail_on_initial_diff_error: false
2026-05-26T13:21:12.0344784Z   fail_on_submodule_diff_error: false
2026-05-26T13:21:12.0345021Z   negation_patterns_first: false
2026-05-26T13:21:12.0345215Z   matrix: false
2026-05-26T13:21:12.0345386Z   exclude_submodules: false
...
2026-05-26T13:21:22.2069398Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
2026-05-26T13:2
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26484167819)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Docs link check (#26450490466)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T01:10:15.294159+00:00
