---
report_id: 6883563b
pr_number: 9721
group_key: pr-9721
generated_at: 2026-05-31T23:02:53.658504+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 1
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #9721

## 概要

PR #9721 触发了 2 个 workflow，均失败。

- **代码问题**: 1 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26717286208) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#26717286227) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-Full (Run #26717286208)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26717286208)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #26717286227)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 问题出现在 PR #9721 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `test_\w+.*failed`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26717286227)
[查看 Job: smart test (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26717286227/job/78738265793)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26717286227/job/78738265810)

**日志片段**:
```
2026-05-31T16:04:25.7459018Z     Uninstalling transformers-5.9.0:
...
2026-05-31T16:04:33.1846078Z 
2026-05-31T16:04:33.1857465Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-05-31T16:04:33.1858366Z te 0.4.0 requires ml-dtypes, which is not installed.
2026-05-31T16:04:33.1858701Z te 0.4.0 requires tornado, which is not installed.
2026-05-31T16:04:33.1859445Z ms-se
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26717286208)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#26717286227)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-05-31T23:02:53.658547+00:00
