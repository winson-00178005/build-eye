---
report_id: 666240c8
pr_number: null
group_key: run-28657885693
generated_at: 2026-07-03T12:13:24.583285+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28657885693

## 概要

run-28657885693 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#28657885693) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-Light (Run #28657885693)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `test_\w+.*failed`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951652)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951674)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951686)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / multicard-4-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951689)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951697)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951713)
[查看 Job: e2e-light (v0.20.2) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951730)
[查看 Job: e2e-light (v0.20.2) / multicard-4-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951733)
[查看 Job: e2e-light (v0.20.2) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951754)
[查看 Job: e2e-light (v0.20.2) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/28657885693/job/84991951767)

**日志片段**:
```
2026-07-03T11:44:16.1471050Z     Uninstalling transformers-5.12.1:
...
2026-07-03T11:44:22.6526061Z 
2026-07-03T11:44:22.6535090Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-07-03T11:44:22.6536317Z te 0.4.0 requires ml-dtypes, which is not installed.
2026-07-03T11:44:22.6536700Z te 0.4.0 requires tornado, which is not installed.
2026-07-03T11:44:22.6537159Z ms-s
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#28657885693)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-07-03T12:13:24.583330+00:00
