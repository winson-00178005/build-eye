---
report_id: 57f7212c
pr_number: 10114
group_key: pr-10114
generated_at: 2026-06-05T23:12:08.919306+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #10114

## 概要

PR #10114 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Cache csrc Build Artifacts (#27018057729) | PR代码问题 | 中 | 编译错误 |
| 2 | Cache csrc Build Artifacts (#27016914528) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Cache csrc Build Artifacts (Run #27018057729)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10114 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27018057729)
[查看 Job: build-X64-a3-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27018057729/job/79738316552)
[查看 Job: build-ARM64-a3-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27018057729/job/79738316574)
[查看 Job: build-X64-a2-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27018057729/job/79738316605)

**日志片段**:
```
2026-06-05T13:53:01.0188907Z                        from
2026-06-05T13:53:01.0189289Z       /__w/vllm-ascend/vllm-ascend/csrc/attention/sparse_attn_sharedkv_metadata/op_kernel_aicpu/sparse_attn_sharedkv_metadata_aicpu.cpp:16:
2026-06-05T13:53:01.0189524Z       /usr/include/c++/12/x86_64-openEuler-linux/bits/c++config.h:521:46:
2026-06-05T13:53:01.0189643Z       error: missing binary operator before token "("
2026-06-05T13:53:01.0189740Z        #elif __cplusplus >= 201103L &&
2026-06-05T13:53:01.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. Cache csrc Build Artifacts (Run #27016914528)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #10114 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/27016914528)
[查看 Job: build-X64-a3-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27016914528/job/79734256817)
[查看 Job: build-X64-a2-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27016914528/job/79734256863)
[查看 Job: build-ARM64-a2-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27016914528/job/79734256879)
[查看 Job: build-X64-310p-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27016914528/job/79734256916)
[查看 Job: build-ARM64-310p-openeuler-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/27016914528/job/79734256958)

**日志片段**:
```
2026-06-05T13:26:19.2010367Z                        from
2026-06-05T13:26:19.2010882Z       /__w/vllm-ascend/vllm-ascend/csrc/attention/sparse_attn_sharedkv_metadata/op_kernel_aicpu/sparse_attn_sharedkv_metadata_aicpu.cpp:16:
2026-06-05T13:26:19.2011505Z       /usr/include/c++/12/x86_64-openEuler-linux/bits/c++config.h:521:46:
2026-06-05T13:26:19.2011869Z       error: missing binary operator before token "("
2026-06-05T13:26:19.2012156Z        #elif __cplusplus >= 201103L &&
2026-06-05T13:26:19.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Cache csrc Build Artifacts (#27018057729)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Cache csrc Build Artifacts (#27016914528)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-06-05T23:12:08.919347+00:00
