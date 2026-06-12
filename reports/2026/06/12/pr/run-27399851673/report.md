---
report_id: 6afd739f
pr_number: null
group_key: run-27399851673
generated_at: 2026-06-12T08:28:53.959508+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27399851673

## 概要

run-27399851673 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27399851673) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-Light (Run #27399851673)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, test_assertion, compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `FAILED\s+[\w/]+\.py`
- test_assertion: `test_\w+.*failed`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27399851673)
[查看 Job: unit test (v0.18.0) / unit test](https://github.com/vllm-project/vllm-ascend/actions/runs/27399851673/job/80975615920)
[查看 Job: e2e-light (v0.18.0) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27399851673/job/80975616059)
[查看 Job: e2e-light (v0.18.0) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27399851673/job/80975616068)

**日志片段**:
```
2026-06-12T07:01:10.0043789Z     changing mode of /tmp/pip-build-env-hf034n3e/overlay/bin/tiny-agents to 755
2026-06-12T07:01:10.5384450Z     changing mode of /tmp/pip-build-env-hf034n3e/overlay/bin/transformers to 755
2026-06-12T07:01:11.0351436Z 
2026-06-12T07:01:11.0361939Z   ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-06-12T07:01:11.0365777Z   te 0.4.0 requi
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27399851673)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-06-12T08:28:53.959540+00:00
