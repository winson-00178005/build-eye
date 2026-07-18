---
report_id: 00dca114
pr_number: null
group_key: run-29572096800
generated_at: 2026-07-18T06:08:03.331566+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-29572096800

## 概要

run-29572096800 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#29572096800) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-Light (Run #29572096800)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `test_\w+.*failed`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/29572096800)
[查看 Job: smart test (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/29572096800/job/87859645648)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/29572096800/job/87859645670)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/29572096800/job/87859645712)
[查看 Job: e2e-light (v0.20.2) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/29572096800/job/87859645732)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/29572096800/job/87859645836)

**日志片段**:
```
2026-07-17T10:16:36.3166003Z     Uninstalling transformers-5.14.1:
...
2026-07-17T10:16:42.7807294Z 
2026-07-17T10:16:42.7819541Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-07-17T10:16:42.7820841Z te 0.4.0 requires ml-dtypes, which is not installed.
2026-07-17T10:16:42.7821252Z te 0.4.0 requires tornado, which is not installed.
2026-07-17T10:16:42.7821642Z ms-s
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#29572096800)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-07-18T06:08:03.331601+00:00
