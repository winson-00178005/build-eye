---
report_id: c4a10c88
pr_number: 9449
group_key: pr-9449
generated_at: 2026-05-27T04:01:52.458495+00:00
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
| 1 | E2E-Light (#26486239020) | PR代码问题 | 中 | 编译错误 |
| 2 | Docs link check (#26486238913) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26486239020)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9449 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26486239020)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/26486239020/job/77994212988)

**日志片段**:
```
2026-05-27T02:01:58.7327121Z ##[error]PR title must contain one of the following prefixes: [BugFix], [Performance], [Test], [CI], [Feature], [Doc], [Misc], [Community], [Refactor]
2026-05-27T02:01:58.7336035Z ##[error]Example: '[Feature] Add new optimization pass' or 'Add new feature [Feature]'
2026-05-27T02:01:58.7483276Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-27T02:01:58.7545315Z ##[error]Process
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. Docs link check (Run #26486238913)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9449 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26486238913)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/26486238913/job/77994212470)

**日志片段**:
```
2026-05-27T02:02:07.8318575Z   token: ***
...
2026-05-27T02:02:07.8318978Z   fail_on_initial_diff_error: false
2026-05-27T02:02:07.8319203Z   fail_on_submodule_diff_error: false
2026-05-27T02:02:07.8319434Z   negation_patterns_first: false
2026-05-27T02:02:07.8319629Z   matrix: false
2026-05-27T02:02:07.8319802Z   exclude_submodules: false
...
2026-05-27T02:02:20.3192622Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-05-27T02:02:25.5575052Z 
2026-05-27T02:02:25.5584346Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26486239020)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Docs link check (#26486238913)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T04:01:52.458548+00:00
