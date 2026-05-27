---
report_id: 3e38e95e
pr_number: 7964
group_key: pr-7964
generated_at: 2026-05-27T01:10:15.294721+00:00
overall_classification: code
total_failed_workflows: 5
category_counts:
  code: 5
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #7964

## 概要

PR #7964 触发了 5 个 workflow，均失败。

- **代码问题**: 5 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26458536987) | PR代码问题 | 高 | 测试断言失败 |
| 2 | E2E-Light (#26457557662) | PR代码问题 | 中 | 编译错误 |
| 3 | E2E-Light (#26451710946) | PR代码问题 | 高 | 编译错误 |
| 4 | E2E-Light (#26451013024) | PR代码问题 | 高 | 编译错误 |
| 5 | E2E-Light (#26449888216) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26458536987)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 问题出现在 PR #7964 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `test_\w+.*failed`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987)
[查看 Job: smart test (1ac10f159a09897baada01b14b6a0dd6442aefd6) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676529)
[查看 Job: smart test (1ac10f159a09897baada01b14b6a0dd6442aefd6) / smart-ut (a2 x1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676555)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676581)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676586)
[查看 Job: e2e-light (v0.20.2) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676616)
[查看 Job: e2e-light (v0.20.2) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676672)
[查看 Job: smart test (v0.20.2) / smart-ut (a2 x1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676693)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676702)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676707)
[查看 Job: e2e-light (v0.20.2) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676869)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900676880)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26458536987/job/77900677523)

**日志片段**:
```
2026-05-26T15:50:25.1843029Z     Uninstalling transformers-5.9.0:
2026-05-26T15:50:25.1996080Z       Successfully uninstalled transformers-5.9.0
2026-05-26T15:50:32.5799473Z 
2026-05-26T15:50:32.5809784Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-05-26T15:50:32.5811351Z te 0.4.0 requires ml-dtypes, which is not installed.
2026-05-26T15:50:32.5811946Z te 0.4.0 r
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

### 2. E2E-Light (Run #26457557662)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #7964 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26457557662)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26457557662/job/77896200276)

**日志片段**:
```
2026-05-26T15:24:09.6230452Z      FusedExpertsResult,[m
2026-05-26T15:24:09.6230799Z      _MoECommMethods,[m
2026-05-26T15:24:09.6231062Z  )[m
2026-05-26T15:24:09.6720122Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-26T15:24:09.6775241Z ##[error]Process completed with exit code 1.
2026-05-26T15:24:09.6889753Z ##[error]Executing the custom container implementation failed. Please contact your self host
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Light (Run #26451710946)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #7964 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26451710946)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26451710946/job/77874244598)

**日志片段**:
```
2026-05-26T13:43:51.6338894Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-26T13:43:52.1238130Z ============================
2026-05-26T13:43:52.1248161Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-26T13:44:02.9416626Z ##[error]vllm_ascend/attention/attention_v1.py:317: error: "AttentionMaskBuilder" has no attribute "get_swa_mask"; maybe "get_mla_mask" or "get_attn_mask"?  [attr-defined]
2026-05-26T13:44:04.3749967Z Found 1 error i
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 4. E2E-Light (Run #26451013024)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #7964 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26451013024)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26451013024/job/77871611937)

**日志片段**:
```
2026-05-26T13:31:55.0694894Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-26T13:31:55.4896551Z ============================
2026-05-26T13:31:55.4907699Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-26T13:32:06.2530285Z ##[error]vllm_ascend/attention/attention_v1.py:298: error: "AttentionMaskBuilder" has no attribute "get_swa_mask"; maybe "get_mla_mask" or "get_attn_mask"?  [attr-defined]
2026-05-26T13:32:06.2539163Z ##[error]vllm_a
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. E2E-Light (Run #26449888216)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #7964 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26449888216)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26449888216/job/77867495326)

**日志片段**:
```
2026-05-26T13:11:21.4802790Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-26T13:11:21.9053817Z ============================
2026-05-26T13:11:21.9064802Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-26T13:11:33.2406209Z ##[error]vllm_ascend/attention/attention_v1.py:298: error: "AttentionMaskBuilder" has no attribute "get_swa_mask"; maybe "get_mla_mask" or "get_attn_mask"?  [attr-defined]
2026-05-26T13:11:33.2415457Z ##[error]vllm_a
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26458536987)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误
- **E2E-Light (#26457557662)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26451710946)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26451013024)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26449888216)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T01:10:15.294778+00:00
