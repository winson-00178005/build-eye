---
report_id: 94d89fa1
pr_number: null
group_key: run-27673404314
generated_at: 2026-06-17T09:06:39.683566+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27673404314

## 概要

run-27673404314 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#27673404314) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #27673404314)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27673404314)
[查看 Job: e2e-light (v0.18.0) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27673404314/job/81843416606)
[查看 Job: e2e-light (v0.18.0) / multicard-2-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/27673404314/job/81843416651)

**日志片段**:
```
2026-06-17T07:41:24.2547134Z   image: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-910b-ubuntu22.04-py3.11
2026-06-17T07:41:24.2548354Z   type: light
2026-06-17T07:41:24.2549750Z   contains_310: false
2026-06-17T07:41:24.2550421Z   continue_on_error: true
2026-06-17T07:41:24.2551094Z ##[endgroup]
...
2026-06-17T07:41:24.3885375Z ##[group]Run '/home/runner/k8s/index.js'
...
2026-06-17T07:45:24.3856523Z     Uninstalling numpy-2.4.4:
...
2026-06-17T07:46:26.7948698Z 
2026-06
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#27673404314)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-17T09:06:39.683596+00:00
