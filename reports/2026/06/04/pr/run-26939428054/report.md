---
report_id: 42d005fa
pr_number: null
group_key: run-26939428054
generated_at: 2026-06-04T08:24:28.629604+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26939428054

## 概要

run-26939428054 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26939428054) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26939428054)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26939428054)
[查看 Job: lint-and-select-tests](https://github.com/vllm-project/vllm-ascend/actions/runs/26939428054/job/79476959581)

**日志片段**:
```
2026-06-04T08:12:33.7215173Z                  buf = self.routed_experts_capturer.get_device_buffer()[m
2026-06-04T08:12:33.7215703Z                  total = scheduler_output.total_num_scheduled_tokens[m
2026-06-04T08:12:33.7216336Z                  self.routed_experts_cpu[:total].copy_(buf[:total], non_blocking=True)[m
2026-06-04T08:12:33.7682803Z ##[error]Error: failed to run script step: Error: command terminated with non-zero exit code: command terminated with exit code 1
2026-06-04T08:12:
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26939428054)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-04T08:24:28.629625+00:00
