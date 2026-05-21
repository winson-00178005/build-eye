# GitHub Token 配置指南

Build-Eye 监测系统需要配置以下 GitHub Token 密钥才能正常运行。

## 必需密钥

### GITHUB_TOKEN

**用途**: 访问 vllm-project/vllm-ascend 仓库的公开数据

**权限要求**:
- `actions:read` - 读取 workflow runs 数据
- `contents:read` - 读取仓库内容
- `pull-requests:read` - 读取 PR 信息

**配置方式**:
1. GitHub Actions 自动提供 `secrets.GITHUB_TOKEN`，无需手动配置
2. 该 token 仅对本仓库有效，但可以访问公开仓库的数据

**注意事项**:
- 默认 token 权限可能受限，需要在 workflow 中声明 `permissions`
- 参见 `.github/workflows/monitor.yml` 中的 permissions 配置

### ARCHIVE_REPO_TOKEN

**用途**: 向 winson-00178005/build-eye 仓库提交报告文件

**权限要求**:
- `contents:write` - 写入报告文件
- `pull-requests:write` - 创建 PR（可选，用于批量归档）

**配置步骤**:

1. **创建 Personal Access Token**
   - 访问 GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
   - 创建新 token，选择:
     - Repository: `winson-00178005/build-eye` (仅此仓库)
     - Permissions: Contents (Read and write)

2. **添加到仓库密钥**
   - 访问本仓库 Settings → Secrets and variables → Actions
   - 点击 "New repository secret"
   - Name: `ARCHIVE_REPO_TOKEN`
   - Value: 粘贴刚才创建的 token

3. **验证配置**
   ```bash
   # 在本地测试
   export ARCHIVE_REPO_TOKEN="your_token_here"
   python scripts/archive/archiver.py --input reports/ --repo https://github.com/winson-00178005/build-eye.git
   ```

## 可选密钥

### GITHUB_API_TOKEN

**用途**: 提高 GitHub API 调用限额（从 60/小时 提升到 5000/小时）

**配置方式**:
- 如果 `GITHUB_TOKEN` 额度不足，可创建单独的 fine-grained token
- 仅需 `public_repo` 权限即可访问公开仓库

## 安全最佳实践

1. **使用 Fine-grained tokens**: 限制 token 权限范围到特定仓库
2. **定期轮换**: 建议每 90 天更新一次 token
3. **不要硬编码**: 所有 token 必须通过 `secrets` 注入
4. **日志脱敏**: 确保日志中不会打印 token 值
5. **权限最小化**: 只授予必需的最小权限

## Troubleshooting

### Token 权限不足
```
错误: HTTP 403 - Resource not accessible by integration
解决: 检查 workflow 中的 permissions 配置，确保声明了所需权限
```

### API 额度耗尽
```
错误: HTTP 403 - API rate limit exceeded
解决: 
1. 检查 polling 频率是否过高
2. 配置 GITHUB_API_TOKEN 提高额度
3. 确认缓存策略生效
```

### 归档失败
```
错误: Git push failed - Authentication required
解决: 
1. 确认 ARCHIVE_REPO_TOKEN 已正确配置
2. 检查 token 是否有 contents:write 权限
3. 验证归档仓库 URL 是否正确
```