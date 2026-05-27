---
report_id: eb22340f
pr_number: null
group_key: run-26486737902
generated_at: 2026-05-27T04:01:52.457751+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26486737902

## 概要

run-26486737902 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26486737902) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #26486737902)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26486737902)
[查看 Job: e2e-comment (v0.20.2) / 310p singlecard](https://github.com/vllm-project/vllm-ascend/actions/runs/26486737902/job/77995824304)

**日志片段**:
```
2026-05-27T02:18:55.6292147Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.0.0-310p-ubuntu22.04-py3.11
2026-05-27T02:18:55.6293538Z   type: comment
2026-05-27T02:18:55.6295340Z   contains_310: false
2026-05-27T02:18:55.6296252Z   continue_on_error: false
2026-05-27T02:18:55.6297209Z   ref: 9a1b5c15c747d95a33fd5ac2c3557f40d5738c10
2026-05-27T02:18:55.6298189Z   singlecard_tests: 
2026-05-27T02:18:55.6299021Z   multicard_2_tests: 
...
2026-05-27T02:33:05.4197230Z `
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26486737902)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-27T04:01:52.457777+00:00
