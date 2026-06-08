---
report_id: 4970b610
pr_number: 10193
group_key: pr-10193
generated_at: 2026-06-08T23:15:22.771344+00:00
overall_classification: code
total_failed_workflows: 3
category_counts:
  code: 1
  infrastructure: 2
  interference: 0
---

# 构建失败报告: PR #10193

## 概要

PR #10193 触发了 3 个 workflow，均失败。

- **代码问题**: 1 次
- **基础设施问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27141470245) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27141470344) | 基础设施问题 | 低 | 无失败job信息 |
| 3 | E2E-Light (#27136811221) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #27141470245)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27141470245)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #27141470344)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27141470344)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 3. E2E-Light (Run #27136811221)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10193 代码中。 建议检查 PR 的代码修改和测试用例。

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

- **E2E-Full (#27141470245)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27141470344)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27136811221)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-08T23:15:22.771402+00:00
