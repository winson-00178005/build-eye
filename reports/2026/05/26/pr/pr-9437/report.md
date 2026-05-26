---
report_id: c04ca998
pr_number: 9437
group_key: pr-9437
generated_at: 2026-05-26T03:03:16.967100+00:00
overall_classification: code
total_failed_workflows: 2
category_counts:
  code: 2
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9437

## 概要

PR #9437 触发了 2 个 workflow，均失败。

- **代码问题**: 2 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26429543529) | PR代码问题 | 高 | 编译错误 |
| 2 | E2E-Light (#26429088661) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26429543529)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9437 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26429543529)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26429543529/job/77799794510)

**日志片段**:
```
2026-05-26T02:57:06.1740629Z [31m-[m
2026-05-26T02:57:06.1740852Z              ].clone()[m
2026-05-26T02:57:06.1741402Z              self.slot_mapping_buf[num_decode_tokens : num_decode_tokens * self.pcp_size].fill_(-1)[m
2026-05-26T02:57:06.1741799Z  [m
2026-05-26T02:57:06.1742342Z [1mdiff --git a/vllm_ascend/attention/sfa_v1.py b/vllm_ascend/attention/sfa_v1.py[m
2026-05-26T02:57:06.1742829Z [1mindex 549e81d..3557ab8 100644[m
2026-05-26T02:57:06.1743204Z [1m--- a/vllm_ascend/attentio
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Light (Run #26429088661)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9437 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26429088661)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26429088661/job/77798483532)

**日志片段**:
```
2026-05-26T02:40:15.7898604Z [31m-            ].clone()[m
2026-05-26T02:40:15.7899221Z [32m+[m[32m            self.slot_mapping_buf[:num_actual_tokens_pcp_padded].copy_([m[41m
2026-05-26T02:40:15.7899561Z [m
2026-05-26T02:40:15.7900284Z [32m+[m[32m                common_attn_metadata.slot_mapping[:num_actual_tokens_pcp_padded], non_blocking=True[m[41m
2026-05-26T02:40:15.7900710Z [m
2026-05-26T02:40:15.7900996Z [32m+[m[32m            )[m[41m
2026-05-26T02:40:15.7901206Z [m
20
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26429543529)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26429088661)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-26T03:03:16.967162+00:00
