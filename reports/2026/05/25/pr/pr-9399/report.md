---
report_id: cc6f552d
pr_number: 9399
group_key: pr-9399
generated_at: 2026-05-25T03:27:33.360631+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9399

## 概要

PR #9399 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26379297544) | PR代码问题 | 高 | 测试断言失败 |


## Workflow 详细分析
### 1. E2E-Full (Run #26379297544)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 问题出现在 PR #9399 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `FAILED\s+[\w/]+\.py`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26379297544)
[查看 Job: e2e-comment (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26379297544/job/77645388884)

**日志片段**:
```
2026-05-25T02:12:12.8680240Z ../../../usr/local/python3.11.15/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/graph_pass.py:192
2026-05-25T02:12:12.8681085Z   /usr/local/python3.11.15/lib/python3.11/site-packages/torch_npu/dynamo/torchair/_ge_concrete_graph/graph_pass.py:192: DeprecationWarning: invalid escape sequence '\ '
2026-05-25T02:12:12.8681698Z     '''
2026-05-25T02:12:12.8681800Z 
2026-05-25T02:12:12.8682067Z tests/e2e/singlecard/spec_decode/test_v1_spec_decode
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26379297544)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误

---
报告生成时间: 2026-05-25T03:27:33.360659+00:00
