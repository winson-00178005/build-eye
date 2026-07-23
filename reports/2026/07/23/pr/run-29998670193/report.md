---
report_id: 9e090fcb
pr_number: null
group_key: run-29998670193
generated_at: 2026-07-23T11:52:53.008364+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-29998670193

## 概要

run-29998670193 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#29998670193) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #29998670193)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193)
[查看 Job: e2e-upstream_multicard (0, 9.0.1-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193/job/89178811764)
[查看 Job: e2e-upstream_online (0, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193/job/89178811776)
[查看 Job: e2e-upstream_singlecard (0, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193/job/89178811779)
[查看 Job: e2e-upstream_singlecard (3, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193/job/89178811800)
[查看 Job: e2e-upstream_multicard (0, 9.0.1-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193/job/89178811804)
[查看 Job: e2e-upstream_singlecard (2, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29998670193/job/89178811930)

**日志片段**:
```
2026-07-23T10:19:25.1206764Z (node:479) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-07-23T10:19:25.1207594Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-07-23T10:19:25.5805280Z /__w/_temp/075a49c5-e69a-4d4e-bc23-f4b6d393fddd.sh: line 1: npu-smi: command not found
2026-07-23T10:19:25.6002573Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#29998670193)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-23T11:52:53.008399+00:00
