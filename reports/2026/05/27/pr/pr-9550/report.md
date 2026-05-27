---
report_id: aeee68bf
pr_number: 9550
group_key: pr-9550
generated_at: 2026-05-27T05:14:43.376254+00:00
overall_classification: code
total_failed_workflows: 3
category_counts:
  code: 3
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9550

## 概要

PR #9550 触发了 3 个 workflow，均失败。

- **代码问题**: 3 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26489351595) | PR代码问题 | 高 | 测试断言失败 |
| 2 | E2E-Full (#26489351566) | PR代码问题 | 高 | 编译错误 |
| 3 | E2E-Light (#26488650479) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26489351595)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 测试断言失败

**分析推理**: 检测到代码问题模式: test_assertion, compilation。 问题出现在 PR #9550 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- test_assertion: `test_\w+.*failed`
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26489351595)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26489351595/job/78004003106)

**日志片段**:
```
2026-05-27T03:51:40.0661454Z     Uninstalling transformers-5.9.0:
...
2026-05-27T03:51:46.4448830Z 
2026-05-27T03:51:46.4458671Z ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
2026-05-27T03:51:46.4459580Z te 0.4.0 requires ml-dtypes, which is not installed.
2026-05-27T03:51:46.4459961Z te 0.4.0 requires tornado, which is not installed.
2026-05-27T03:51:46.4460406Z ms-se
```

**建议**:
- 优先: 检查失败的测试用例 (低成本)
- 检查失败的测试用例 (低成本)
- 修复测试或代码 (中等成本)

### 2. E2E-Full (Run #26489351566)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9550 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26489351566)
[查看 Job: e2e-comment (d4004455d2357985830af10e432709b42c820455) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26489351566/job/78003773385)

**日志片段**:
```
2026-05-27T03:43:51.3758656Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-27T03:43:51.3759083Z   type: comment
2026-05-27T03:43:51.3759657Z   contains_310: false
2026-05-27T03:43:51.3759852Z   continue_on_error: false
2026-05-27T03:43:51.3760108Z   ref: 3142330e829612f42bda7aa96f9b51499c87896d
2026-05-27T03:43:51.3760931Z   singlecard_tests: tests/e2e/singlecard/spec_decode/test_extract_hidden_states.py tests/e2e/singlecard/te
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Light (Run #26488650479)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9550 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26488650479)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26488650479/job/78002213707)

**日志片段**:
```
2026-05-27T03:28:18.5053442Z 
2026-05-27T03:28:18.5053825Z To bypass pre-commit hooks, add --no-verify to git commit.
2026-05-27T03:28:18.5054085Z 
2026-05-27T03:28:18.5501660Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-27T03:28:18.5579459Z ##[error]Process completed with exit code 1.
2026-05-27T03:28:18.5689281Z ##[error]Executing the custom container implementation failed. Please contact your self ho
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26489351595)**: 检查失败的测试用例 (低成本) - 查看测试文件中的断言错误
- **E2E-Full (#26489351566)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26488650479)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T05:14:43.376326+00:00
