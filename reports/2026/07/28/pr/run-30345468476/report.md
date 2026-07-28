---
report_id: d1d4516c
pr_number: null
group_key: run-30345468476
generated_at: 2026-07-28T12:00:06.334480+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-30345468476

## 概要

run-30345468476 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#30345468476) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #30345468476)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/30345468476)
[查看 Job: e2e-upstream_online (0, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30345468476/job/90231429257)
[查看 Job: e2e-upstream_singlecard (1, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30345468476/job/90231429283)
[查看 Job: e2e-upstream_singlecard (0, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30345468476/job/90231429313)
[查看 Job: e2e-upstream_singlecard (2, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30345468476/job/90231429335)
[查看 Job: e2e-upstream_singlecard (3, 9.0.1-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/30345468476/job/90231429396)

**日志片段**:
```
2026-07-28T09:15:29.0309892Z (node:490) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-07-28T09:15:29.0310570Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-07-28T09:15:29.3372371Z /__w/_temp/ead3bda7-92b2-4d59-a76f-abbc600a192f.sh: line 1: npu-smi: command not found
2026-07-28T09:15:29.3441864Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#30345468476)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-28T12:00:06.334502+00:00
