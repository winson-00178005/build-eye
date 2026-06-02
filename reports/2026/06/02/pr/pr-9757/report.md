---
report_id: 1f3b0a79
pr_number: 9757
group_key: pr-9757
generated_at: 2026-06-02T08:33:04.387063+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 1
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #9757

## 概要

PR #9757 触发了 2 个 workflow，均失败。

- **代码问题**: 1 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26807146210) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | E2E-Light (#26807146209) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #26807146210)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26807146210)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. E2E-Light (Run #26807146209)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9757 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26807146209)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26807146209/job/79027564510)

**日志片段**:
```
2026-06-02T08:13:30.1525736Z      @staticmethod[m
2026-06-02T08:13:30.1526528Z      def chunk_scaled_dot_kkt_fwd(NT, k, beta, g_cumsum, A, cu_seqlens, chunk_indices, T, B, H, Hg, K, BT, BK):[m
2026-06-02T08:13:30.1527205Z          chunk_scaled_dot_kkt_fwd_kernel[(NT, 1)]([m
2026-06-02T08:13:30.2067659Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-02T08:13:30.2149872Z ##[error]Process completed with ex
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26807146210)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **E2E-Light (#26807146209)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-02T08:33:04.387140+00:00
