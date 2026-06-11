---
report_id: c1740e14
pr_number: 10349
group_key: pr-10349
generated_at: 2026-06-11T23:24:37.120767+00:00
overall_classification: code
total_failed_workflows: 6
category_counts:
  code: 2
  infrastructure: 4
  interference: 0
---

# 构建失败报告: PR #10349

## 概要

PR #10349 触发了 6 个 workflow，均失败。

- **代码问题**: 2 次
- **基础设施问题**: 4 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27363072972) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27363073401) | 基础设施问题 | 低 | 无失败job信息 |
| 3 | E2E-Full (#27353479170) | 基础设施问题 | 低 | 无失败job信息 |
| 4 | E2E-Light (#27353478794) | PR代码问题 | 中 | 编译错误 |
| 5 | E2E-Light (#27353188770) | PR代码问题 | 中 | 编译错误 |
| 6 | E2E-Full (#27353187727) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. E2E-Full (Run #27363072972)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27363072972)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #27363073401)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27363073401)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 3. E2E-Full (Run #27353479170)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27353479170)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 4. E2E-Light (Run #27353478794)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27353478794)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27353478794/job/80821510801)

**日志片段**:
```
2026-06-11T14:20:56.3861095Z [INFO][m Installing environment for local.
2026-06-11T14:20:56.3861672Z [INFO][m Once installed this environment will be reused.
2026-06-11T14:20:56.3862098Z [INFO][m This may take a few minutes...
2026-06-11T14:20:56.7583304Z An unexpected error has occurred: FileNotFoundError: [Errno 2] No such file or directory: '/root/.cache/pre-commit/repojr1e6g_y/py_env-python3.12/lib/python3.12/site-packages/pip/_vendor/requests/__pycache__'
2026-06-11T14:20:56.7593045Z Che
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. E2E-Light (Run #27353188770)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27353188770)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27353188770/job/80820474732)

**日志片段**:
```
2026-06-11T14:16:28.1440013Z [INFO][m Installing environment for https://github.com/astral-sh/ruff-pre-commit.
2026-06-11T14:16:28.1440776Z [INFO][m Once installed this environment will be reused.
2026-06-11T14:16:28.1441206Z [INFO][m This may take a few minutes...
2026-06-11T14:16:28.4573200Z An unexpected error has occurred: OSError: [Errno 39] Directory not empty: '/root/.cache/pre-commit/repoqnczjq7l/py_env-python3.12/lib/python3.12/site-packages/pip/_internal'
2026-06-11T14:16:28.4582339
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 6. E2E-Full (Run #27353187727)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27353187727)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#27363072972)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27363073401)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Full (#27353479170)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27353478794)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#27353188770)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#27353187727)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-06-11T23:24:37.120840+00:00
