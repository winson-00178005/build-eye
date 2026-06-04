---
report_id: bb718895
pr_number: null
group_key: run-26768908902
generated_at: 2026-06-01T23:30:29.782543+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26768908902

## 概要

run-26768908902 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26768908902) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26768908902)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26768908902)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26768908902/job/78902866991)

**日志片段**:
```
2026-06-01T16:51:59.3301029Z  def split_qkv_rmsnorm_rope_simt_impl_fake([m
2026-06-01T16:51:59.3301441Z      input: torch.Tensor,[m
2026-06-01T16:51:59.3301824Z      cos_sin_cache: torch.Tensor,[m
2026-06-01T16:51:59.3693520Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-01T16:51:59.3767473Z ##[error]Process completed with exit code 1.
2026-06-01T16:51:59.3887363Z ##[error]Executing the custom containe
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26768908902)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-01T23:30:29.782569+00:00
