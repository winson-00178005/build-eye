---
report_id: a94921a6
pr_number: null
group_key: run-26587254704
generated_at: 2026-05-28T23:19:23.882076+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26587254704

## 概要

run-26587254704 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26587254704) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-Full (Run #26587254704)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, test_assertion, compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `AssertionError`
- test_assertion: `FAILED\s+[\w/]+\.py`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26587254704)
[查看 Job: e2e-full (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26587254704/job/78336713842)

**日志片段**:
```
2026-05-28T16:20:39.5517556Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-28T16:20:39.5517974Z   type: full
2026-05-28T16:20:39.5518492Z   contains_310: false
2026-05-28T16:20:39.5518691Z   continue_on_error: false
2026-05-28T16:20:39.5518901Z   ref: 
2026-05-28T16:20:39.5519189Z   singlecard_tests: 
2026-05-28T16:20:39.5519403Z   multicard_2_tests: 
...
2026-05-28T16:45:28.6465095Z >       [94massert[39;49;00m match[90m[3
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26587254704)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-05-28T23:19:23.882103+00:00
