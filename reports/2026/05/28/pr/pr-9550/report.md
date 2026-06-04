---
report_id: 032caa6a
pr_number: 9550
group_key: pr-9550
generated_at: 2026-05-28T23:19:23.880832+00:00
overall_classification: code
total_failed_workflows: 4
category_counts:
  code: 2
  infrastructure: 2
  interference: 0
---

# 构建失败报告: PR #9550

## 概要

PR #9550 触发了 4 个 workflow，均失败。

- **代码问题**: 2 次
- **基础设施问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26592358815) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#26592358761) | PR代码问题 | 高 | 编译错误 |
| 3 | E2E-Light (#26590112009) | PR代码问题 | 中 | 编译错误 |
| 4 | E2E-Full (#26590111941) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. E2E-Full (Run #26592358815)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26592358815)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #26592358761)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error, import_error。 问题出现在 PR #9550 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `ImportError`
- import_error: `AttributeError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26592358761)
[查看 Job: e2e-light (7e1b45a09252a5b513cd83116aa7a2f310220c34) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26592358761/job/78360381191)
[查看 Job: e2e-light (7e1b45a09252a5b513cd83116aa7a2f310220c34) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26592358761/job/78360381234)
[查看 Job: smart test (7e1b45a09252a5b513cd83116aa7a2f310220c34) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26592358761/job/78360381374)

**日志片段**:
```
2026-05-28T18:28:27.4556506Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-28T18:28:27.4557540Z   type: light
2026-05-28T18:28:27.4559020Z   contains_310: true
2026-05-28T18:28:27.4559746Z   continue_on_error: true
2026-05-28T18:28:27.4560307Z   ref: 
2026-05-28T18:28:27.4560796Z   singlecard_tests: 
2026-05-28T18:28:27.4561330Z   multicard_2_tests: 
...
2026-05-28T18:38:09.6606837Z (Use `node --trace-deprecation ...` to show w
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Light (Run #26590112009)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9550 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26590112009)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26590112009/job/78346652917)

**日志片段**:
```
2026-05-28T17:14:52.0029307Z  from vllm.triton_utils import triton[m
2026-05-28T17:14:52.0029777Z  from vllm.utils.math_utils import next_power_of_2[m
2026-05-28T17:14:52.0030089Z  [m
2026-05-28T17:14:52.0468233Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-28T17:14:52.0566033Z ##[error]Process completed with exit code 1.
2026-05-28T17:14:52.0678952Z ##[error]Executing the custom container implementat
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 4. E2E-Full (Run #26590111941)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26590111941)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26592358815)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#26592358761)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26590112009)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#26590111941)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-05-28T23:19:23.880970+00:00
