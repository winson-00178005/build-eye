---
report_id: 4691fa0c
pr_number: 9504
group_key: pr-9504
generated_at: 2026-05-25T10:08:18.225469+00:00
overall_classification: code
total_failed_workflows: 6
category_counts:
  code: 6
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9504

## 概要

PR #9504 触发了 6 个 workflow，均失败。

- **代码问题**: 6 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26393829494) | PR代码问题 | 高 | 编译错误 |
| 2 | E2E-Light (#26393536459) | PR代码问题 | 高 | 编译错误 |
| 3 | E2E-Light (#26393262900) | PR代码问题 | 中 | 编译错误 |
| 4 | E2E-Light (#26392845642) | PR代码问题 | 中 | 编译错误 |
| 5 | E2E-Light (#26392483438) | PR代码问题 | 中 | 编译错误 |
| 6 | E2E-Light (#26392132610) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26393829494)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9504 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26393829494)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26393829494/job/77689725097)

**日志片段**:
```
2026-05-25T09:38:54.7798278Z [36;1mfor python_version in "3.10" "3.11" "3.12"; do[0m
2026-05-25T09:38:54.7798596Z [36;1m  echo "============================"[0m
2026-05-25T09:38:54.7798845Z [36;1m  tools/mypy.sh 1 "$python_version"[0m
2026-05-25T09:38:54.7799102Z [36;1m  echo "============================"[0m
2026-05-25T09:38:54.7799321Z [36;1mdone[0m
2026-05-25T09:38:54.7799541Z shell: sh -e {0}
2026-05-25T09:38:54.7799704Z ##[endgroup]
2026-05-25T09:38:54.7886392Z ##[group]Run '/home
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. E2E-Light (Run #26393536459)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9504 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26393536459)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26393536459/job/77688791326)

**日志片段**:
```
2026-05-25T09:32:08.4458172Z pre-commit hook(s) made changes.
2026-05-25T09:32:08.4458735Z If you are seeing this message in CI, reproduce locally with: `pre-commit run --all-files`.
2026-05-25T09:32:08.4459407Z To run `pre-commit` as part of git workflow, use `pre-commit install`.
2026-05-25T09:32:08.4459893Z All changes made by hooks:
2026-05-25T09:32:08.5633727Z [1mdiff --git a/vllm_ascend/attention/dsa_v1.py b/vllm_ascend/attention/dsa_v1.py[m
2026-05-25T09:32:08.5635005Z [1mindex 4967914
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Light (Run #26393262900)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9504 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26393262900)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26393262900/job/77687884732)

**日志片段**:
```
2026-05-25T09:24:39.7752958Z          actual_tokens = attn_metadata[0].num_actual_tokens[m
2026-05-25T09:24:39.7753304Z  [m
2026-05-25T09:24:39.7753513Z [31m-[m
2026-05-25T09:24:39.7754027Z          # Delay allgather optimization: when prefill_comm_compute_overlap is[m
2026-05-25T09:24:39.7754697Z          # enabled and the batch is pure-prefill, wq_a/wkv can compute on the[m
2026-05-25T09:24:39.7755308Z          # local SP partition first, then allgather smaller intermediates.[m
2026-05-
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 4. E2E-Light (Run #26392845642)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9504 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26392845642)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26392845642/job/77686498018)

**日志片段**:
```
2026-05-25T09:14:17.2276363Z          assert self.rope_head_dim is not None[m
2026-05-25T09:14:17.2276831Z          kv = kv.view(-1, 1, self.nope_head_dim + self.rope_head_dim)[m
2026-05-25T09:14:17.2277296Z          torch.ops._C_ascend.inplace_partial_rotary_mul([m
2026-05-25T09:14:17.2277804Z [31m-            kv.unsqueeze(1), cos, sin,[m
2026-05-25T09:14:17.2278200Z [32m+[m[32m            kv.unsqueeze(1),[m
2026-05-25T09:14:17.2278545Z [32m+[m[32m            cos,[m
2026-05-25T09:1
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. E2E-Light (Run #26392483438)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9504 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26392483438)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26392483438/job/77685328287)

**日志片段**:
```
2026-05-25T09:02:34.5462800Z  [m
2026-05-25T09:02:34.5463486Z          return q, qr, full_hidden_states[m
2026-05-25T09:02:34.5464323Z  [m
2026-05-25T09:02:34.5465151Z [36m@@ -1803,7 +1803,11 @@[m [mclass AscendDSAImpl(DSAAttentionImpl):[m
2026-05-25T09:02:34.5465889Z          elif need_prefill_gather:[m
2026-05-25T09:02:34.5466658Z              # Delayed allgather + compute-communication overlap[m
2026-05-25T09:02:34.5467605Z              q, qr, hidden_states = self._mla_prolog_prefill
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 6. E2E-Light (Run #26392132610)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9504 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26392132610)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26392132610/job/77684192590)

**日志片段**:
```
2026-05-25T08:53:38.8927511Z [32m+[m[32m        torch.ops._C_ascend.npu_scatter_nd_update_v2(swa_kv_cache, slot_mapping, kv)[m
2026-05-25T08:53:38.8927888Z  [m
2026-05-25T08:53:38.8928337Z          return q, qr, full_hidden_states[m
2026-05-25T08:53:38.8928581Z  [m
2026-05-25T08:53:38.8929041Z [36m@@ -1803,7 +1803,10 @@[m [mclass AscendDSAImpl(DSAAttentionImpl):[m
2026-05-25T08:53:38.8929457Z          elif need_prefill_gather:[m
2026-05-25T08:53:38.8929885Z              # Delayed all
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26393829494)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26393536459)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26393262900)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26392845642)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26392483438)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26392132610)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-25T10:08:18.225517+00:00
