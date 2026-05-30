---
report_id: 358fc6fe
pr_number: null
group_key: run-26688687145
generated_at: 2026-05-30T17:06:57.939253+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26688687145

## 概要

run-26688687145 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26688687145) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26688687145)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26688687145)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26688687145/job/78661229609)

**日志片段**:
```
2026-05-30T16:17:37.6251515Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-05-30T16:17:38.0236069Z ============================
2026-05-30T16:17:38.0247585Z [0;32mRunning mypy for vllm_ascend on python version: 3.10[0m
2026-05-30T16:17:44.6967177Z ##[error]vllm_ascend/distributed/ec_transfer/e_mooncake_backend.py:15: error: Item "None" of "Any | None" has no attribute "put"  [union-attr]
2026-05-30T16:17:44.6976103Z ##[error]vllm_ascend/distributed/ec_transfer
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26688687145)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-30T17:06:57.939281+00:00
