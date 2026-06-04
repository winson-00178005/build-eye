---
report_id: 43216646
pr_number: null
group_key: run-26586266714
generated_at: 2026-05-28T23:19:23.883127+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26586266714

## 概要

run-26586266714 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26586266714) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26586266714)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `ModuleNotFoundError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26586266714)
[查看 Job: e2e-light (v0.20.2) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26586266714/job/78334508235)
[查看 Job: e2e-light (7e1b45a09252a5b513cd83116aa7a2f310220c34) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26586266714/job/78334508329)
[查看 Job: e2e-light (7e1b45a09252a5b513cd83116aa7a2f310220c34) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26586266714/job/78334508335)
[查看 Job: e2e-light (v0.20.2) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26586266714/job/78334508426)

**日志片段**:
```
2026-05-28T16:09:02.7302870Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-28T16:09:02.7303850Z   type: light
2026-05-28T16:09:02.7305265Z   contains_310: true
2026-05-28T16:09:02.7305785Z   continue_on_error: true
2026-05-28T16:09:02.7306460Z   ref: 
2026-05-28T16:09:02.7306888Z   singlecard_tests: 
2026-05-28T16:09:02.7307397Z   multicard_2_tests: 
...
2026-05-28T16:20:13.8852071Z [2026-05-28 16:20:13.883728][UC][I] Registere
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26586266714)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-28T23:19:23.883152+00:00
