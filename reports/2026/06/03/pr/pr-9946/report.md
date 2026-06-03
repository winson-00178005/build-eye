---
report_id: 194ff376
pr_number: 9946
group_key: pr-9946
generated_at: 2026-06-03T19:52:17.200477+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 1
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #9946

## 概要

PR #9946 触发了 2 个 workflow，均失败。

- **代码问题**: 1 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Image build lint (#26894813833) | 基础设施问题 | 低 | 无失败job信息 |
| 2 | Release Code and Wheel (#26894814044) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Image build lint (Run #26894813833)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 无失败job信息

**分析推理**: 无法获取job详情，默认归类为基础设施问题

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26894813833)
[查看 PR #9946](https://github.com/vllm-project/vllm-ascend/pull/9946)

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 2. Release Code and Wheel (Run #26894814044)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9946 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26894814044)
[查看 PR #9946](https://github.com/vllm-project/vllm-ascend/pull/9946)
[查看 Job: build and release wheel (310P) (ubuntu-24.04, 3.10)](https://github.com/vllm-project/vllm-ascend/actions/runs/26894814044/job/79330676061)

**日志片段**:
```
2026-06-03T15:25:42.8953221Z #1 DONE 0.0s
2026-06-03T15:25:42.8953347Z 
2026-06-03T15:25:42.8953636Z #2 [internal] load metadata for quay.io/ascend/manylinux:9.1.0-beta.1-310p-manylinux_2_28-py3.10
2026-06-03T15:25:42.9819939Z #2 ERROR: quay.io/ascend/manylinux:9.1.0-beta.1-310p-manylinux_2_28-py3.10: not found
2026-06-03T15:25:42.9946050Z ------
2026-06-03T15:25:42.9946996Z  > [internal] load metadata for quay.io/ascend/manylinux:9.1.0-beta.1-310p-manylinux_2_28-py3.10:
2026-06-03T15:25:42.9948
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Image build lint (#26894813833)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **Release Code and Wheel (#26894814044)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-03T19:52:17.200515+00:00
