---
report_id: 765965fe
pr_number: null
group_key: run-27136811221
generated_at: 2026-06-08T14:10:53.033417+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27136811221

## 概要

run-27136811221 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27136811221) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27136811221)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27136811221)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27136811221/job/80091470960)

**日志片段**:
```
2026-06-08T12:18:39.2923030Z [m
2026-06-08T12:18:39.2923552Z [32m+[m[32m        block_size = int(raw_value)[m[41m
2026-06-08T12:18:39.2923903Z [m
2026-06-08T12:18:39.2924325Z [32m+[m[32m    except ValueError as exc:[m[41m
2026-06-08T12:18:39.2924662Z [m
2026-06-08T12:18:39.2925070Z [32m+[m[32m        raise ValueError([m[41m
2026-06-08T12:18:39.2925391Z [m
2026-06-08T12:18:39.2926137Z [32m+[m[32m            f"{DSV4_COMPRESSED_KV_BLOCK_SIZE_ENV} must be an integer in "[m[41
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27136811221)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-08T14:10:53.033443+00:00
