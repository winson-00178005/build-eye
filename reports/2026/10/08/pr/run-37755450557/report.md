---
report_id: 22cb3bfc
pr_number: null
group_key: run-37755450557
generated_at: 2026-10-08T11:12:09.311095+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-37755450557

## 概要

run-37755450557 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#37755450557) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-upstream (Run #37755450557)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `FAILED\s+[\w/]+\.py`
- compilation: `error:\s+`
- import_error: `ModuleNotFoundError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557)
[查看 Job: e2e-upstream_singlecard (1, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881455)
[查看 Job: e2e-upstream_singlecard (2, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881469)
[查看 Job: e2e-upstream_singlecard (3, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881495)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881555)
[查看 Job: e2e-upstream_singlecard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881572)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881586)
[查看 Job: e2e-upstream_online (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37755450557/job/113239881607)

**日志片段**:
```
2026-10-08T09:32:16.1809404Z 
2026-10-08T09:32:16.1809513Z ............................................................
2026-10-08T09:32:16.1809984Z [95m[1/40] START  tests/benchmarks/test_skip_tokenizer_init.py[0m
2026-10-08T09:33:28.4472380Z INTERNALERROR> Traceback (most recent call last):
2026-10-08T09:33:28.4472901Z INTERNALERROR>   File "/usr/local/python3.12.13/lib/python3.12/site-packages/_pytest/main.py", line 326, in wrap_session
2026-10-08T09:33:28.4473339Z INTERNALERROR>     config
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#37755450557)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-10-08T11:12:09.311126+00:00
