---
report_id: 5328b06d
pr_number: 9455
group_key: pr-9455
generated_at: 2026-05-25T03:09:14.594850+00:00
overall_classification: code
total_failed_workflows: 3
category_counts:
  code: 3
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9455

## 概要

PR #9455 触发了 3 个 workflow，均失败。

- **代码问题**: 3 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#26380298217) | PR代码问题 | 中 | 编译错误 |
| 2 | E2E-upstream (#26379330298) | PR代码问题 | 中 | 编译错误 |
| 3 | E2E-upstream (#26378342049) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #26380298217)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9455 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26380298217)
[查看 Job: e2e-upstream_singlecard (2, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26380298217/job/77648098711)
[查看 Job: e2e-upstream_singlecard (1, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26380298217/job/77648098715)
[查看 Job: e2e-upstream_a2_2 (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26380298217/job/77648098718)
[查看 Job: e2e-upstream_singlecard (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26380298217/job/77648098719)
[查看 Job: e2e-upstream_singlecard (3, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26380298217/job/77648098721)

**日志片段**:
```
2026-05-25T02:54:45.4063605Z       1 warning generated.
2026-05-25T02:54:45.4063670Z       1 warning generated.
2026-05-25T02:54:45.4063756Z       gmake: *** [Makefile:156: all] Error 2
2026-05-25T02:54:45.4063846Z 
2026-05-25T02:54:45.4063853Z 
2026-05-25T02:54:46.7477406Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-25T02:54:46.7534550Z hint: Build failures usually indicate a problem with the package o
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-upstream (Run #26379330298)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9455 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26379330298)
[查看 Job: e2e-upstream_singlecard (2, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26379330298/job/77645434577)
[查看 Job: e2e-upstream_singlecard (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26379330298/job/77645434583)
[查看 Job: e2e-upstream_singlecard (1, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26379330298/job/77645434584)
[查看 Job: e2e-upstream_singlecard (3, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26379330298/job/77645434587)

**日志片段**:
```
2026-05-25T02:19:48.3452007Z       1 warning generated.
2026-05-25T02:19:48.3452077Z       1 warning generated.
2026-05-25T02:19:48.3452167Z       gmake: *** [Makefile:156: all] Error 2
2026-05-25T02:19:48.3452176Z 
2026-05-25T02:19:48.3452181Z 
2026-05-25T02:19:49.8046949Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-25T02:19:49.8105001Z hint: Build failures usually indicate a problem with the package o
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-upstream (Run #26378342049)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9455 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26378342049)
[查看 Job: e2e-upstream_singlecard (1, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26378342049/job/77642697286)
[查看 Job: e2e-upstream_singlecard (2, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26378342049/job/77642697287)
[查看 Job: e2e-upstream_singlecard (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26378342049/job/77642697292)
[查看 Job: e2e-upstream_singlecard (3, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26378342049/job/77642697296)

**日志片段**:
```
2026-05-25T01:37:01.4732674Z       1 warning generated.
2026-05-25T01:37:01.4732736Z       1 warning generated.
2026-05-25T01:37:01.4732817Z       gmake: *** [Makefile:156: all] Error 2
2026-05-25T01:37:01.4732824Z 
2026-05-25T01:37:01.4732829Z 
2026-05-25T01:37:02.8090340Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-25T01:37:02.8135625Z hint: Build failures usually indicate a problem with the package o
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#26380298217)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-upstream (#26379330298)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-upstream (#26378342049)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T03:09:14.594917+00:00
