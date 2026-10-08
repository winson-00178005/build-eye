---
report_id: 699ea163
pr_number: null
group_key: run-37753153248
generated_at: 2026-10-08T11:12:09.311704+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-37753153248

## 概要

run-37753153248 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#37753153248) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-upstream (Run #37753153248)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/37753153248)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 4)](https://github.com/vllm-project/vllm-ascend/actions/runs/37753153248/job/113232196465)
[查看 Job: e2e-upstream_multicard (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 2)](https://github.com/vllm-project/vllm-ascend/actions/runs/37753153248/job/113232196497)
[查看 Job: e2e-upstream_online (0, 9.2.0_20260928212200-910b-ubuntu22.04-py3.12, 1)](https://github.com/vllm-project/vllm-ascend/actions/runs/37753153248/job/113232196541)

**日志片段**:
```
2026-10-08T08:59:40.5062706Z ##[group]Run '/home/runner/k8s/index.js'
2026-10-08T08:59:40.5065403Z shell: /home/runner/externals/node20/bin/node {0}
2026-10-08T08:59:40.5065946Z ##[endgroup]
2026-10-08T09:05:12.9643938Z ##[error]Error: pod failed to come online:
Pod linux-aarch64-a2b3-0-ccj57-runner-xx7nv-workflow has unrecoverable errors:
  â container "job": ImagePullBackOff (failed for 301s, exceeding the 300s grace period)
    Back-off pulling image "swr.cn-north-12.myhuaweicloud.com/base_
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-upstream (#37753153248)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-10-08T11:12:09.311733+00:00
