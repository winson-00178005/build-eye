---
report_id: 5c07f526
pr_number: null
group_key: run-29795113451
generated_at: 2026-07-21T06:30:59.446978+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-29795113451

## 概要

run-29795113451 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#29795113451) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #29795113451)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/29795113451)
[查看 Job: e2e-light (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/29795113451/job/88525286487)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/29795113451/job/88525286489)
[查看 Job: smart test (39910f2b25aacc09f5e7f166cdf0030b19f8b9e8) / smart-ut (cpu x0)](https://github.com/vllm-project/vllm-ascend/actions/runs/29795113451/job/88525286499)

**日志片段**:
```
2026-07-21T02:18:21.7265258Z   image_310p: swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-beta.1-310p-ubuntu22.04-py3.11
2026-07-21T02:18:21.7266542Z   type: light
2026-07-21T02:18:21.7268017Z   contains_310: true
2026-07-21T02:18:21.7268782Z   continue_on_error: false
2026-07-21T02:18:21.7269473Z   ref: 
2026-07-21T02:18:21.7270044Z   singlecard_tests: 
2026-07-21T02:18:21.7270691Z   multicard_2_tests: 
...
2026-07-21T02:25:32.8416697Z             )[90m[39;49;00m
2026-07
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#29795113451)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-07-21T06:30:59.447006+00:00
