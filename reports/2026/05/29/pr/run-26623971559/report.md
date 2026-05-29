---
report_id: ca5a4d14
pr_number: null
group_key: run-26623971559
generated_at: 2026-05-29T07:58:27.953372+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26623971559

## 概要

run-26623971559 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26623971559) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26623971559)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26623971559)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26623971559/job/78456318122)

**日志片段**:
```
2026-05-29T07:24:01.9389577Z          flashcomm2_oproj_tp_size,[m
2026-05-29T07:24:01.9389835Z      )[m
2026-05-29T07:24:01.9390016Z  [m
2026-05-29T07:24:01.9816159Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-05-29T07:24:01.9862823Z ##[error]Process completed with exit code 1.
2026-05-29T07:24:02.0065483Z ##[error]Executing the custom container implementation failed. Please contact your self hosted run
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26623971559)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-29T07:58:27.953391+00:00
