# 运维手册 - Build-Eye CI 监测系统部署指南

## 一、环境准备

### 1.1 仓库配置

本系统已配置好以下仓库：
- **监测目标**: https://github.com/vllm-project/vllm-ascend
- **归档仓库**: https://github.com/winson-00178005/build-eye.git

### 1.2 GitHub Token 配置

需要在 GitHub 上配置 **三个 Token**：

#### GITHUB_TOKEN（自动提供）

1. **获取位置**: GitHub Actions 自动提供
2. **权限要求**:
   - `actions:read` - 读取 workflow runs
   - `contents:read` - 读取仓库内容
   - `pull-requests:read` - 读取 PR 信息
3. **作用域**: 仅对 build-eye 仓库有效

**⚠️ 重要**: GITHUB_TOKEN 无法访问其他仓库！

#### VLLM_ASCEND_TOKEN（必需 - 用于访问目标仓库）

**用途**: 访问 vllm-project/vllm-ascend 仓库的 workflow runs 数据

**权限要求**:
- `public_repo` - 读取公开仓库数据
- 或 Fine-grained token: `contents:read`, `actions:read`

**配置步骤**:

1. **创建 Token**:
   ```
   GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
   ```
   
2. **Token 配置**:
   - Repository: `All public repositories` 或仅 `vllm-project/vllm-ascend`
   - Permissions: Contents (Read), Actions (Read)

3. **添加到仓库密钥**:
   ```
   build-eye 仓库 → Settings → Secrets and variables → Actions → New repository secret
   
   Name: VLLM_ASCEND_TOKEN
   Value: <粘贴你的 Token>
   ```

4. **验证配置**:
   ```bash
   curl -H "Authorization: token YOUR_TOKEN" \
     "https://api.github.com/repos/vllm-project/vllm-ascend/actions/runs?per_page=1"
   ```

#### ARCHIVE_REPO_TOKEN（必需 - 用于归档报告）

**用途**: 向 winson-00178005/build-eye 仓库提交报告文件

**权限要求**:
- `contents:write` - 写入报告文件

**配置步骤**:

1. **创建 Token**:
   ```
   GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
   ```
   
2. **Token 配置**:
   - Repository: 仅选择 `winson-00178005/build-eye`
   - Permissions: Contents (Read and write)

3. **添加到仓库密钥**:
   ```
   build-eye 仓库 → Settings → Secrets and variables → Actions → New repository secret
   
   Name: ARCHIVE_REPO_TOKEN
   Value: <粘贴你的 Token>
   ```

---

## 二、GitHub Actions Workflow 配置

### 2.1 Workflow 文件位置

文件已创建: `.github/workflows/monitor.yml`

### 2.2 Workflow 功能

- **定时轮询**: 每 6 小时自动检查（cron: `0 */6 * * *`)
- **手动触发**: 通过 GitHub Actions 页面手动运行
- **试运行模式**: 支持不归档的测试运行

### 2.3 配置 Workflow Secrets

进入 build-eye 仓库配置页面：

```
https://github.com/winson-00178005/build-eye/settings/secrets/actions
```

添加以下 Secrets：

| Secret 名称 | 说明 | 是否必需 |
|------------|------|---------|
| `VLLM_ASCEND_TOKEN` | 访问 vllm-ascend 仓库的 Token | **必需** |
| `ARCHIVE_REPO_TOKEN` | 归档仓库写入 Token | **必需** |
| `GITHUB_TOKEN` | GitHub Actions 自动提供 | 自动（作用域受限）|

---

## 三、首次运行配置

### 3.1 推送代码到仓库

```bash
# 已完成 - 代码已推送
git push origin main
```

### 3.2 验证 Workflow 文件

确认 `.github/workflows/monitor.yml` 存在于仓库中：
```
https://github.com/winson-00178005/build-eye/tree/main/.github/workflows
```

### 3.3 手动触发首次测试

1. 打开 GitHub Actions 页面：
   ```
   https://github.com/winson-00178005/build-eye/actions
   ```

2. 选择 `Build-Eye Scheduled Monitoring` workflow

3. 点击 `Run workflow` 按钮

4. 配置参数：
   | 参数 | 值 |
   |-----|---|
   | `lookback_hours` | 24 |
   | `dry_run` | true（首次测试建议开启） |
   | `target_repo` | vllm-project/vllm-ascend |

5. 点击绿色 `Run workflow` 按钮

---

## 四、今晚采集报告

### 4.1 配置完成检查

确认以下配置已完成：

- [ ] 代码已推送到 `winson-00178005/build-eye` 仓库
- [ ] `ARCHIVE_REPO_TOKEN` Secret 已配置
- [ ] Workflow 文件存在于 `.github/workflows/monitor.yml`

### 4.2 触发今晚采集

**方式一: 手动触发**

```
1. 访问: https://github.com/winson-00178005/build-eye/actions
2. 选择: Build-Eye Scheduled Monitoring
3. 点击: Run workflow
4. 参数:
   - lookback_hours: 24
   - dry_run: false（关闭试运行，正式归档）
   - target_repo: vllm-project/vllm-ascend
5. 执行
```

**方式二: 等待定时触发**

系统将在以下时间自动运行：
- 00:00 UTC（北京时间 08:00）
- 06:00 UTC（北京时间 14:00）
- 12:00 UTC（北京时间 20:00）
- 18:00 UTC（北京时间 02:00）

### 4.3 查看采集结果

**查看 Workflow 运行状态**:
```
https://github.com/winson-00178005/build-eye/actions
```

**查看归档报告**:
```
https://github.com/winson-00178005/build-eye/tree/main/reports
```

报告目录结构：
```
reports/
└── 2026/
    └── 05/
        └── 21/
            ├── code-pr-xxxx.md      # 代码问题报告
            └── infrastructure-pr-xxxx.md  # 基础设施报告
```

---

## 五、常见问题处理

### 5.1 Workflow 运行失败

**问题**: Workflow 显示红色失败状态

**排查步骤**:
1. 点击失败的 workflow run 查看日志
2. 检查 Secrets 是否正确配置
3. 检查 Token 权限是否足够

**常见错误**:

| 错误信息 | 原因 | 解决方案 |
|---------|------|---------|
| `ARCHIVE_REPO_TOKEN not found` | Secret 未配置 | 配置 ARCHIVE_REPO_TOKEN |
| `Permission denied` | Token 权限不足 | 添加 contents:write 权限 |
| `API rate limit exceeded` | GitHub API 限额耗尽 | 降低 polling 频率或等待重置 |

### 5.2 无报告生成

**可能原因**:
- vLLM-Ascend 最近 24 小时无失败构建
- Workflow runs 数据获取失败

**验证方式**:
```bash
# 手动检查 vLLM-Ascend 失败构建
curl -H "Authorization: token YOUR_TOKEN" \
  "https://api.github.com/repos/vllm-project/vllm-ascend/actions/runs?status=completed&conclusion=failure"
```

### 5.3 报告未归档

**原因**: `dry_run` 参数设置为 `true`

**解决**: 手动触发时将 `dry_run` 设置为 `false`

---

## 六、监控和维护

### 6.1 Workflow 健康监控

建议定期检查：
- Workflow 是否按时触发
- 报告是否正常归档
- Token 是否过期（Fine-grained tokens 有有效期）

### 6.2 Token 更新

Fine-grained tokens 通常有 90 天有效期：

1. 提前更新 Token
2. 更新 GitHub Secret
3. 验证新 Token 有效

### 6.3 日志查看

Workflow 运行日志包含：
- 检查了多少 workflow runs
- 发现多少失败构建
- 分类统计（代码/基础设施/干扰）
- 归档状态

---

## 七、高级配置

### 7.1 自定义监测时间范围

修改 `lookback_hours` 参数：
- 默认: 24 小时
- 可选: 12、48、72 等

### 7.2 监测特定 Workflow

修改 `config/config.yaml`:
```yaml
target_repository:
  monitored_workflows:
    - pr_test_full.yaml
    - pr_test_light.yaml
    - schedule_nightly_test_a3.yaml  # 添加 nightly 监测
```

### 7.3 调整轮询频率

修改 `.github/workflows/monitor.yml`:
```yaml
on:
  schedule:
    - cron: '0 */4 * * *'  # 每 4 小时
```

---

## 八、快速命令参考

### 本地测试（无需 Token）

```bash
cd /d/build-eye
python tests/mock_test.py
```

### 手动触发 Workflow

```
GitHub Actions → Build-Eye Scheduled Monitoring → Run workflow
```

### 查看报告

```
https://github.com/winson-00178005/build-eye/tree/main/reports
```

### 查看 Workflow 日志

```
https://github.com/winson-00178005/build-eye/actions
```

---

## 附录: Token 创建详细步骤

### 步骤1: 访问 Token 创建页面

```
https://github.com/settings/personal-access-tokens/new
```

### 步骤2: 配置 Token

- **Token name**: `build-eye-archive-token`
- **Expiration**: 90 days（建议）
- **Repository access**: Only select repositories → `winson-00178005/build-eye`
- **Permissions**:
  - Contents: Read and write

### 步骤3: 生成并保存 Token

点击 `Generate token`，立即复制 Token（只显示一次）

### 步骤4: 添加到仓库 Secret

```
https://github.com/winson-00178005/build-eye/settings/secrets/actions

New repository secret:
  Name: ARCHIVE_REPO_TOKEN
  Value: <粘贴 Token>
```

---

**运维手册版本**: v1.0  
**更新日期**: 2026-05-21