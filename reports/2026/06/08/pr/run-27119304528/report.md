---
report_id: c4abab83
pr_number: null
group_key: run-27119304528
generated_at: 2026-06-08T08:59:32.563811+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-27119304528

## 概要

run-27119304528 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27119304528) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27119304528)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528)
[查看 Job: e2e-upstream_a2_2 (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528/job/80032587135)
[查看 Job: e2e-upstream_a2_4 (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528/job/80032587158)
[查看 Job: e2e-upstream_singlecard (1, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528/job/80032587160)
[查看 Job: e2e-upstream_singlecard (3, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528/job/80032587161)
[查看 Job: e2e-upstream_singlecard (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528/job/80032587163)
[查看 Job: e2e-upstream_singlecard (2, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/27119304528/job/80032587169)

**日志片段**:
```
2026-06-08T06:10:28.6433833Z (node:304) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-06-08T06:10:28.6434668Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-08T06:10:29.0848918Z /__w/_temp/ce4b2202-eb29-4599-8d1e-c5083a04fb95.sh: line 1: npu-smi: command not found
2026-06-08T06:10:29.1009165Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#27119304528)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-08T08:59:32.563864+00:00
