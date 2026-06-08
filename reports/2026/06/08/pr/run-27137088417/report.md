---
report_id: 4cc4816b
pr_number: null
group_key: run-27137088417
generated_at: 2026-06-08T14:10:53.033123+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27137088417

## 概要

run-27137088417 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#27137088417) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #27137088417)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27137088417)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/27137088417/job/80092206792)

**日志片段**:
```
2026-06-08T12:19:18.9186947Z   token: ***
...
2026-06-08T12:19:18.9187418Z   fail_on_initial_diff_error: false
2026-06-08T12:19:18.9187665Z   fail_on_submodule_diff_error: false
2026-06-08T12:19:18.9187916Z   negation_patterns_first: false
2026-06-08T12:19:18.9188140Z   matrix: false
2026-06-08T12:19:18.9188514Z   exclude_submodules: false
...
2026-06-08T12:19:32.1253784Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-08T12:19:38.6417449Z 
2026-06-08T12:19:38.6425493Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#27137088417)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-08T14:10:53.033151+00:00
