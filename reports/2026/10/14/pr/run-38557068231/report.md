---
report_id: d140aa2c
pr_number: null
group_key: run-38557068231
generated_at: 2026-10-14T14:57:40.481848+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-38557068231

## 概要

run-38557068231 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#38557068231) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-upstream (Run #38557068231)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `AssertionError`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231)
[查看 Job: e2e-upstream_singlecard (1, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038013)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038024)
[查看 Job: e2e-upstream_singlecard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038025)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038033)
[查看 Job: e2e-upstream_singlecard (2, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038090)
[查看 Job: e2e-upstream_online (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038121)
[查看 Job: e2e-upstream_singlecard (3, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/38557068231/job/115831038326)

**日志片段**:
```
2026-10-14T12:05:10.0078689Z 
2026-10-14T12:05:10.0079294Z ../../../../usr/local/python3.12.13/lib/python3.12/site-packages/schemathesis/generation/coverage.py:305
2026-10-14T12:05:10.0082062Z   /usr/local/python3.12.13/lib/python3.12/site-packages/schemathesis/generation/coverage.py:305: DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.
2
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#38557068231)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-10-14T14:57:40.481893+00:00
