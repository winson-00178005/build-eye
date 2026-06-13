---
report_id: dac094d8
pr_number: null
group_key: run-27459434285
generated_at: 2026-06-13T17:24:55.497293+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27459434285

## 概要

run-27459434285 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27459434285) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27459434285)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27459434285)
[查看 Job: e2e-light (v0.18.0) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27459434285/job/81170402114)
[查看 Job: e2e-light (v0.18.0) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27459434285/job/81170402115)

**日志片段**:
```
2026-06-13T07:14:52.5958051Z   image: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-910b-ubuntu22.04-py3.11
2026-06-13T07:14:52.5958708Z   type: light
2026-06-13T07:14:52.5959434Z   contains_310: false
2026-06-13T07:14:52.5959745Z   continue_on_error: true
2026-06-13T07:14:52.5960074Z ##[endgroup]
...
2026-06-13T07:14:52.6760673Z ##[group]Run '/home/runner/k8s/index.js'
...
2026-06-13T07:18:01.0893133Z     Uninstalling numpy-2.4.4:
...
2026-06-13T07:18:43.9078354Z 
2026-06
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27459434285)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-13T17:24:55.497321+00:00
