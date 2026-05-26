---
report_id: f04476fa
pr_number: 9075
group_key: pr-9075
generated_at: 2026-05-26T03:03:16.968463+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9075

## 概要

PR #9075 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Cache csrc Build Artifacts (#26426724785) | PR代码问题 | 中 | 编译错误 |
| 2 | E2E-Light (#26426724837) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Cache csrc Build Artifacts (Run #26426724785)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9075 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724785)
[查看 Job: build-ARM64-a3-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724785/job/77791749875)
[查看 Job: build-X64-a3-ubuntu-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724785/job/77791749877)
[查看 Job: build-X64-a3-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724785/job/77791749900)
[查看 Job: build-ARM64-a3-ubuntu-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724785/job/77791749901)

**日志片段**:
```
2026-05-26T01:28:23.5760418Z       In file included from
2026-05-26T01:28:23.5760820Z       /__w/vllm-ascend/vllm-ascend/csrc/build/binary/ascend910_93/src/inplace_partial_rotary_mul/op_kernel/rotate_interleaved_split_s.h:17:
2026-05-26T01:28:23.5760936Z       In file included from
2026-05-26T01:28:23.5761322Z       /__w/vllm-ascend/vllm-ascend/csrc/build/binary/ascend910_93/src/inplace_partial_rotary_mul/op_kernel/rotate_interleaved_common.h:18:
2026-05-26T01:28:23.5761668Z       /usr/local/Asc
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Light (Run #26426724837)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9075 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724837)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724837/job/77792174360)
[查看 Job: e2e-light (v0.20.2) / multicard-4-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724837/job/77792174362)
[查看 Job: e2e-light (v0.20.2) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26426724837/job/77792174371)

**日志片段**:
```
2026-05-26T01:21:36.8631583Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-05-26T01:21:36.8991899Z [command]/usr/bin/git config --file /__w/_temp/git-credentials-087c4caf-eb03-4d1d-aa3c-74c811ae7a85.config http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-05-26T01:21:36.9033679Z [command]/usr/bin/git config --local includeIf.gitdir:/__w/vllm-ascend/vllm-ascend/vllm-empty/.git.path /__w/_temp/g
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Cache csrc Build Artifacts (#26426724785)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26426724837)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-26T03:03:16.968490+00:00
