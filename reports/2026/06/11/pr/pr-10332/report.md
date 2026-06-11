---
report_id: 899dcdf8
pr_number: 10332
group_key: pr-10332
generated_at: 2026-06-11T08:50:02.041119+00:00
overall_classification: code
total_failed_workflows: 3
category_counts:
  code: 2
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #10332

## 概要

PR #10332 触发了 3 个 workflow，均失败。

- **代码问题**: 2 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#27334042963) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | Docs link check (#27330744795) | PR代码问题 | 中 | 编译错误 |
| 3 | Docs link check (#27330515945) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #27334042963)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27334042963)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. Docs link check (Run #27330744795)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10332 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27330744795)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/27330744795/job/80742318896)

**日志片段**:
```
2026-06-11T07:22:43.0280091Z   token: ***
...
2026-06-11T07:22:43.0280562Z   fail_on_initial_diff_error: false
2026-06-11T07:22:43.0280824Z   fail_on_submodule_diff_error: false
2026-06-11T07:22:43.0281084Z   negation_patterns_first: false
2026-06-11T07:22:43.0281314Z   matrix: false
2026-06-11T07:22:43.0281697Z   exclude_submodules: false
...
2026-06-11T07:23:41.9300696Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-11T07:23:48.2792820Z 
2026-06-11T07:23:48.2803720Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. Docs link check (Run #27330515945)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10332 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27330515945)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/27330515945/job/80741547527)

**日志片段**:
```
2026-06-11T07:17:47.7844857Z   token: ***
...
2026-06-11T07:17:47.7845314Z   fail_on_initial_diff_error: false
2026-06-11T07:17:47.7845572Z   fail_on_submodule_diff_error: false
2026-06-11T07:17:47.7845823Z   negation_patterns_first: false
2026-06-11T07:17:47.7846049Z   matrix: false
2026-06-11T07:17:47.7846422Z   exclude_submodules: false
...
2026-06-11T07:17:59.3301527Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-11T07:18:05.7633608Z 
2026-06-11T07:18:05.7640544Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#27334042963)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **Docs link check (#27330744795)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Docs link check (#27330515945)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-11T08:50:02.041171+00:00
