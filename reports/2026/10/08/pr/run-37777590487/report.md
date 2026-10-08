---
report_id: 7d040f11
pr_number: null
group_key: run-37777590487
generated_at: 2026-10-08T21:05:40.883664+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-37777590487

## 概要

run-37777590487 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#37777590487) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #37777590487)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313481960)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313481986)
[查看 Job: e2e-upstream_singlecard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313482221)
[查看 Job: e2e-upstream_singlecard (3, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313482255)
[查看 Job: e2e-upstream_singlecard (1, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313482322)
[查看 Job: e2e-upstream_singlecard (2, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313482350)
[查看 Job: e2e-upstream_online (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37777590487/job/113313482360)

**日志片段**:
```
2026-10-08T12:36:28.1642766Z (node:402) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-10-08T12:36:28.1643487Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-10-08T12:36:28.5206419Z /__w/_temp/81b25491-d88a-4eb0-8697-9edce2935cf5.sh: line 1: npu-smi: command not found
2026-10-08T12:36:28.5301865Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#37777590487)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-10-08T21:05:40.883688+00:00
