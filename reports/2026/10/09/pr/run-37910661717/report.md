---
report_id: 42c9dcdd
pr_number: null
group_key: run-37910661717
generated_at: 2026-10-09T11:11:27.348544+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-37910661717

## 概要

run-37910661717 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#37910661717) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-upstream (Run #37910661717)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `FAILED\s+[\w/]+\.py`
- compilation: `error:\s+`
- import_error: `ModuleNotFoundError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717)
[查看 Job: e2e-upstream_singlecard (1, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755775187)
[查看 Job: e2e-upstream_singlecard (2, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755775203)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755775232)
[查看 Job: e2e-upstream_multicard (0, 9.1.0-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755775317)
[查看 Job: e2e-upstream_singlecard (0, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755775319)
[查看 Job: e2e-upstream_singlecard (3, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755775425)
[查看 Job: e2e-upstream_online (0, 9.1.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37910661717/job/113755776066)

**日志片段**:
```
2026-10-09T09:55:44.4175841Z 
2026-10-09T09:55:44.4175947Z ............................................................
2026-10-09T09:55:44.4176354Z [95m[1/40] START  tests/benchmarks/test_skip_tokenizer_init.py[0m
2026-10-09T09:57:00.6858980Z INTERNALERROR> Traceback (most recent call last):
2026-10-09T09:57:00.6860469Z INTERNALERROR>   File "/usr/local/python3.12.13/lib/python3.12/site-packages/_pytest/main.py", line 326, in wrap_session
2026-10-09T09:57:00.6860914Z INTERNALERROR>     config
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#37910661717)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-10-09T11:11:27.348582+00:00
