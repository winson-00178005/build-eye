---
report_id: a2021235
pr_number: 10737
group_key: pr-10737
generated_at: 2026-06-21T08:29:19.190834+00:00
overall_classification: infrastructure
total_failed_workflows: 2
category_counts:
  code: 0
  infrastructure: 2
  interference: 0
---

# 构建失败报告: PR #10737

## 概要

PR #10737 触发了 2 个 workflow，均失败。

- **基础设施问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27896907602) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27896907628) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. E2E-Full (Run #27896907602)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27896907602)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #27896907628)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27896907628)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: 基础设施问题

### 优先建议

- **E2E-Full (#27896907602)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27896907628)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-06-21T08:29:19.190911+00:00
