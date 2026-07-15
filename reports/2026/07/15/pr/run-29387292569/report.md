---
report_id: 11b833fc
pr_number: null
group_key: run-29387292569
generated_at: 2026-07-15T06:16:23.498071+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-29387292569

## 概要

run-29387292569 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#29387292569) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #29387292569)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569)
[查看 Job: e2e-upstream_multicard (0, 9.0.0-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218428)
[查看 Job: e2e-upstream_multicard (0, 9.0.0-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218434)
[查看 Job: e2e-upstream_singlecard (1, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218452)
[查看 Job: e2e-upstream_singlecard (2, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218459)
[查看 Job: e2e-upstream_singlecard (3, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218474)
[查看 Job: e2e-upstream_online (0, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218500)
[查看 Job: e2e-upstream_singlecard (0, 9.0.0-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/29387292569/job/87263218600)

**日志片段**:
```
2026-07-15T03:47:10.8093387Z (node:491) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.allocUnsafe(), or Buffer.from() methods instead.
2026-07-15T03:47:10.8094094Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-07-15T03:47:11.2840334Z /__w/_temp/21768d7e-5c60-41de-8328-0600075e5620.sh: line 1: npu-smi: command not found
2026-07-15T03:47:11.2979363Z ##[error]Error: failed to run scr
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#29387292569)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-15T06:16:23.498110+00:00
