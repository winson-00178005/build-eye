---
report_id: 289502b1
pr_number: 9340
group_key: pr-9340
generated_at: 2026-05-25T19:41:29.358391+00:00
overall_classification: code
total_failed_workflows: 3
category_counts:
  code: 3
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9340

## 概要

PR #9340 触发了 3 个 workflow，均失败。

- **代码问题**: 3 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26407603049) | PR代码问题 | 高 | 编译错误 |
| 2 | E2E-Full (#26407603058) | PR代码问题 | 中 | 编译错误 |
| 3 | E2E-Light (#26405794147) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26407603049)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9340 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26407603049)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26407603049/job/77734670251)

**日志片段**:
```
2026-05-25T15:21:28.7856778Z [36;1mfor python_version in "3.10" "3.11" "3.12"; do[0m
2026-05-25T15:21:28.7857093Z [36;1m  echo "============================"[0m
2026-05-25T15:21:28.7857385Z [36;1m  tools/mypy.sh 1 "$python_version"[0m
2026-05-25T15:21:28.7857697Z [36;1m  echo "============================"[0m
2026-05-25T15:21:28.7857965Z [36;1mdone[0m
2026-05-25T15:21:28.7858488Z shell: sh -e {0}
2026-05-25T15:21:28.7858705Z ##[endgroup]
2026-05-25T15:21:28.7965391Z ##[group]Run '/home
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Full (Run #26407603058)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9340 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26407603058)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26407603058/job/77734885817)
[查看 Job: e2e-full (1ac10f159a09897baada01b14b6a0dd6442aefd6) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26407603058/job/77734885820)

**日志片段**:
```
2026-05-25T16:02:27.4894017Z   UV_NO_CACHE: 1
2026-05-25T16:02:27.4894222Z   UV_SYSTEM_PYTHON: 1
2026-05-25T16:02:27.4894393Z ##[endgroup]
2026-05-25T16:02:27.4982172Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-25T16:02:27.4982950Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-25T16:02:27.4983199Z ##[endgroup]
2026-05-25T16:02:27.9564479Z (node:1565) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Light (Run #26405794147)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9340 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26405794147)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26405794147/job/77728789183)

**日志片段**:
```
2026-05-25T14:37:04.1737952Z [31m-                original_seq_lens = original_seq_lens - num_rejected_tokens_gpu[:batch_size] [m
2026-05-25T14:37:04.1739129Z [32m+[m[32m                original_seq_lens = original_seq_lens - num_rejected_tokens_gpu[:batch_size][m
2026-05-25T14:37:04.1739853Z  [m
2026-05-25T14:37:04.1740442Z          copy_and_expand_dflash_inputs_kernel_single_grid[1,]([m
2026-05-25T14:37:04.1741231Z              # Inputs[m
2026-05-25T14:37:04.1742104Z [36m@@ -134,9 +1
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26407603049)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#26407603058)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26405794147)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T19:41:29.358425+00:00
