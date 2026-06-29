---
report_id: e8f9ffda
pr_number: null
group_key: run-28371239090
generated_at: 2026-06-29T14:07:38.217412+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-28371239090

## 概要

run-28371239090 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#28371239090) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #28371239090)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `ModuleNotFoundError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/28371239090)
[查看 Job: e2e-light (v0.18.0) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/28371239090/job/84049832009)

**日志片段**:
```
2026-06-29T12:18:35.5220925Z   image: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-910b-ubuntu22.04-py3.11
2026-06-29T12:18:35.5222153Z   type: light
2026-06-29T12:18:35.5223660Z   contains_310: false
2026-06-29T12:18:35.5224361Z   continue_on_error: true
2026-06-29T12:18:35.5225058Z ##[endgroup]
...
2026-06-29T12:18:35.6523768Z ##[group]Run '/home/runner/k8s/index.js'
...
2026-06-29T12:20:12.3155314Z Collecting tokenizers>=0.21.1 (from vllm==0.18.0+empty)
...
2026-06-29T
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#28371239090)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-29T14:07:38.217437+00:00
