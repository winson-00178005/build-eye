---
report_id: 36ff00ff
pr_number: null
group_key: run-28865356823
generated_at: 2026-07-07T23:04:07.359830+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28865356823

## 概要

run-28865356823 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#28865356823) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #28865356823)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28865356823)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/28865356823/job/85613937786)

**日志片段**:
```
2026-07-07T12:16:48.5029556Z  from vllm_ascend.ec_manager.score_encoder_cache import get_score_encoder_cache_config[m
2026-07-07T12:16:48.5029953Z  [m
2026-07-07T12:16:48.5030435Z  # if true, allow tensor initialization and casting with internal format (e.g., NZ)[m
2026-07-07T12:16:48.5405537Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-07-07T12:16:48.5462632Z ##[error]Process completed with exit code 1
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#28865356823)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-07T23:04:07.359872+00:00
