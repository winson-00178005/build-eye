---
report_id: 3fd6e96f
pr_number: 9389
group_key: pr-9389
generated_at: 2026-05-22T03:10:53.556856+00:00
overall_classification: code
total_failed_workflows: 4
category_counts:
  code: 4
  infrastructure: 0
  interference: 0
---

# 构建失败报告: PR #9389

## 概要

PR #9389 触发了 4 个 workflow，均失败。

- **代码问题**: 4 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | Image build lint (#26254056723) | PR代码问题 | 高 | 编译错误 |
| 2 | vLLM Main Schedule Test (#26253935630) | PR代码问题 | 中 | 编译错误 |
| 3 | Nightly-A2 (#26243068887) | PR代码问题 | 高 | 编译错误 |
| 4 | vLLM Main Schedule Test (#26239472511) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. Image build lint (Run #26254056723)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9389 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26254056723)
[查看 PR #9389](https://github.com/vllm-project/vllm-ascend/pull/9389)
[查看 Job: vllm-ascend lint image build](https://github.com/vllm-project/vllm-ascend/actions/runs/26254056723/job/77272297499)

**日志片段**:
```
2026-05-21T21:28:23.2009520Z #11 2.904 ERROR: Ignored the following versions that require a different python version: 1.6.2 Requires-Python >=3.7,<3.10; 1.6.3 Requires-Python >=3.7,<3.10; 1.7.0 Requires-Python >=3.7,<3.10; 1.7.1 Requires-Python >=3.7,<3.10; 1.7.2 Requires-Python >=3.7,<3.11; 1.7.3 Requires-Python >=3.7,<3.11; 1.8.0 Requires-Python >=3.8,<3.11; 1.8.0rc1 Requires-Python >=3.8,<3.11; 1.8.0rc2 Requires-Python >=3.8,<3.11; 1.8.0rc3 Requires-Python >=3.8,<3.11; 1.8.0rc4 Requires-Pytho
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. vLLM Main Schedule Test (Run #26253935630)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9389 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26253935630)
[查看 PR #9389](https://github.com/vllm-project/vllm-ascend/pull/9389)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26253935630/job/77271884750)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26253935630/job/77271884761)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26253935630/job/77271884765)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26253935630/job/77271884784)

**日志片段**:
```
2026-05-21T21:36:22.1691691Z   UV_NO_CACHE: 1
2026-05-21T21:36:22.1691879Z   UV_SYSTEM_PYTHON: 1
2026-05-21T21:36:22.1692072Z ##[endgroup]
2026-05-21T21:36:22.1795657Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T21:36:22.1796646Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T21:36:22.1796948Z ##[endgroup]
2026-05-21T21:36:22.6612352Z (node:1362) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. Nightly-A2 (Run #26243068887)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9389 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887)
[查看 PR #9389](https://github.com/vllm-project/vllm-ascend/pull/9389)
[查看 Job: doc-test / vLLM Ascend test (nightly-main-openeuler)](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77234205245)
[查看 Job: doc-test / vLLM Ascend test (nightly-main)](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77234205349)
[查看 Job: single-node (main, test_custom_op, linux-aarch64-a2b3-1, tests/e2e/nightly/single_node/ops/single... / test_custom_op](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77236408602)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-3, linux-aarch64-a2b3-2, Qwen3-30B-A3B, Qwen3-VL... / [
  "Qwen3-30B-A3B",
  "Qwen3-VL-30B-A3B-Instruct",
  "Qwen3-30B-A3B-W8A8"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77236408614)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-1, linux-aarch64-a2b3-1, Qwen3-VL-8B-Instruct-W8... / [
  "Qwen3-VL-8B-Instruct-W8A8",
  "Qwen3-8B",
  "Qwen2-Audio-7B-Instruct",
  "Qwen3-8B-W8A8",
  "Qwen3-VL-8B-Instruct",
  "Minitron-8B-Base"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77236408615)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-4, linux-aarch64-a2b3-4, Qwen3-Next-80B-A3B-Inst... / [
  "Qwen3-Next-80B-A3B-Instruct",
  "Qwen3-Omni-30B-A3B-Instruct",
  "Hunyuan-A13B-Instruct",
  "Mixtral-8x7B-Instruct-v0.1"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77236408637)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-2, linux-aarch64-a2b3-1, ERNIE-4.5-21B-A3B-PT, I... / [
  "ERNIE-4.5-21B-A3B-PT",
  "InternVL3_5-8B-hf",
  "Molmo-7B-D-0924",
  "Llama-3.2-3B-Instruct",
  "llava-onevision-qwen2-0.5b-ov-hf"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77236408660)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A2, linux-aarch64-a2b3-8, MiniMax-M2.5-w8a8-QuaRot-A2... / MiniMax-M2.5-w8a8-QuaRot-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77236408906)
[查看 Job: multi-node (main, multi-node-qwen3-235b-dp, Qwen3-235B-A22B-A2.yaml, 2) / Qwen3-235B-A22B-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887/job/77248587847)

**日志片段**:
```
2026-05-21T18:06:39.5734623Z   File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/platform.py", line 151, in pre_register_and_update
2026-05-21T18:06:39.5735372Z     from vllm_ascend.quantization import AscendCompressedTensorsConfig, AscendModelSlimConfig  # noqa: F401
2026-05-21T18:06:39.5735876Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-21T18:06:39.5736238Z   File "<frozen importlib._bootstrap>", line 1229, in _handle_froml
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 4. vLLM Main Schedule Test (Run #26239472511)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9389 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26239472511)
[查看 PR #9389](https://github.com/vllm-project/vllm-ascend/pull/9389)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26239472511/job/77221624526)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26239472511/job/77221624591)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26239472511/job/77221624598)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26239472511/job/77221624787)

**日志片段**:
```
2026-05-21T18:22:35.9553557Z   UV_NO_CACHE: 1
2026-05-21T18:22:35.9553813Z   UV_SYSTEM_PYTHON: 1
2026-05-21T18:22:35.9554044Z ##[endgroup]
2026-05-21T18:22:35.9646255Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T18:22:35.9647385Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T18:22:35.9647812Z ##[endgroup]
2026-05-21T18:22:36.4437157Z (node:1459) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **Image build lint (#26254056723)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26253935630)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26243068887)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26239472511)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T03:10:53.556910+00:00
