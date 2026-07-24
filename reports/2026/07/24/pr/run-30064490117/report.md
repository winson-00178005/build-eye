---
report_id: 0e136e8d
pr_number: null
group_key: run-30064490117
generated_at: 2026-07-24T06:28:22.825337+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-30064490117

## 概要

run-30064490117 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#30064490117) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #30064490117)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/30064490117)
[查看 Job: e2e-upstream_online (0, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30064490117/job/89392813761)
[查看 Job: e2e-upstream_multicard (0, 9.0.1-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/30064490117/job/89392813794)
[查看 Job: e2e-upstream_multicard (0, 9.0.1-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/30064490117/job/89392813808)
[查看 Job: e2e-upstream_singlecard (1, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30064490117/job/89392813828)

**日志片段**:
```
2026-07-24T03:35:12.0481735Z (node:491) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-07-24T03:35:12.0482475Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-07-24T03:35:12.3591027Z /__w/_temp/9a673e90-9ba1-4602-b28a-97f20a99a442.sh: line 1: npu-smi: command not found
2026-07-24T03:35:12.3713124Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#30064490117)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-24T06:28:22.825369+00:00
