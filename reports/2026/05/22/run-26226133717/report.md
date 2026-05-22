---
report_id: 08043fdf
pr_number: null
group_key: run-26266075659
generated_at: 2026-05-22T03:55:44.683289+00:00
overall_classification: code
total_failed_workflows: 1
category_counts:
  code: 1
  infrastructure: 0
  interference: 0
---

# 构建失败报告: run-26266075659

## 概要

run-26266075659 触发了 1 个 workflow，均失败。

- **代码问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Full (#26266075659) | PR代码问题 | 高 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Full (Run #26266075659)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659)
[查看 Job: e2e-full (0d4d334eaa583b9c09aa4eb7538c22db99fd84b3) / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650024)
[查看 Job: e2e-full (0d4d334eaa583b9c09aa4eb7538c22db99fd84b3) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650025)
[查看 Job: e2e-full (v0.20.2) / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650059)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650075)
[查看 Job: e2e-full (v0.20.2) / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650091)
[查看 Job: e2e-full (0d4d334eaa583b9c09aa4eb7538c22db99fd84b3) / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650098)
[查看 Job: e2e-full (v0.20.2) / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26266075659/job/77309650126)

**日志片段**:
```
2026-05-22T03:25:07.7294670Z   UV_NO_CACHE: 1
2026-05-22T03:25:07.7294962Z   UV_SYSTEM_PYTHON: 1
2026-05-22T03:25:07.7295165Z ##[endgroup]
2026-05-22T03:25:07.7373824Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T03:25:07.7374863Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T03:25:07.7375158Z ##[endgroup]
2026-05-22T03:25:08.1942984Z (node:1315) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Full (#26266075659)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T03:55:44.683315+00:00
