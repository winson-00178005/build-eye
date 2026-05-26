---
report_id: dcaa6202
pr_number: 9575
group_key: pr-9575
generated_at: 2026-05-26T09:58:18.456782+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9575

## 概要

PR #9575 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26441522721) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26441522721)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation, import_error。 问题出现在 PR #9575 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`
- import_error: `AttributeError`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721/job/77837658064)
[查看 Job: e2e-light (v0.20.2) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721/job/77837658136)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721/job/77837658147)
[查看 Job: e2e-light (v0.20.2) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721/job/77837658215)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / 310p multicards 4cards](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721/job/77837658248)
[查看 Job: e2e-light (1ac10f159a09897baada01b14b6a0dd6442aefd6) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26441522721/job/77837658272)

**日志片段**:
```
2026-05-26T08:41:46.5356758Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-26T08:41:46.5357726Z   type: light
2026-05-26T08:41:46.5358954Z   contains_310: true
2026-05-26T08:41:46.5359454Z   continue_on_error: false
2026-05-26T08:41:46.5359959Z   ref: 
2026-05-26T08:41:46.5360368Z   singlecard_tests: 
2026-05-26T08:41:46.5360838Z   multicard_2_tests: 
...
2026-05-26T09:09:24.4737579Z Processed prompts:   0%|          | 0/4 [00:
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26441522721)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-26T09:58:18.456807+00:00
