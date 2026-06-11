---
report_id: ad8506ae
pr_number: null
group_key: run-27353478794
generated_at: 2026-06-11T18:50:53.574452+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27353478794

## 概要

run-27353478794 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27353478794) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27353478794)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

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

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27353478794)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-11T18:50:53.574479+00:00
