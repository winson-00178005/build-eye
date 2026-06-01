---
report_id: 79ca3a1a
pr_number: null
group_key: run-26769782661
generated_at: 2026-06-01T20:23:09.659189+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26769782661

## 概要

run-26769782661 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26769782661) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26769782661)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26769782661)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26769782661/job/78905949044)

**日志片段**:
```
2026-06-01T17:09:06.3691401Z  def split_qkv_rmsnorm_rope_simt_impl_fake([m
2026-06-01T17:09:06.3692361Z      input: torch.Tensor,[m
2026-06-01T17:09:06.3693006Z      cos_sin_cache: torch.Tensor,[m
2026-06-01T17:09:06.4123906Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-01T17:09:06.4221574Z ##[error]Process completed with exit code 1.
2026-06-01T17:09:06.4336770Z ##[error]Executing the custom containe
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26769782661)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-01T20:23:09.659213+00:00
