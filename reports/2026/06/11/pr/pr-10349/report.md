---
report_id: e98eefb9
pr_number: 10349
group_key: pr-10349
generated_at: 2026-06-11T18:50:53.573694+00:00
overall_classification: code
total_failed_workflows: 8
category_counts:
  code: 3
  infrastructure: 5
  interference: 0
---

# 构建失败报告: PR #10349

## 概要

PR #10349 触发了 8 个 workflow，均失败。

- **代码问题**: 3 次
- **基础设施问题**: 5 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27363072972) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27363073401) | 基础设施问题 | 低 | 无失败job信息 |
| 3 | E2E-Full (#27354484417) | 基础设施问题 | 低 | 无失败job信息 |
| 4 | E2E-Light (#27354484397) | PR代码问题 | 中 | 编译错误 |
| 5 | E2E-Full (#27353836558) | 基础设施问题 | 低 | 无失败job信息 |
| 6 | E2E-Light (#27353836730) | PR代码问题 | 中 | 编译错误 |
| 7 | E2E-Full (#27348942013) | 基础设施问题 | 低 | 无失败job信息 |
| 8 | E2E-Light (#27348941891) | PR代码问题 | 中 | 编译错误 |


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

### 3. E2E-Full (Run #27354484417)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27354484417)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 4. E2E-Light (Run #27354484397)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27354484397)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27354484397/job/80825078677)

**日志片段**:
```
2026-06-11T14:37:27.0368927Z [INFO][m Installing environment for local.
2026-06-11T14:37:27.0369540Z [INFO][m Once installed this environment will be reused.
2026-06-11T14:37:27.0369972Z [INFO][m This may take a few minutes...
2026-06-11T14:37:43.2471040Z An unexpected error has occurred: CalledProcessError: command: ('/root/.cache/pre-commit/repojr1e6g_y/py_env-python3.12/bin/python', '-mpip', 'install', '.')
2026-06-11T14:37:43.2471730Z return code: 1
2026-06-11T14:37:43.2471954Z stdout:
20
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. E2E-Full (Run #27353836558)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27353836558)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 6. E2E-Light (Run #27353836730)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27353836730)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27353836730/job/80822782986)

**日志片段**:
```
2026-06-11T14:26:11.1643861Z [INFO][m Installing environment for local.
2026-06-11T14:26:11.1644410Z [INFO][m Once installed this environment will be reused.
2026-06-11T14:26:11.1644829Z [INFO][m This may take a few minutes...
2026-06-11T14:26:27.4699854Z An unexpected error has occurred: CalledProcessError: command: ('/root/.cache/pre-commit/repojr1e6g_y/py_env-python3.12/bin/python', '-mpip', 'install', '.')
2026-06-11T14:26:27.4700558Z return code: 1
2026-06-11T14:26:27.4700879Z stdout:
20
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 7. E2E-Full (Run #27348942013)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27348942013)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 8. E2E-Light (Run #27348941891)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10349 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27348941891)
[查看 Job: lint / validate-pr-title](https://github.com/vllm-project/vllm-ascend/actions/runs/27348941891/job/80805110708)

**日志片段**:
```
2026-06-11T13:07:04.0267006Z ##[group]Run '/home/runner/k8s/index.js'
2026-06-11T13:07:04.0276434Z shell: /home/runner/externals/node20/bin/node {0}
2026-06-11T13:07:04.0277660Z ##[endgroup]
2026-06-11T13:07:12.1194171Z ##[error]Error: pod failed to come online with error: Error: Pod linux-amd64-cpu-8-hk-frp8k-runner-m5f8r-workflow is unhealthy with phase status Failed: {}
2026-06-11T13:07:12.1261539Z ##[error]Process completed with exit code 1.
2026-06-11T13:07:12.1301911Z ##[error]Executing th
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#27363072972)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27363073401)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Full (#27354484417)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27354484397)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#27353836558)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27353836730)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Full (#27348942013)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27348941891)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-11T18:50:53.573789+00:00
