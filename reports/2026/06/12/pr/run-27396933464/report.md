---
report_id: 5de84301
pr_number: null
group_key: run-27396933464
generated_at: 2026-06-12T08:28:53.960741+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27396933464

## 概要

run-27396933464 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Docs link check (#27396933464) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. Docs link check (Run #27396933464)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27396933464)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/27396933464/job/80966098315)

**日志片段**:
```
2026-06-12T05:39:08.1058146Z   token: ***
...
2026-06-12T05:39:08.1058628Z   fail_on_initial_diff_error: false
2026-06-12T05:39:08.1058886Z   fail_on_submodule_diff_error: false
2026-06-12T05:39:08.1059153Z   negation_patterns_first: false
2026-06-12T05:39:08.1059385Z   matrix: false
2026-06-12T05:39:08.1059758Z   exclude_submodules: false
...
2026-06-12T05:39:20.1391151Z Using cached wheel-0.47.0-py3-none-any.whl (32 kB)
...
2026-06-12T05:39:26.4752656Z 
2026-06-12T05:39:26.4759196Z ERROR: pip'
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Docs link check (#27396933464)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-12T08:28:53.960764+00:00
