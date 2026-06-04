# Build-Eye Dashboard 重设计方案

## 版本信息

| 项目 | 内容 |
|------|------|
| **文档版本** | v1.0 |
| **创建日期** | 2026-06-04 |
| **适用项目** | Build-Eye CI 监测系统 |
| **作者** | 架构师 |
| **变更说明** | Dashboard 重设计：下沉到 Job 级别、取消白名单限制、优化数据采集 |

---

## 一、设计背景

### 1.1 问题分析

Build-Eye 与外部 vLLM Ascend Dashboard (http://123.57.0.174/) 统计数据存在系统性差异，根本原因如下：

| 差异原因 | Build-Eye 当前行为 | 外部网站行为 | 影响 |
|----------|-------------------|-------------|------|
| **统计粒度** | Workflow 级别计数 | Job 级别计数 | 总数和成功率完全不可比 |
| **cancelled/skipped 处理** | 计入"失败" | 独立分类展示 | 成功率偏低 |
| **白名单过滤** | 只监控 11 个 workflow | 监控所有 workflow | 总运行数偏少 |
| **event=schedule 过滤** | nightly/weekly 只取 schedule 事件 | 包含所有触发类型 | 遗漏手动重触发 |
| **分页限制** | max_pages=5 (最多500条) | 全量采集 | 遗漏超出500条的数据 |
| **lookback 窗口** | PR 24h / Nightly 168h | 全历史+近7天 | 数据时效不一致 |
| **completed_at 兜底** | 用 updated_at 代替 | 使用真实 completed_at | 时长计算偏差 |
| **跨类型去重** | 无去重 | 每条数据唯一 | dashboard 可能重复计数 |

### 1.2 设计目标

1. **数据可比**：与外部网站统计粒度一致，下沉到 Job 级别
2. **数据完整**：全历史存储、全量采集、无白名单/事件/分页限制
3. **分类清晰**：cancelled/skipped/timed_out 独立统计，不计入成功率
4. **多维时间**：支持全历史、近7天、近30天、自定义时间范围
5. **独立页面**：Workflow 看板、Job 看板、分类统计、健康评分四个独立页面

---

## 二、数据模型设计

### 2.1 SQLite 新增表

#### workflow_runs 表

```sql
CREATE TABLE IF NOT EXISTS workflow_runs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    workflow_id INTEGER,
    conclusion TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'completed',
    event TEXT,
    head_branch TEXT,
    head_sha TEXT,
    triggering_actor TEXT DEFAULT 'unknown',
    html_url TEXT,
    started_at TEXT,
    completed_at TEXT,
    duration_seconds REAL,
    pipeline_type TEXT,
    hardware_label TEXT,
    created_at TEXT,
    updated_at TEXT
);
```

**conclusion 字段规范**：success / failure / cancelled / skipped / timed_out / action_required / null

**pipeline_type 识别规则**（保持现有 PipelineDetector 逻辑）：
- Nightly-* / *_nightly_* → nightly
- Weekly-* / *_weekly_* → weekly
- pull_request / pull_request_target 事件 → pr
- 其余 → 根据分支和 PR 关联判断

**hardware_label 提取规则**：从 workflow name 或 job runner 名称中提取 A2/A3 标识。

#### job_records 表

```sql
CREATE TABLE IF NOT EXISTS job_records (
    id INTEGER PRIMARY KEY,
    workflow_run_id INTEGER NOT NULL,
    workflow_name TEXT NOT NULL,
    job_name TEXT NOT NULL,
    conclusion TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'completed',
    started_at TEXT,
    completed_at TEXT,
    duration_seconds REAL,
    runner_name TEXT,
    runner_group_name TEXT,
    steps_count INTEGER DEFAULT 0,
    failed_step_name TEXT,
    hardware_label TEXT,
    FOREIGN KEY (workflow_run_id) REFERENCES workflow_runs(id)
);
CREATE INDEX IF NOT EXISTS idx_job_workflow_run ON job_records(workflow_run_id);
CREATE INDEX IF NOT EXISTS idx_job_workflow_name ON job_records(workflow_name);
CREATE INDEX IF NOT EXISTS idx_job_conclusion ON job_records(conclusion);
CREATE INDEX IF NOT EXISTS idx_workflow_conclusion ON workflow_runs(conclusion);
CREATE INDEX IF NOT EXISTS idx_workflow_pipeline ON workflow_runs(pipeline_type);
CREATE INDEX IF NOT EXISTS idx_workflow_created ON workflow_runs(created_at);
CREATE INDEX IF NOT EXISTS idx_workflow_name ON workflow_runs(name);
```

### 2.2 成功率定义

**Workflow 成功率** = `conclusion=success 的数量 / (conclusion=success + conclusion=failure 的数量)`

**Job 成功率** = `conclusion=success 的数量 / (conclusion=success + conclusion=failure 的数量)`

**排除项**（独立统计，不参与成功率计算）：
- cancelled — 人工取消或新提交覆盖
- skipped — 条件不满足被跳过
- timed_out — 超时
- action_required — 需人工审批

在 overview 和统计中，这些状态作为独立字段展示：
```json
{
  "total_runs": 175,
  "success_runs": 1,
  "failure_runs": 140,
  "cancelled_runs": 20,
  "skipped_runs": 10,
  "timed_out_runs": 4,
  "success_rate": 0.7
}
```

---

## 三、数据采集流程优化

### 3.1 采集策略变更

| 变更项 | 原策略 | 新策略 |
|--------|--------|--------|
| monitored_workflows | 11 个白名单 | **所有 workflow**（移除白名单过滤） |
| event 过滤 | nightly/weekly 只取 schedule | **所有触发事件** |
| 分页限制 | max_pages=5 (最多500) | **全量分页采集**（无上限） |
| lookback 窗口 | PR 24h / Nightly 168h | **增量同步**（按 updated_at） |
| completed_at | updated_at 兜底 | **仅用真实 completed_at** |
| 跨类型去重 | 无去重 | **按 workflow_run_id 唯一** |

### 3.2 增量同步流程

1. 查询 SQLite 中 `MAX(updated_at)` 作为 last_sync_time
2. 调用 GitHub API：`GET /repos/{owner}/{repo}/actions/runs?status=completed&per_page=100`，全量分页
3. 对每个 run，调用 `GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs` 获取 job 列表
4. 写入 workflow_runs 和 job_records 表（INSERT OR REPLACE）

**首次全量采集**：不设时间窗口，从 GitHub API 分页拉取所有历史 completed runs。

### 3.3 定时调度

保持现有 4 次/天的 deploy-dashboard 工作流，但改为增量同步：
- 步骤 1：运行 `sync_data.py`（增量采集，写入 SQLite）
- 步骤 2：运行 `export_dashboard.py`（从 SQLite 导出 JSON 文件）

---

## 四、预导出 JSON 设计

### 4.1 导出文件

deploy 时从 SQLite 导出以下 JSON 文件到 `dashboard/` 目录：

| 文件 | 时间范围 | 内容 |
|------|----------|------|
| `dashboard_all.json` | 全历史 | workflow_overview + job_overview + workflow_runs + job_stats + categories + health_scores + trends |
| `dashboard_7d.json` | 近 7 天 | 同上结构，数据限定近7天 |
| `dashboard_30d.json` | 近 30 天 | 同上结构，数据限定近30天 |
| `dashboard_custom.json` | 自定义时间范围 | 通过 `--start-date` 和 `--end-date` 参数按需生成 |

### 4.2 JSON 结构

每个 JSON 文件包含以下顶层字段：

```json
{
  "meta": {
    "time_range": "all|7d|30d|custom",
    "start_date": "2026-01-01",
    "end_date": "2026-06-04",
    "generated_at": "2026-06-04T12:00:00Z",
    "total_workflows": 175,
    "total_jobs": 1100
  },
  "workflow_overview": {
    "total_runs": 175,
    "success_runs": 1,
    "failure_runs": 140,
    "cancelled_runs": 20,
    "skipped_runs": 10,
    "timed_out_runs": 4,
    "success_rate": 0.7,
    "avg_duration_minutes": 524,
    "pipelines": {
      "nightly": { ... },
      "weekly": { ... },
      "pr": { ... }
    }
  },
  "job_overview": {
    "total_jobs": 1100,
    "success_jobs": 500,
    "failure_jobs": 400,
    "cancelled_jobs": 100,
    "skipped_jobs": 50,
    "timed_out_jobs": 50,
    "job_success_rate": 55.6,
    "avg_job_duration_minutes": 45
  },
  "workflow_runs": [
    {
      "id": 26841726588,
      "name": "Nightly-A3",
      "conclusion": "cancelled",
      "started_at": "2026-06-03T03:03:24Z",
      "completed_at": "2026-06-03T09:19:24Z",
      "duration_minutes": 376,
      "pipeline_type": "nightly",
      "hardware_label": "A3",
      "html_url": "...",
      "job_count": 15,
      "job_success_count": 8,
      "job_failure_count": 2,
      "job_cancelled_count": 5
    }
  ],
  "job_stats": [
    {
      "workflow_name": "Nightly-A2",
      "job_name": "Build nightly-a2 image (main) / Build nightly-a2 image",
      "total_runs": 6,
      "success_runs": 6,
      "failure_runs": 0,
      "cancelled_runs": 0,
      "success_rate": 100.0,
      "avg_duration_minutes": 16.5,
      "min_duration_minutes": 9.7,
      "max_duration_minutes": 45.9,
      "last_run_at": "2026-06-03T03:03:19Z",
      "last_conclusion": "success"
    }
  ],
  "categories": {
    "distribution": { "code": 30, "infrastructure": 15, "interference": 5 }
  },
  "health_scores": {
    "scores": [
      { "pipeline_type": "nightly", "score": 25, "rating": "danger" }
    ]
  },
  "trends": {
    "workflow_success_rate_trend": [0.7, 0.0, 0.5],
    "job_success_rate_trend": [55.6, 30.0, 40.0],
    "failure_count_trend": [140, 15, 50],
    "dates": ["2026-05-27", "2026-06-03", "2026-06-04"]
  },
  "notification_settings": { ... }
}
```

### 4.3 自定义时间导出

通过命令行参数支持任意时间范围：

```bash
python scripts/report/export_dashboard.py \
  --db data/build_metrics.db \
  --output dashboard/dashboard_custom.json \
  --start-date 2026-05-01 \
  --end-date 2026-05-15
```

GitHub Actions workflow_dispatch 中增加输入参数：

```yaml
on:
  workflow_dispatch:
    inputs:
      start_date:
        description: '开始日期 (YYYY-MM-DD)'
        required: false
      end_date:
        description: '结束日期 (YYYY-MM-DD)'
        required: false
```

前端增加"自定义时间"下拉选项，选中后通过 URL 参数 `?range=custom&start=2026-05-01&end=2026-05-15` 加载对应的 JSON（若存在则直接加载，否则提示需要先生成）。

---

## 五、前端页面设计

### 5.1 页面结构

左侧固定导航菜单，4 个独立页面：

```
┌──────────────────────────────────────────────────────────┐
│  vLLM-Ascend Build-Eye                                    │
├──────┬───────────────────────────────────────────────────┤
│      │                                                    │
│ 📊   │  [当前页面内容]                                    │
│ Work │                                                    │
│ flow │                                                    │
│      │                                                    │
│ 🔧   │                                                    │
│ Job  │                                                    │
│      │                                                    │
│ 📉   │                                                    │
│ 分类 │                                                    │
│      │                                                    │
│ 💯   │                                                    │
│ 健康 │                                                    │
│      │                                                    │
│ ⚙️   │                                                    │
│ 设置 │                                                    │
│      │                                                    │
└──────┴───────────────────────────────────────────────────┘
```

### 5.2 Workflow 看板页面

**顶部统计卡片**（3 个维度切换：全历史/7天/30天/自定义）：
- 总运行次数 + 各结论分布（success/failure/cancelled/skipped/timed_out）
- 成功率（仅 success/(success+failure)）
- 平均时长

**流水线分组统计**：
- Nightly / Weekly / PR 三个分组的成功率、运行数、平均时长

**Workflow 运行列表**（可筛选表格）：
- 列：开始时间 | Workflow名称 | 硬件 | 状态 | 结果 | 时长 | Job统计
- 筛选器：Workflow名称下拉、结论下拉、硬件下拉
- 每行可展开查看其下的 Job 列表

### 5.3 Job 看板页面

**顶部统计卡片**（同上时间维度切换）：
- 总 Job 数 + 各结论分布
- Job 成功率
- 平均 Job 时长

**Job 统计表格**（按 Job 名称聚合）：
- 列：Workflow | Job名称 | 总运行 | 成功/失败 | 成功率 | 平均时长 | 最小/最大时长 | 最近运行 | 最近状态
- 筛选器：Workflow下拉、Job名称搜索、状态下拉、时间维度切换

### 5.4 分类统计页面

- 失败原因分布图（code/infrastructure/interference）
- 各分类占比饼图
- 趋势折线图

### 5.5 健康评分页面

- 各流水线类型健康度（保持现有评分算法）
- 健康度趋势图
- 建议列表

### 5.6 设置页面

仅保留邮件通知设置（飞书/钉钉已删除）。

---

## 六、数据采集脚本设计

### 6.1 新增脚本

| 脚本 | 功能 |
|------|------|
| `scripts/monitor/sync_data.py` | 增量/全量同步 workflow runs + jobs 到 SQLite |
| `scripts/report/export_dashboard.py` | 从 SQLite 导出多维度 JSON 文件 |

### 6.2 sync_data.py 流程

```
1. 连接 SQLite (data/build_metrics.db)
2. 查询 last_sync_time = MAX(updated_at) FROM workflow_runs
3. 如果 last_sync_time 为空 → 全量采集模式
4. 调用 GitHub API 获取 workflow runs (全量分页, status=completed)
5. 对每个 run 调用 GitHub API 获取 jobs
6. INSERT OR REPLACE 到 workflow_runs 表
7. INSERT OR REPLACE 到 job_records 表
8. 计算并填充 duration_seconds, pipeline_type, hardware_label
9. 更新 last_sync_time
```

### 6.3 export_dashboard.py 流程

```
1. 连接 SQLite
2. 根据参数确定时间范围 (all/7d/30d/custom)
3. 查询 workflow_runs → 计算 overview
4. 查询 job_records → 计算 job_stats (按 workflow_name + job_name 聚合)
5. 查询分类数据 → categories
6. 查询健康评分 → health_scores
7. 查询趋势数据 → trends
8. 组装 JSON 并写入文件
```

---

## 七、GitHub Actions 工作流变更

### 7.1 deploy-dashboard.yml

```yaml
steps:
  - name: Sync data to SQLite
    run: python scripts/monitor/sync_data.py --db data/build_metrics.db

  - name: Export dashboard JSON files
    run: |
      python scripts/report/export_dashboard.py --db data/build_metrics.db --range all --output dashboard/dashboard_all.json
      python scripts/report/export_dashboard.py --db data/build_metrics.db --range 7d --output dashboard/dashboard_7d.json
      python scripts/report/export_dashboard.py --db data/build_metrics.db --range 30d --output dashboard/dashboard_30d.json

  - name: Export custom range (if requested)
    if: ${{ github.event.inputs.start_date }}
    run: |
      python scripts/report/export_dashboard.py --db data/build_metrics.db --range custom --start-date ${{ github.event.inputs.start_date }} --end-date ${{ github.event.inputs.end_date }} --output dashboard/dashboard_custom.json

  - name: Deploy to GitHub Pages
    ...
```

### 7.2 移除的文件/逻辑

- 移除 `scripts/report/dashboard_data_generator.py` 中直接从环境变量/元数据文件构建数据的逻辑，改为从 SQLite 读取
- 移除 fetch_runs.py 中的 `monitored_workflows` 白名单过滤
- 移除 nightly/weekly 采集中的 `--event schedule` 和 `--branch main` 过滤
- 移除 `max_pages=5` 限制

---

## 八、实施优先级

| 阶段 | 内容 | 优先级 |
|------|------|--------|
| Phase 1 | SQLite 新增表 + sync_data.py + 全量数据采集 | P0 |
| Phase 2 | export_dashboard.py + 多维 JSON 导出 | P0 |
| Phase 3 | 前端 Workflow 看板 + Job 看板页面 | P0 |
| Phase 4 | 前端分类统计 + 健康评分页面 | P1 |
| Phase 5 | GitHub Actions 工作流改造 + 自定义时间导出 | P1 |