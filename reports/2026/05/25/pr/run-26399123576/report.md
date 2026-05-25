---
report_id: d383141f
pr_number: null
group_key: run-26399123576
generated_at: 2026-05-25T14:55:27.551304+00:00
overall_classification: infrastructure
total_failed_workflows: 1
category_counts:
  code: 0
  infrastructure: 1
  interference: 0
---

# 构建失败报告: run-26399123576

## 概要

run-26399123576 触发了 1 个 workflow，均失败。

- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26399123576) | 基础设施问题 | 低 | 构建超时 |


## Workflow 详细分析
### 1. E2E-Light (Run #26399123576)

- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 构建超时

**分析推理**: 检测到基础设施问题: timeout。 问题出现在 job 'e2e-light (v0.20.2) / singlecard-light (0)' 中。 Runner: linux-aarch64-a2b3-1-zsnst-runner-lxzft。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- timeout: `timed\s+out`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26399123576)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26399123576/job/77709474408)

**日志片段**:
```
2026-05-25T12:44:06.9495719Z ##[endgroup]
2026-05-25T12:44:06.9496152Z ##[group]Setting up auth
2026-05-25T12:44:06.9498933Z Removing SSH command configuration
2026-05-25T12:44:06.9509091Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-05-25T12:44:06.9585527Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-05-25T12:44:07.009
```

**建议**:
- 优先: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

## 修复建议

**整体根因**: 基础设施问题

### 优先建议

- **E2E-Light (#26399123576)**: 重新触发构建 (低成本) - 超时可能是暂时性 Runner 问题

---
报告生成时间: 2026-05-25T14:55:27.551322+00:00
