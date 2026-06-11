---
report_id: 03af684c
pr_number: null
group_key: run-27353188770
generated_at: 2026-06-11T18:50:53.574605+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27353188770

## 概要

run-27353188770 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27353188770) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27353188770)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

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

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27353188770)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-11T18:50:53.574630+00:00
