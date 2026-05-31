---
report_id: 242fe66a
pr_number: null
group_key: run-26704491432
generated_at: 2026-05-31T07:48:41.052969+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26704491432

## 概要

run-26704491432 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26704491432) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26704491432)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `AttributeError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26704491432)
[查看 Job: smart test (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / smart-ut (a2 x1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26704491432/job/78703266074)
[查看 Job: smart test (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26704491432/job/78703266082)
[查看 Job: smart test (v0.20.2) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26704491432/job/78703266089)

**日志片段**:
```
2026-05-31T06:04:25.1254212Z >       [94mraise[39;49;00m [96mAttributeError[39;49;00m([90m[39;49;00m
2026-05-31T06:04:25.1255338Z             [33mf[39;49;00m[33m"[39;49;00m[33m'[39;49;00m[33m{[39;49;00m[96mtype[39;49;00m([96mself[39;49;00m).[91m__name__[39;49;00m[33m}[39;49;00m[33m'[39;49;00m[33m object has no attribute [39;49;00m[33m'[39;49;00m[33m{[39;49;00mname[33m}[39;49;00m[33m'[39;49;00m[33m"[39;49;00m[90m[39;49;00m
2026-05-31T06:04:25.1256197Z        
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26704491432)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-31T07:48:41.052991+00:00
