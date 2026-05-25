# 📊 vllm-project/vllm-ascend 构建分析报告（校对版）

**原始报告生成时间**: 2026-05-25 08:15:29  
**校对时间**: 2026-05-25  
**校对依据**: GitHub Actions API 实际数据 + build-eye workflow 分析  
**时间范围**: 2026-05-17 ~ 2026-05-24

---

## ⚠️ 原报告准确性校对结果

### 严重错误（7 处）

| # | 错误描述 | 原报告数据 | 实际数据（校对后） | 影响 |
|---|---------|-----------|------------------|------|
| E1 | **总构建数严重偏低** | 2400 | ~8912（API total_count） | 概览统计不具代表性 |
| E2 | **PR 流水线 0 失败是错误的** | 344 total, 344 success, 0 failure | ~694 total, ~380 success, ~70 failure | PR 成功率约 76.8%（非 100%） |
| E3 | **Nightly 成功数为 0 是错误的** | 632 total, 0 success, 8 failure | ~251 total, 4 success, ~12 failure | Nightly 有成功构建 |
| E4 | **Nightly 失败数不完整** | 8 | 12（跨全部 API 页面） | 缺少 4 个失败记录 |
| E5 | **Weekly 总数和失败数错误** | 8 total, 0 success, 8 failure | 2 total, 0 success, 2 failure | 数量夸大 4 倍 |
| E6 | **失败详情 Workflow 名称全部为 N/A** | 所有条目显示 "N/A" | 实际有 Nightly-A2、Nightly-A3 等名称 | 数据提取/渲染 Bug |
| E7 | **模板变量未渲染** | `{stats['pr']['total']}` | 应为具体数值 | Python 模板渲染遗漏 |

### 数据质量问题（3 处）

| # | 问题描述 | 说明 |
|---|---------|------|
| Q1 | **失败详情重复且截断** | Nightly 8 条失败全是同一时间同一消息，实际有 12 个不同时间不同 commit 的失败 |
| Q2 | **分类引擎 96.8% 未知率** | 248 失败中 240 归为"未知"，分类器对 vllm-ascend 数据适配不足 |
| Q3 | **成功/失败/其他状态未区分** | 大量 skipped/cancelled/in_progress 构建被归入总数但无明确标注 |

---

## 一、概览（校对后）

```
┌──────────────────────────────────────────────────────────────────┐
│                   构建统计概览（校对后）                            │
├──────────────────────────────────────────────────────────────────┤
│  API 可访问总数: ~1000   总记录数: 8912                           │
│                                                                  │
│  已完成构建分布:                                                  │
│    success:  420  (42.0%)  ✅                                    │
│    skipped:  425  (42.5%)  ⏭️                                    │
│    failure:   98  (9.8%)   ❌                                    │
│    cancelled: 50  (5.0%)   🚫                                    │
│    in-progress: 2  (0.2%)  ⏳                                    │
│                                                                  │
│  注: API 最多返回 1000 条记录，8912 为 reported total_count       │
└──────────────────────────────────────────────────────────────────┘
```

> **说明**: GitHub Actions API 对单次查询最多返回约 1000 条记录。`total_count=8912` 是 API 报告的总量，但实际只能获取前 1000 条。统计数据基于 API 可获取的 1000 条样本。

---

## 二、各流水线统计（校对后）

### PR 流水线

| 指标 | 原报告 | 校对后 | 差异 |
|------|--------|--------|------|
| 总构建数 | 344 | ~694 | +350 |
| 成功 | 344 | ~380 | +36 |
| 失败 | 0 | ~70 | 严重错误 |
| 取消 | — | ~42 | 原报告未记录 |
| 跳过 | — | ~199 | 原报告未记录 |
| 成功率 | 100.0% | 76.8%（排除 skipped） | 严重错误 |

> **校对说明**: 原报告声称 PR 流水线"0 失败"是不准确的。实际 E2E-Light 和 E2E-Full 等 PR workflow 有约 70 个失败构建。344 total 也远低于实际约 694 个。

### NIGHTLY 流水线

| 指标 | 原报告 | 校对后 | 差异 |
|------|--------|--------|------|
| 总构建数 | 632 | ~251 | -381 |
| 成功 | 0 | 4 | 严重错误 |
| 失败 | 8 | ~12 | +4 |
| 取消 | — | ~8 | 原报告未记录 |
| 跳过 | — | ~224 | 原报告未记录 |
| 成功率 | 0.0% | ~1.6%（4/251） | 严重错误 |

#### 失败详情（校对后 12 个）

| 时间 | Workflow | Commit 摘要 |
|------|----------|-------------|
| 2026-05-24 16:42 | **Nightly-A2** | [Doc][Misc] Keep VLLM_USE_MODELSCOPE... |
| 2026-05-23 16:40 | **Nightly-A3** | [Doc] Remove modelscope installation... |
| 2026-05-23 16:40 | **Nightly-A2** | [Doc] Remove modelscope installation... |
| 2026-05-23 15:27 | **Nightly-A2** | [CI] Modify nightly test case config... |
| 2026-05-23 15:27 | **Nightly-A3** | [CI] Modify nightly test case config... |
| 2026-05-23 13:08 | **Nightly-A3** | [CI] Modify nightly test case config... |
| 2026-05-23 10:26 | **Nightly-A3** | [CI] Modify nightly test case config... |
| 2026-05-23 09:08 | **Nightly-A3** | [CI] Modify nightly test case config... |
| 2026-05-23 02:56 | **Nightly-A3** | add deepseekv4 e2e |
| 2026-05-22 17:27 | **Nightly-A3** | [BugFix]Fix Deepseek-V4 async scheduling... |
| 2026-05-22 17:27 | **Nightly-A2** | [BugFix]Fix Deepseek-V4 async scheduling... |
| 2026-05-22 10:16 | **Nightly-A3** | [CI] Modify nightly test case config... |

> **校对说明**: 原报告所有 8 条失败都显示 Workflow=N/A、时间相同、消息相同。这是数据提取 Bug——实际有 12 个失败，分布在 Nightly-A2 和 Nightly-A3 两个 workflow，时间从 05-22 到 05-24 不等。

### WEEKLY 流水线

| 指标 | 原报告 | 校对后 | 差异 |
|------|--------|--------|------|
| 总构建数 | 8 | 2-3 | 严重夸大 |
| 成功 | 0 | 0 | 一致 |
| 失败 | 8 | 2 | 严重夸大 |
| 成功率 | 0.0% | 0.0% | 一致 |

#### 失败详情（校对后 2 个）

| 时间 | Workflow | Commit 摘要 |
|------|----------|-------------|
| 2026-05-24 05:04 | **Weekly-A3** | [Doc][Misc] Keep VLLM_USE_MODELSCOPE... |
| 2026-05-23 03:26 | **Weekly-A3** | — |

> **校对说明**: 原报告称 Weekly 有 8 个失败，全部为同一时间同一消息。实际仅有 2 个 Weekly-A3 失败构建，且时间不同。原报告可能误将 skipped 的 Nightly 构建计入 Weekly。

---

## 三、失败原因分类（校对后）

基于 build-eye 分类引擎和人工复核的综合分析：

| 分类 | 原报告数量 | 校对后数量 | 说明 |
|------|-----------|-----------|------|
| 🧪 代码问题 | 0 | ~35 | E2E-Light/E2E-Full 的 PR 失败多为代码问题 |
| 📦 基础设施 | 8 | ~12 | Nightly-A2/A3 失败包含基础设施和配置问题 |
| 🔄 干扰因素 | 0 | ~5 | 部分 PR 失败为并发合入干扰 |
| 📄 文档相关 | — | 3 | Docs link check 和 VLLM_USE_MODELSCOPE 文档问题 |
| ❓ 未知 | 240 | ~43 | 分类器对非标准 workflow 名称适配不足 |

```
失败原因分布（校对后，基于 API 可获取数据）:
  代码问题    35 (35%)
  基础设施    12 (12%)
  干扰因素     5 (5%)
  文档相关     3 (3%)
  未知        43 (44%)
```

> **校对说明**: 原报告 96.8% 未知率是因为分类引擎只处理了少数 workflow 的数据，大量 skipped/cancelled 状态被误计入总数。排除这些后，实际失败约 98 个，分类覆盖率显著提升。

---

## 四、结论（校对后）

### ✅ 优点

- **PR 核心流水线 E2E-Light/E2E-Full 有较高成功率**: 排除 skipped/cancelled 后约 76.8%
- **Nightly 流水线存在少量成功构建**: 4/251 约 1.6%（原报告误报为 0）

### ⚠️ 问题

- **Nightly 流水线失败率高**: 12 个失败构建需根因分析，集中在 05-22~05-24
- **Weekly-A3 流水线全部失败**: 仅 2-3 次运行，均失败
- **E2E-Light 是最大失败来源**: 约 43 个失败，是所有 workflow 中失败数最多的

### 📝 建议

1. **优先修复 E2E-Light**: 作为 PR 的主要验证 workflow，43 个失败影响代码质量控制
2. **调查 Nightly-A2/A3 连续失败**: 05-22~05-24 期间有密集失败，需分析是否为基础设施退化
3. **修复 Weekly-A3**: 仅 2 次运行均失败，需要人工复核日志
4. **改进 build-eye 数据采集**: 修复 Workflow 名称提取 Bug（全部显示 N/A）和重复/截断问题
5. **优化分类引擎**: 降低"未知"分类比例，增加对 vllm-ascend 特有 workflow 的适配

---

## 五、原报告错误根因分析

| 错误 | 根因 | 修复建议 |
|------|------|---------|
| E1: 总数偏低 2400 vs 8912 | 数据采集未完整分页获取 | 增加 API 分页循环直到获取全部数据 |
| E2: PR 0 失败 | 可能只统计了 merge-success 的 PR | 区分 conclusion=success/failure/cancelled |
| E3: Nightly 0 成功 | 可能将 skipped 误归为非成功 | 正确区分 success/skipped/cancelled |
| E6: Workflow=N/A | workflow name 字段提取路径错误 | 检查 JSON 解析路径，使用 .name 或 .path |
| E7: 模板未渲染 | Python f-string/template 渲染遗漏 | 使用 Jinja2 或 f-string 正确渲染 |
| Q1: 重复截断 | 数据去重和截断逻辑错误 | 对相同 workflow_run_id 去重 |
| Q2: 96.8% 未知 | 分类器对 skipped/cancelled 也尝试分类 | 先过滤出 conclusion=failure 再分类 |