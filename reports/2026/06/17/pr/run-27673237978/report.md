---
report_id: 0844b142
pr_number: null
group_key: run-27673237978
generated_at: 2026-06-17T09:06:39.684019+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27673237978

## 概要

run-27673237978 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27673237978) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27673237978)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27673237978)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/27673237978/job/81842302019)

**日志片段**:
```
2026-06-17T07:36:09.0439159Z   and \{len(proxy_state.decoders)} decode clients, {len(proxy_state.pds)} pd clients."
2026-06-17T07:36:11.7837122Z Success: no issues found in 27 source files
2026-06-17T07:36:11.7991588Z [0;32mRunning mypy for tests on python version: 3.10[0m
2026-06-17T07:36:16.3225150Z ##[error]tests/e2e/singlecard/test_laps_scheduling.py:81: error: Argument 2 to "VllmRunner" has incompatible type "**dict[str, object]"; expected "str | None"  [arg-type]
2026-06-17T07:36:16.3233
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27673237978)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-17T09:06:39.684046+00:00
