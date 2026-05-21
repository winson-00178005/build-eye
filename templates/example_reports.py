"""示例报告模板 - 各类失败类型。"""

CODE_REPORT_TEMPLATE = """---
report_id: sample001
pr_number: 1234
workflow_run_id: 567890
generated_at: 2024-01-15T12:00:00
classification: code
confidence: high
category_detail: 测试断言失败
---

# 构建失败报告: PR #1234

## 概要

PR #1234 构建失败，根因: 测试断言失败。测试 test_inference.py 断言期望输出形状不匹配。

## 根因分析

**分类**: PR代码问题
**置信度**: 高 ✓
**具体问题**: 测试断言失败

### 分析推理

检测到代码问题模式: test_assertion。问题出现在 PR #1234 代码中。建议检查 PR 的代码修改和测试用例。

## 证据

### 匹配模式

- **test_assertion**: `AssertionError`
  - `AssertionError`
  - `Expected output shape`

### 链接

- [Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/567890)
- [PR #1234](https://github.com/vllm-project/vllm-ascend/pull/1234)
- [Job: e2e-full](https://github.com/vllm-project/vllm-ascend/actions/runs/567890/job/67890)

### 日志片段

```
FAILED tests/e2e/singlecard/test_inference.py::test_basic_inference
AssertionError: Expected output shape (1, 100) but got (1, 50)
...
```

## 修复建议

**优先建议**: 检查失败的测试用例 (低成本)

### 详细步骤

1. **检查失败的测试用例** (低成本)
   查看测试文件中的断言错误
   - 查看 job 日志中的具体测试失败信息
   - 确认测试是否因 PR 代码修改导致

2. **修复测试或代码** (中等成本)
   根据测试失败原因修改代码或测试用例
   - 如果测试预期行为改变，更新测试
   - 如果代码引入 bug，修复代码逻辑

---
报告生成时间: 2024-01-15T12:00:00
"""

INFRA_REPORT_TEMPLATE = """---
report_id: sample002
pr_number: null
workflow_run_id: 567891
generated_at: 2024-01-15T13:00:00
classification: infrastructure
confidence: high
category_detail: K8s内部服务失败
---

# 构建失败报告: Workflow E2E-Full

## 概要

构建失败由基础设施问题导致: K8s内部服务失败。不是代码问题，建议重试。

## 根因分析

**分类**: 基础设施问题
**置信度**: 高 ✓
**具体问题**: K8s内部服务失败

### 分析推理

检测到基础设施问题: cache_service。问题出现在 job 'e2e-light' 中。Runner: linux-aarch64-a2b3-1。不是PR代码问题，建议检查基础设施状态。

## 证据

### 匹配模式

- **cache_service**: `cache-service.nginx-pypi-cache`
  - `cache-service.nginx-pypi-cache.svc.cluster.local`
  - `connection refused`

### 链接

- [Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/567891)

### 日志片段

```
Could not find a version that satisfies the requirement torch>=2.0
cache-service.nginx-pypi-cache.svc.cluster.local connection refused
...
```

## 修复建议

**优先建议**: 等待服务恢复 (低成本)

### 详细步骤

1. **等待服务恢复** (低成本)
   cache-service.nginx-pypi-cache 通常会自动恢复
   - 等待 10-30 分钟后重新触发构建
   - 如果持续失败，联系基础设施团队

---
报告生成时间: 2024-01-15T13:00:00
"""

INTERFERENCE_REPORT_TEMPLATE = """---
report_id: sample003
pr_number: 1235
workflow_run_id: 567892
generated_at: 2024-01-15T14:00:00
classification: interference
confidence: medium
category_detail: 多PR并发干扰
---

# 构建失败报告: PR #1235

## 概要

构建失败由 3 个并发PR合入干扰导致。建议重试构建或协调合入顺序。

## 根因分析

**分类**: 多PR并发干扰
**置信度**: 中 ~
**具体问题**: 多PR并发干扰

### 分析推理

最近 24 小时内有 3 个PR合并。可能是并发合入导致的干扰。

## 证据

### 匹配模式

- **concurrent_merge**: 短时间内合并 3 个PR

### 链接

- [Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/567892)
- [PR #1235](https://github.com/vllm-project/vllm-ascend/pull/1235)

## 修复建议

**优先建议**: 重新触发构建 (低成本)

### 详细步骤

1. **重新触发构建** (低成本)
   并发合入导致的干扰通常可通过重试解决
   - 等待其他 PR 构建完成
   - 重新触发当前 PR 的 workflow

2. **检查相关 PR** (低成本)
   查看可能干扰的 PR: #1233, #1234
   - 检查相关 PR 的构建状态
   - 确认是否已完成或失败

3. **协调合入顺序** (中等成本)
   如持续失败，可能需要协调多个 PR 的合入时机
   - 联系相关 PR 作者
   - 调整合入顺序或时机

## 相关PR

可能与当前构建冲突的PR:

- PR #1233: Fix memory leak
- PR #1234: Add optimization

---
报告生成时间: 2024-01-15T14:00:00
"""