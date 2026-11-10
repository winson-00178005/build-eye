---
report_id: cc729822
pr_number: 21293
group_key: pr-21293
generated_at: 2026-11-10T00:01:24.602815+00:00
overall_classification: infrastructure
total_failed_workflows: 1
category_counts:
  code: 0
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #21293

## 概要

PR #21293 触发了 1 个 workflow，均失败。

- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Image build lint (#42633120451) | 基础设施问题 | 低 | 无失败job信息 |


## Workflow 详细分析
### 1. Image build lint (Run #42633120451)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/42633120451)
[查看 PR #21293](https://github.com/vllm-project/vllm-ascend/pull/21293)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: 基础设施问题

### 优先建议

- **Image build lint (#42633120451)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复

---
报告生成时间: 2026-11-10T00:01:24.602842+00:00
