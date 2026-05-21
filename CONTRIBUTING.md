# 贡献者指南

感谢您对 Build-Eye CI 监测系统的关注！我们欢迎任何形式的贡献。

## 目录

- [如何贡献](#如何贡献)
- [开发环境搭建](#开发环境搭建)
- [代码贡献流程](#代码贡献流程)
- [代码规范](#代码规范)
- [提交规范](#提交规范)
- [测试要求](#测试要求)
- [文档贡献](#文档贡献)
- [问题反馈](#问题反馈)
- [社区行为准则](#社区行为准则)

## 如何贡献

您可以通过以下方式参与项目：

### 代码贡献

- 修复 Bug
- 添加新功能
- 优化性能
- 重构代码

### 非代码贡献

- 完善文档
- 提交 Issue
- 参与讨论
- 测试验证

## 开发环境搭建

### 1. 克隆仓库

```bash
git clone https://github.com/winson-00178005/build-eye.git
cd build-eye
```

### 2. 安装依赖

```bash
# 安装运行依赖
pip install -r requirements.txt

# 安装开发依赖
pip install -r requirements-dev.txt
```

### 3. 配置开发环境

```bash
# 设置环境变量（可选）
export GITHUB_TOKEN="your_token_here"

# 创建本地测试目录
mkdir -p data reports
```

### 4. 运行模拟测试

```bash
python tests/mock_test.py
```

## 代码贡献流程

### 1. Fork 仓库

在 GitHub 上 Fork 本仓库到您的账号。

### 2. 创建分支

```bash
# 从 main 分支创建新分支
git checkout main
git pull origin main

# 创建功能分支
git checkout -b feature/your-feature-name

# 或创建修复分支
git checkout -b fix/your-bug-fix
```

### 3. 开发和测试

```bash
# 编写代码
# ...

# 运行测试
pytest tests/

# 运行模拟测试验证功能
python tests/mock_test.py
```

### 4. 提交变更

```bash
git add .
git commit -m "feat: 添加新分类规则支持"
```

### 5. 推送分支

```bash
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

- 在 GitHub 上创建 Pull Request
- 填写 PR 描述，说明变更内容和原因
- 等待代码审查

## 代码规范

### Python 代码规范

遵循以下规范：

- **PEP 8**: Python 代码风格指南
- **类型提示**: 使用 Python 类型注解
- **文档字符串**: 函数和类需添加 docstring

### 代码示例

```python
def detect_code_issues(
    log_excerpt: str,
    pr: Dict[str, Any],
    workflow_run: Dict[str, Any]
) -> Dict[str, Any]:
    """
    检测 PR 代码相关问题。
    
    Args:
        log_excerpt: 构建日志片段
        pr: PR 信息字典
        workflow_run: Workflow run 信息
    
    Returns:
        包含检测结果和证据的字典
    """
    # 实现逻辑
    pass
```

### 目录结构规范

```
scripts/
├── monitor/       # CI 监控模块
├── classify/      # 失败分类模块
├── recommend/     # 修复建议模块
├── report/        # 报告生成模块
└── archive/       # 报告归档模块
```

### 模块命名规范

- 文件名: 小写，使用下划线分隔（如 `code_detector.py`）
- 类名: 大驼峰（如 `FailureClassifier`）
- 函数名: 小写，使用下划线分隔（如 `detect_code_issues`）
- 常量名: 大写，使用下划线分隔（如 `CONFIDENCE_HIGH`）

## 提交规范

使用以下提交消息格式：

```
<type>: <subject>

<body>

<footer>
```

### Type 类型

| 类型 | 说明 |
|------|------|
| feat | 新功能 |
| fix | Bug 修复 |
| docs | 文档更新 |
| style | 代码格式调整（不影响逻辑） |
| refactor | 重构代码 |
| test | 测试相关 |
| chore | 构建、配置等 |

### 示例

```bash
# 新功能
git commit -m "feat: 支持 nightly 流水线监测"

# Bug 修复
git commit -m "fix: 修复 datetime 解析兼容性问题"

# 文档更新
git commit -m "docs: 更新 Token 配置指南"

# 重构
git commit -m "refactor: 优化分类引擎性能"
```

## 测试要求

### 运行测试

```bash
# 运行所有测试
pytest tests/

# 运行特定测试
pytest tests/test_classification.py -v

# 运行覆盖率测试
pytest tests/ --cov=scripts/
```

### 测试规范

- 每个新功能必须包含测试
- 测试文件命名: `test_<模块名>.py`
- 测试函数命名: `test_<功能描述>`
- 使用模拟数据进行测试，避免依赖真实 API

### 添加新测试

```python
def test_new_classification_pattern():
    """测试新的分类模式检测。"""
    
    log_excerpt = """
    HCCL error: rank 0 communication timeout
    """
    
    result = detect_infrastructure_issues(
        log_excerpt,
        {"runner_name": "linux-aarch64-a3-4"},
        {}
    )
    
    assert result["detected"] == True
    assert "hccl" in str(result["evidence"])
```

## 文档贡献

### 文档类型

- README.md: 项目概述和快速开始
- CONTRIBUTING.md: 贡献者指南
- docs/: 详细文档

### 文档规范

- 使用中文编写
- 使用 Markdown 格式
- 包含代码示例和截图
- 保持更新及时性

### 更新文档

```bash
# 文档变更提交
git add README.md docs/
git commit -m "docs: 更新安装说明"
```

## 问题反馈

### 提交 Issue

1. 在 GitHub Issues 页面创建新 Issue
2. 选择合适的模板（Bug 报告或功能请求）
3. 填写详细信息

### Issue 模板

**Bug 报告模板：**

```markdown
## Bug 描述

简要描述遇到的问题。

## 重现步骤

1. 运行命令 `python scripts/monitor/fetch_runs.py`
2. 出现错误 `KeyError: 'completed_at'`

## 期望结果

成功获取 workflow runs。

## 实际结果

出现 KeyError 异常。

## 环境信息

- Python 版本: 3.11
- 操作系统: Windows 11

## 日志输出

```
Traceback (most recent call last):
...
```
```

**功能请求模板：**

```markdown
## 功能描述

建议添加的功能。

## 使用场景

为什么需要这个功能？

## 建议方案

如何实现这个功能？
```

### 参与讨论

- 在 Issue 中发表意见
- 在 Pull Request 中参与代码审查
- 提出改进建议

## 社区行为准则

### 我们的承诺

为了营造开放和友好的环境，我们承诺：

- 尊重不同观点和经验
- 优雅地接受批评
- 关注社区整体利益
- 对其他社区成员表示同理心

### 不当行为

以下行为被视为不当：

- 使用性语言或图像
- 发布侮辱性/贬损性评论
- 公开或私下骚扰
- 未经许可发布他人私人信息
- 其他不道德或不专业的行为

### 报告问题

如遇到不当行为，请通过 GitHub Issues 报告。

## 获取帮助

- **GitHub Issues**: 提交问题和建议
- **README.md**: 查看项目文档
- **代码注释**: 查看代码内文档

## 致谢

感谢所有贡献者的付出！

---

**Happy Contributing!** 🎉