---
report_id: 53861a35
pr_number: null
group_key: run-27531442766
generated_at: 2026-06-15T10:27:17.186593+00:00
overall_classification: infrastructure
total_failed_workflows: 1
category_counts:
  code: 0
  infrastructure: 1
  interference: 0
---

# 构建失败报告: run-27531442766

## 概要

run-27531442766 触发了 1 个 workflow，均失败。

- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-upstream (#27531442766) | 基础设施问题 | 高 | K8s内部服务失败 |


## Workflow 详细分析
### 1. E2E-upstream (Run #27531442766)

- **根因分类**: 基础设施问题
- **置信度**: 高
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'e2e-upstream (linux-aarch64-a2b3-1, 0, 1, 2, 3, false, 4, e2e-upstream_singlecard, 23, pip instal...' 中。 Runner: linux-aarch64-a2b3-1-zsnst-runner-klbpj。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27531442766)
[查看 Job: e2e-upstream (linux-aarch64-a2b3-1, 0, 1, 2, 3, false, 4, e2e-upstream_singlecard, 23, pip instal...](https://github.com/vllm-project/vllm-ascend/actions/runs/27531442766/job/81370443246)
[查看 Job: e2e-upstream (linux-aarch64-a2b3-1, 0, 1, 2, 3, true, 4, e2e-upstream_singlecard_online, 23, pip ...](https://github.com/vllm-project/vllm-ascend/actions/runs/27531442766/job/81370443326)

**日志片段**:
```
2026-06-15T07:43:12.9140761Z   fetch-depth: 1
2026-06-15T07:43:12.9141272Z   fetch-tags: false
2026-06-15T07:43:12.9141800Z   show-progress: true
2026-06-15T07:43:12.9142312Z   lfs: false
2026-06-15T07:43:12.9142784Z   submodules: false
2026-06-15T07:43:12.9143305Z   set-safe-directory: true
2026-06-15T07:43:12.9143847Z env:
2026-06-15T07:43:12.9146821Z   UV_INDEX_STRATEGY: unsafe-best-match
2026-06-15T07:43:12.9147636Z   UV_INSECURE_HOST: cache-service.nginx-pypi-cache.svc.cluster.local
2026-06
```

**建议**:
- 优先: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

## 修复建议

**整体根因**: 基础设施问题

### 优先建议

- **E2E-upstream (#27531442766)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复

---
报告生成时间: 2026-06-15T10:27:17.186615+00:00
