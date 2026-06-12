---
report_id: e21631a5
pr_number: 10349
group_key: pr-10349
generated_at: 2026-06-12T08:28:53.960870+00:00
overall_classification: infrastructure
total_failed_workflows: 2
category_counts:
  code: 0
  infrastructure: 2
  interference: 0
---

# 构建失败报告: PR #10349

## 概要

PR #10349 触发了 2 个 workflow，均失败。

- **基础设施问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#27393624834) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#27393624857) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. E2E-Full (Run #27393624834)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27393624834)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #27393624857)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27393624857)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: 基础设施问题

### 优先建议

- **E2E-Full (#27393624834)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#27393624857)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-06-12T08:28:53.960899+00:00
