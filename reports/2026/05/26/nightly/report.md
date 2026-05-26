---
report_id: 032701ed
report_type: nightly_daily
date: 2026-05-26
generated_at: 2026-05-26T03:12:15.265543+00:00
total_runs: 50
success_runs: 10
failure_runs: 40
---

# Nightly 构建报告 - 2026-05-26

## 概览

| 指标 | 数值 |
|------|------|
| 运行总数 | 50 |
| 成功率 | 20.0% |
| 失败数 | 40 |
| 平均时长 | 186.6 分钟 |




## 失败详情

- 失败 (40)

**根因分类**:
- 代码问题 (34)
- 基础设施问题 (6)

| # | Workflow | 状态 | 根因 | 置信度 | 详情 |
|---|---|---|---|---|---|
| 1 | vLLM Main Schedule Test (#26419606840) | 失败 | 代码问题 | 高 | 编译错误 |
| 2 | Nightly-A2 (#26412181441) | 失败 | 代码问题 | 高 | 编译错误 |
| 3 | vLLM Main Schedule Test (#26409927217) | 失败 | 代码问题 | 高 | 编译错误 |
| 4 | vLLM Main Schedule Test (#26398978835) | 失败 | 代码问题 | 高 | 编译错误 |
| 5 | vLLM Main Schedule Test (#26386592221) | 失败 | 代码问题 | 高 | 编译错误 |
| 6 | vLLM Main Schedule Test (#26372402659) | 失败 | 代码问题 | 高 | 编译错误 |
| 7 | Nightly-A2 (#26366938206) | 失败 | 代码问题 | 高 | 编译错误 |
| 8 | Nightly-A3 (#26366927091) | 失败 | 基础设施问题 | 中 | K8s内部服务失败 |
| 9 | vLLM Main Schedule Test (#26364582559) | 失败 | 代码问题 | 高 | 编译错误 |
| 10 | Docs link check (#26362038335) | 失败 | 代码问题 | 高 | 编译错误 |
| 11 | E2E-upstream (#26358050036) | 失败 | 代码问题 | 高 | 编译错误 |
| 12 | vLLM Main Schedule Test (#26358021964) | 失败 | 代码问题 | 高 | 编译错误 |
| 13 | vLLM Main Schedule Test (#26353449009) | 失败 | 代码问题 | 高 | 编译错误 |
| 14 | vLLM Main Schedule Test (#26343078965) | 失败 | 代码问题 | 高 | 编译错误 |
| 15 | Nightly-A3 (#26338068996) | 失败 | 基础设施问题 | 中 | K8s内部服务失败 |
| 16 | Nightly-A2 (#26338064984) | 失败 | 代码问题 | 高 | 编译错误 |
| 17 | vLLM Main Schedule Test (#26335885645) | 失败 | 代码问题 | 高 | 编译错误 |
| 18 | Release Code and Wheel (#26329744775) | 失败 | 基础设施问题 | 低 | 未能明确归类 |
| 19 | vLLM Main Schedule Test (#26329602920) | 失败 | 代码问题 | 高 | 编译错误 |
| 20 | vLLM Main Schedule Test (#26324769664) | 失败 | 代码问题 | 高 | 编译错误 |
| 21 | vLLM Main Schedule Test (#26311912901) | 失败 | 代码问题 | 高 | 编译错误 |
| 22 | Nightly-A3 (#26302347768) | 失败 | 基础设施问题 | 中 | K8s内部服务失败 |
| 23 | Nightly-A2 (#26302345284) | 失败 | 代码问题 | 高 | 编译错误 |
| 24 | vLLM Main Schedule Test (#26299256650) | 失败 | 代码问题 | 高 | 编译错误 |
| 25 | vLLM Main Schedule Test (#26283288369) | 失败 | 代码问题 | 高 | 编译错误 |
| 26 | Release Code and Wheel (#26271541708) | 失败 | 代码问题 | 高 | 编译错误 |
| 27 | vLLM Main Schedule Test (#26271314173) | 失败 | 代码问题 | 高 | 编译错误 |
| 28 | Image build lint (#26254056723) | 失败 | 代码问题 | 高 | 编译错误 |
| 29 | vLLM Main Schedule Test (#26253935630) | 失败 | 代码问题 | 高 | 编译错误 |
| 30 | Nightly-A2 (#26243068887) | 失败 | 代码问题 | 高 | 编译错误 |
| 31 | Nightly-A3 (#26243065104) | 失败 | 基础设施问题 | 中 | K8s内部服务失败 |
| 32 | vLLM Main Schedule Test (#26239472511) | 失败 | 代码问题 | 高 | 编译错误 |
| 33 | Release Code and Wheel (#26223112224) | 失败 | 代码问题 | 高 | 编译错误 |
| 34 | vLLM Main Schedule Test (#26222654971) | 失败 | 代码问题 | 高 | 编译错误 |
| 35 | Release Code and Wheel (#26208851000) | 失败 | 代码问题 | 高 | 编译错误 |
| 36 | vLLM Main Schedule Test (#26208639745) | 失败 | 代码问题 | 高 | 编译错误 |
| 37 | Image build lint (#26192072868) | 失败 | 代码问题 | 高 | 编译错误 |
| 38 | vLLM Main Schedule Test (#26191916523) | 失败 | 代码问题 | 高 | 编译错误 |
| 39 | Nightly-A2 (#26180770916) | 失败 | 代码问题 | 高 | 编译错误 |
| 40 | Nightly-A3 (#26180748860) | 失败 | 基础设施问题 | 中 | K8s内部服务失败 |


## 失败 Workflow 详细分析
### 1. vLLM Main Schedule Test (Run #26419606840)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26419606840)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26419606840/job/77771390133)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26419606840/job/77771390139)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26419606840/job/77771390151)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26419606840/job/77771390152)

**日志片段**:
```
2026-05-25T21:16:10.6742884Z   UV_HTTP_TIMEOUT: 120
2026-05-25T21:16:10.6743135Z   UV_NO_CACHE: 1
2026-05-25T21:16:10.6743401Z   UV_SYSTEM_PYTHON: 1
2026-05-25T21:16:10.6743958Z ##[endgroup]
2026-05-25T21:16:10.6831433Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-25T21:16:10.6832519Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-25T21:16:10.6832850Z ##[endgroup]
2026-05-25T21:16:11.1697909Z (node:1618) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 2. Nightly-A2 (Run #26412181441)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441)
[查看 Job: doc-test / vLLM Ascend test (nightly-main)](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77748845093)
[查看 Job: doc-test / vLLM Ascend test (nightly-main-openeuler)](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77748845100)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-1, linux-aarch64-a2b3-1, Qwen3-VL-8B-Instruct-W8... / [
  "Qwen3-VL-8B-Instruct-W8A8",
  "Qwen3-8B",
  "Qwen2-Audio-7B-Instruct",
  "Qwen3-8B-W8A8",
  "Qwen3-VL-8B-Instruct",
  "Minitron-8B-Base"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880560)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-2, linux-aarch64-a2b3-1, ERNIE-4.5-21B-A3B-PT, I... / [
  "ERNIE-4.5-21B-A3B-PT",
  "InternVL3_5-8B-hf",
  "Molmo-7B-D-0924",
  "Llama-3.2-3B-Instruct",
  "llava-onevision-qwen2-0.5b-ov-hf"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880603)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-3, linux-aarch64-a2b3-2, Qwen3-30B-A3B, Qwen3-VL... / [
  "Qwen3-30B-A3B",
  "Qwen3-VL-30B-A3B-Instruct",
  "Qwen3-30B-A3B-W8A8"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880648)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-4, linux-aarch64-a2b3-4, Qwen3-Next-80B-A3B-Inst... / [
  "Qwen3-Next-80B-A3B-Instruct",
  "Qwen3-Omni-30B-A3B-Instruct",
  "Hunyuan-A13B-Instruct",
  "Mixtral-8x7B-Instruct-v0.1"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880692)
[查看 Job: single-node (main, test_custom_op, linux-aarch64-a2b3-1, tests/e2e/nightly/single_node/ops/single... / test_custom_op](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880705)
[查看 Job: single-node (main, Qwen3.5-397B-A17B-w4a8-mtp, linux-aarch64-a2b3-8, Qwen3.5-397B-A17B-w4a8-mtp-A... / Qwen3.5-397B-A17B-w4a8-mtp](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880752)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A2, linux-aarch64-a2b3-8, MiniMax-M2.5-w8a8-QuaRot-A2... / MiniMax-M2.5-w8a8-QuaRot-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880760)
[查看 Job: single-node (main, Qwen3.5-27B-w8a8-A2, linux-aarch64-a2b3-2, Qwen3.5-27B-w8a8-A2.yaml) / Qwen3.5-27B-w8a8-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77784880770)
[查看 Job: multi-node (main, multi-node-qwen3-235b-dp, Qwen3-235B-A22B-A2.yaml, 2) / Qwen3-235B-A22B-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26412181441/job/77788422770)

**日志片段**:
```
2026-05-25T17:39:54.0558152Z   File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/platform.py", line 151, in pre_register_and_update
2026-05-25T17:39:54.0558812Z     from vllm_ascend.quantization import AscendCompressedTensorsConfig, AscendModelSlimConfig  # noqa: F401
2026-05-25T17:39:54.0559441Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-25T17:39:54.0559807Z   File "<frozen importlib._bootstrap>", line 1229, in _handle_froml
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. vLLM Main Schedule Test (Run #26409927217)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26409927217)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26409927217/job/77741932835)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26409927217/job/77741932841)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26409927217/job/77741932860)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26409927217/job/77741932876)

**日志片段**:
```
2026-05-25T16:36:29.7319551Z   UV_HTTP_TIMEOUT: 120
2026-05-25T16:36:29.7319785Z   UV_NO_CACHE: 1
2026-05-25T16:36:29.7320049Z   UV_SYSTEM_PYTHON: 1
2026-05-25T16:36:29.7320518Z ##[endgroup]
2026-05-25T16:36:29.7406038Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-25T16:36:29.7407199Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-25T16:36:29.7407536Z ##[endgroup]
2026-05-25T16:36:30.2243516Z (node:1487) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 4. vLLM Main Schedule Test (Run #26398978835)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26398978835)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26398978835/job/77706350526)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26398978835/job/77706350527)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26398978835/job/77706350529)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26398978835/job/77706350553)

**日志片段**:
```
2026-05-25T12:11:10.4949631Z   UV_HTTP_TIMEOUT: 120
2026-05-25T12:11:10.4950128Z   UV_NO_CACHE: 1
2026-05-25T12:11:10.4950762Z   UV_SYSTEM_PYTHON: 1
2026-05-25T12:11:10.4951596Z ##[endgroup]
2026-05-25T12:11:10.5088501Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-25T12:11:10.5090196Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-25T12:11:10.5090728Z ##[endgroup]
2026-05-25T12:11:10.9931915Z (node:1669) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. vLLM Main Schedule Test (Run #26386592221)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26386592221)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26386592221/job/77666350782)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26386592221/job/77666350784)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26386592221/job/77666350798)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26386592221/job/77666350802)

**日志片段**:
```
2026-05-25T06:40:20.3348792Z   UV_HTTP_TIMEOUT: 120
2026-05-25T06:40:20.3348989Z   UV_NO_CACHE: 1
2026-05-25T06:40:20.3349223Z   UV_SYSTEM_PYTHON: 1
2026-05-25T06:40:20.3349418Z ##[endgroup]
2026-05-25T06:40:20.3439360Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-25T06:40:20.3440276Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-25T06:40:20.3440564Z ##[endgroup]
2026-05-25T06:40:20.8142193Z (node:1688) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 6. vLLM Main Schedule Test (Run #26372402659)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26372402659)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26372402659/job/77626779954)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26372402659/job/77626779955)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26372402659/job/77626779958)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26372402659/job/77626779959)

**日志片段**:
```
2026-05-24T21:29:14.9352774Z   UV_HTTP_TIMEOUT: 120
2026-05-24T21:29:14.9352977Z   UV_NO_CACHE: 1
2026-05-24T21:29:14.9353202Z   UV_SYSTEM_PYTHON: 1
2026-05-24T21:29:14.9353402Z ##[endgroup]
2026-05-24T21:29:14.9455713Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-24T21:29:14.9457254Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-24T21:29:14.9457753Z ##[endgroup]
2026-05-24T21:29:15.4360671Z (node:1529) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 7. Nightly-A2 (Run #26366938206)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206)
[查看 Job: doc-test / vLLM Ascend test (nightly-main)](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612258480)
[查看 Job: doc-test / vLLM Ascend test (nightly-main-openeuler)](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612258482)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-2, linux-aarch64-a2b3-1, ERNIE-4.5-21B-A3B-PT, I... / [
  "ERNIE-4.5-21B-A3B-PT",
  "InternVL3_5-8B-hf",
  "Molmo-7B-D-0924",
  "Llama-3.2-3B-Instruct",
  "llava-onevision-qwen2-0.5b-ov-hf"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902205)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-4, linux-aarch64-a2b3-4, Qwen3-Next-80B-A3B-Inst... / [
  "Qwen3-Next-80B-A3B-Instruct",
  "Qwen3-Omni-30B-A3B-Instruct",
  "Hunyuan-A13B-Instruct",
  "Mixtral-8x7B-Instruct-v0.1"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902210)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-1, linux-aarch64-a2b3-1, Qwen3-VL-8B-Instruct-W8... / [
  "Qwen3-VL-8B-Instruct-W8A8",
  "Qwen3-8B",
  "Qwen2-Audio-7B-Instruct",
  "Qwen3-8B-W8A8",
  "Qwen3-VL-8B-Instruct",
  "Minitron-8B-Base"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902220)
[查看 Job: single-node (main, test_custom_op, linux-aarch64-a2b3-1, tests/e2e/nightly/single_node/ops/single... / test_custom_op](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902261)
[查看 Job: single-node (main, Qwen3.5-397B-A17B-w4a8-mtp, linux-aarch64-a2b3-8, Qwen3.5-397B-A17B-w4a8-mtp-A... / Qwen3.5-397B-A17B-w4a8-mtp](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902264)
[查看 Job: single-node (main, Qwen3.5-27B-w8a8-A2, linux-aarch64-a2b3-2, Qwen3.5-27B-w8a8-A2.yaml) / Qwen3.5-27B-w8a8-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902265)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-3, linux-aarch64-a2b3-2, Qwen3-30B-A3B, Qwen3-VL... / [
  "Qwen3-30B-A3B",
  "Qwen3-VL-30B-A3B-Instruct",
  "Qwen3-30B-A3B-W8A8"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902268)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A2, linux-aarch64-a2b3-8, MiniMax-M2.5-w8a8-QuaRot-A2... / MiniMax-M2.5-w8a8-QuaRot-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77612902290)
[查看 Job: multi-node (main, multi-node-qwen3-235b-dp, Qwen3-235B-A22B-A2.yaml, 2) / Qwen3-235B-A22B-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366938206/job/77629051373)

**日志片段**:
```
2026-05-24T17:01:07.5610641Z   File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/platform.py", line 151, in pre_register_and_update
2026-05-24T17:01:07.5611364Z     from vllm_ascend.quantization import AscendCompressedTensorsConfig, AscendModelSlimConfig  # noqa: F401
2026-05-24T17:01:07.5611862Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-24T17:01:07.5612496Z   File "<frozen importlib._bootstrap>", line 1229, in _handle_froml
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 8. Nightly-A3 (Run #26366927091)

- **状态**: 失败
- **根因分类**: 基础设施问题
- **置信度**: 中
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'single-node (main, deepseek-r1-0528-w8a8, linux-aarch64-a3-16, DeepSeek-R1-0528-W8A8.yaml) / deepseek-r1-0528-w8a8' 中。 Runner: linux-aarch64-a3-16-l6dgl-runner-fxv8l。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP, DeepSeek-V3_2-W8A8-EP.yaml, 4) / DeepSeek-V3_2-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77612917066)
[查看 Job: multi-node (main, multi-node-GLM5_1-W8A8-EP, GLM5_1-W8A8-EP.yaml, 4) / GLM5_1-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77617276304)
[查看 Job: double-node (main, multi-node-qwen3-dp, Qwen3-235B-A22B.yaml, 2) / Qwen3-235B-A22B.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77619338888)
[查看 Job: double-node (main, multi-node-qwenw8a8-2node-eplb, Qwen3-235B-W8A8-EPLB.yaml, 2) / Qwen3-235B-W8A8-EPLB.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77620358442)
[查看 Job: double-node (main, multi-node-qwen3-dp-mooncake-layerwise, Qwen3-235B-A22B-Mooncake-Layerwise.yam... / Qwen3-235B-A22B-Mooncake-Layerwise.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77623522179)
[查看 Job: double-node (main, multi-node-GLM-5.1-w8a8-A3, GLM5_1-W8A8-A3-dual-nodes.yaml, 2) / GLM5_1-W8A8-A3-dual-nodes.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77628526534)
[查看 Job: single-node (main, deepseek-r1-0528-w8a8, linux-aarch64-a3-16, DeepSeek-R1-0528-W8A8.yaml) / deepseek-r1-0528-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77630452842)
[查看 Job: single-node (main, deepseek-v3-2-w8a8, linux-aarch64-a3-16, DeepSeek-V3.2-W8A8.yaml) / deepseek-v3-2-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77630452845)
[查看 Job: single-node (main, qwen3-vl-235b-a22b-instruct-w8a8, linux-aarch64-a3-16, Qwen3-VL-235B-A22B-Inst... / qwen3-vl-235b-a22b-instruct-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77630452854)
[查看 Job: single-node (main, glm-4.7-w8a8, linux-aarch64-a3-16, GLM-4.7.yaml) / glm-4.7-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77630452869)
[查看 Job: single-node (main, mtpx-deepseek-r1-0528-w8a8, linux-aarch64-a3-16, MTPX-DeepSeek-R1-0528-W8A8.yaml) / mtpx-deepseek-r1-0528-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77630452879)
[查看 Job: single-node (main, kimi-k2.5, linux-aarch64-a3-16, Kimi-K2.5.yaml) / kimi-k2.5](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77630662939)
[查看 Job: single-node (main, Qwen3.5-397B-A17B-w8a8-mtp, linux-aarch64-a3-16, Qwen3.5-397B-A17B-W8A8-mtp-A3... / Qwen3.5-397B-A17B-w8a8-mtp](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77635204156)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A3, linux-aarch64-a3-16, MiniMax-M2.5-w8a8-QuaRot-A3.... / MiniMax-M2.5-w8a8-QuaRot-A3](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77636599958)
[查看 Job: single-node (main, Qwen3.5-27B-w8a8-A3, linux-aarch64-a3-2, Qwen3.5-27B-w8a8-A3.yaml) / Qwen3.5-27B-w8a8-A3](https://github.com/vllm-project/vllm-ascend/actions/runs/26366927091/job/77638242734)

**日志片段**:
```
2026-05-24T18:07:20.0491527Z [36;1m  "file_count": ${FILE_COUNT},[0m
2026-05-24T18:07:20.0491805Z [36;1m  "total_size": ${TOTAL_SIZE},[0m
2026-05-24T18:07:20.0492082Z [36;1m  "created_at": "${CREATED_AT}",[0m
2026-05-24T18:07:20.0492410Z [36;1m  "retention_days": 90,[0m
2026-05-24T18:07:20.0492681Z [36;1m  "workflow": "Nightly-A3",[0m
2026-05-24T18:07:20.0493053Z [36;1m  "job": "e2e",[0m
2026-05-24T18:07:20.0493353Z [36;1m  "sha": "1383e98c4ca4bdae75969057c0c21c3ad1ccb036"[0m
2026-
```

**修复建议**:
- **优先**: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

### 9. vLLM Main Schedule Test (Run #26364582559)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26364582559)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26364582559/job/77606056720)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26364582559/job/77606056723)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26364582559/job/77606056726)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26364582559/job/77606056727)

**日志片段**:
```
2026-05-24T15:15:11.3888800Z   UV_HTTP_TIMEOUT: 120
2026-05-24T15:15:11.3889026Z   UV_NO_CACHE: 1
2026-05-24T15:15:11.3889277Z   UV_SYSTEM_PYTHON: 1
2026-05-24T15:15:11.3889517Z ##[endgroup]
2026-05-24T15:15:11.3976988Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-24T15:15:11.3978086Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-24T15:15:11.3978439Z ##[endgroup]
2026-05-24T15:15:11.8799063Z (node:1547) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 10. Docs link check (Run #26362038335)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26362038335)
[查看 Job: Sphinx linkcheck](https://github.com/vllm-project/vllm-ascend/actions/runs/26362038335/job/77599150982)

**日志片段**:
```
2026-05-24T13:09:33.9859648Z (community/contributors: line  178) [32mok        [39;49;00mhttps://github.com/vllm-project/vllm-ascend/commit/00ea61ec885e21ed0e51dc8e751cb27cfa539dc3
2026-05-24T13:09:35.8915794Z (tutorials/features/suffix_speculative_decoding: line   66) [35mredirect  [39;49;00mhttps://www.snowflake.com/en/engineering-blog/fast-speculative-decoding-vllm-arctic/[35m - permanently to https://www.snowflake.com/en/blog/engineering/fast-speculative-decoding-vllm-arctic/[39;49;00m
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 11. E2E-upstream (Run #26358050036)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26358050036)
[查看 Job: e2e-upstream_singlecard (0, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358050036/job/77588316533)
[查看 Job: e2e-upstream_singlecard (3, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358050036/job/77588316538)
[查看 Job: e2e-upstream_singlecard (2, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358050036/job/77588316547)
[查看 Job: e2e-upstream_singlecard (1, v0.20.2)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358050036/job/77588316548)

**日志片段**:
```
2026-05-24T10:17:34.7163896Z   ERROR: Failed building editable for vllm_ascend
2026-05-24T10:17:34.7163989Z error: failed-wheel-build-for-install
2026-05-24T10:17:34.7164005Z 
2026-05-24T10:17:34.7164309Z Ã Failed to build installable wheels for some pyproject.toml based projects
2026-05-24T10:17:34.7164414Z â°â> vllm_ascend
2026-05-24T10:17:34.7164501Z Failed to build vllm_ascend
2026-05-24T10:17:35.6188777Z ##[error]Error: failed to run script step: Error: command terminated with non-zero 
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 12. vLLM Main Schedule Test (Run #26358021964)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26358021964)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358021964/job/77588238875)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358021964/job/77588238884)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358021964/job/77588238887)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26358021964/job/77588238888)

**日志片段**:
```
2026-05-24T10:06:56.6231753Z   UV_HTTP_TIMEOUT: 120
2026-05-24T10:06:56.6231949Z   UV_NO_CACHE: 1
2026-05-24T10:06:56.6232147Z   UV_SYSTEM_PYTHON: 1
2026-05-24T10:06:56.6232329Z ##[endgroup]
2026-05-24T10:06:56.6318272Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-24T10:06:56.6319189Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-24T10:06:56.6319470Z ##[endgroup]
2026-05-24T10:06:57.0942920Z (node:1757) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 13. vLLM Main Schedule Test (Run #26353449009)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26353449009)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26353449009/job/77575663042)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26353449009/job/77575663044)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26353449009/job/77575663055)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26353449009/job/77575663058)

**日志片段**:
```
2026-05-24T06:11:17.4885550Z   UV_NO_CACHE: 1
2026-05-24T06:11:17.4885837Z   UV_SYSTEM_PYTHON: 1
2026-05-24T06:11:17.4886111Z ##[endgroup]
2026-05-24T06:11:17.4978431Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-24T06:11:17.4979814Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-24T06:11:17.4980174Z ##[endgroup]
2026-05-24T06:11:17.9787376Z (node:1343) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 14. vLLM Main Schedule Test (Run #26343078965)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26343078965)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26343078965/job/77548370317)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26343078965/job/77548370325)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26343078965/job/77548370328)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26343078965/job/77548370329)

**日志片段**:
```
2026-05-23T21:06:07.1590900Z   UV_NO_CACHE: 1
2026-05-23T21:06:07.1591119Z   UV_SYSTEM_PYTHON: 1
2026-05-23T21:06:07.1591291Z ##[endgroup]
2026-05-23T21:06:07.1681322Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-23T21:06:07.1682123Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-23T21:06:07.1682368Z ##[endgroup]
2026-05-23T21:06:07.6231885Z (node:1412) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 15. Nightly-A3 (Run #26338068996)

- **状态**: 失败
- **根因分类**: 基础设施问题
- **置信度**: 中
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'single-node (main, deepseek-v3-2-w8a8, linux-aarch64-a3-16, DeepSeek-V3.2-W8A8.yaml) / deepseek-v3-2-w8a8' 中。 Runner: linux-aarch64-a3-16-l6dgl-runner-wcks7。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP, DeepSeek-V3_2-W8A8-EP.yaml, 4) / DeepSeek-V3_2-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77535762180)
[查看 Job: multi-node (main, multi-node-GLM5_1-W8A8-EP, GLM5_1-W8A8-EP.yaml, 4) / GLM5_1-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77539701601)
[查看 Job: double-node (main, multi-node-qwen3-dp, Qwen3-235B-A22B.yaml, 2) / Qwen3-235B-A22B.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77541484361)
[查看 Job: double-node (main, multi-node-qwen3-dp-mooncake-layerwise, Qwen3-235B-A22B-Mooncake-Layerwise.yam... / Qwen3-235B-A22B-Mooncake-Layerwise.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77545448071)
[查看 Job: double-node (main, multi-node-deepseek-v3.1, DeepSeek-V3.1-BF16.yaml, 2) / DeepSeek-V3.1-BF16.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77549763484)
[查看 Job: double-node (main, multi-node-GLM-5.1-w8a8-A3, GLM5_1-W8A8-A3-dual-nodes.yaml, 2) / GLM5_1-W8A8-A3-dual-nodes.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77549885712)
[查看 Job: single-node (main, deepseek-v3-2-w8a8, linux-aarch64-a3-16, DeepSeek-V3.2-W8A8.yaml) / deepseek-v3-2-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77551770610)
[查看 Job: single-node (main, glm-4.7-w8a8, linux-aarch64-a3-16, GLM-4.7.yaml) / glm-4.7-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77551770635)
[查看 Job: single-node (main, qwen3-vl-235b-a22b-instruct-w8a8, linux-aarch64-a3-16, Qwen3-VL-235B-A22B-Inst... / qwen3-vl-235b-a22b-instruct-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77551770643)
[查看 Job: single-node (main, kimi-k2.5, linux-aarch64-a3-16, Kimi-K2.5.yaml) / kimi-k2.5](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77555730571)
[查看 Job: single-node (main, Qwen3.5-397B-A17B-w8a8-mtp, linux-aarch64-a3-16, Qwen3.5-397B-A17B-W8A8-mtp-A3... / Qwen3.5-397B-A17B-w8a8-mtp](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77557486289)
[查看 Job: single-node (main, Qwen3.5-27B-w8a8-A3, linux-aarch64-a3-2, Qwen3.5-27B-w8a8-A3.yaml) / Qwen3.5-27B-w8a8-A3](https://github.com/vllm-project/vllm-ascend/actions/runs/26338068996/job/77558364641)

**日志片段**:
```
2026-05-23T18:05:14.7083530Z [36;1m  "file_count": ${FILE_COUNT},[0m
2026-05-23T18:05:14.7083802Z [36;1m  "total_size": ${TOTAL_SIZE},[0m
2026-05-23T18:05:14.7084076Z [36;1m  "created_at": "${CREATED_AT}",[0m
2026-05-23T18:05:14.7084352Z [36;1m  "retention_days": 90,[0m
2026-05-23T18:05:14.7084615Z [36;1m  "workflow": "Nightly-A3",[0m
2026-05-23T18:05:14.7084871Z [36;1m  "job": "e2e",[0m
2026-05-23T18:05:14.7085216Z [36;1m  "sha": "a7a1e59143074e292110202eddacc8c3b757e861"[0m
2026-
```

**修复建议**:
- **优先**: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

### 16. Nightly-A2 (Run #26338064984)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984)
[查看 Job: doc-test / vLLM Ascend test (nightly-main)](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535099147)
[查看 Job: doc-test / vLLM Ascend test (nightly-main-openeuler)](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535099148)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-2, linux-aarch64-a2b3-1, ERNIE-4.5-21B-A3B-PT, I... / [
  "ERNIE-4.5-21B-A3B-PT",
  "InternVL3_5-8B-hf",
  "Molmo-7B-D-0924",
  "Llama-3.2-3B-Instruct",
  "llava-onevision-qwen2-0.5b-ov-hf"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954430)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-4, linux-aarch64-a2b3-4, Qwen3-Next-80B-A3B-Inst... / [
  "Qwen3-Next-80B-A3B-Instruct",
  "Qwen3-Omni-30B-A3B-Instruct",
  "Hunyuan-A13B-Instruct",
  "Mixtral-8x7B-Instruct-v0.1"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954445)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-1, linux-aarch64-a2b3-1, Qwen3-VL-8B-Instruct-W8... / [
  "Qwen3-VL-8B-Instruct-W8A8",
  "Qwen3-8B",
  "Qwen2-Audio-7B-Instruct",
  "Qwen3-8B-W8A8",
  "Qwen3-VL-8B-Instruct",
  "Minitron-8B-Base"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954450)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A2, linux-aarch64-a2b3-8, MiniMax-M2.5-w8a8-QuaRot-A2... / MiniMax-M2.5-w8a8-QuaRot-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954456)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-3, linux-aarch64-a2b3-2, Qwen3-30B-A3B, Qwen3-VL... / [
  "Qwen3-30B-A3B",
  "Qwen3-VL-30B-A3B-Instruct",
  "Qwen3-30B-A3B-W8A8"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954473)
[查看 Job: single-node (main, Qwen3.5-27B-w8a8-A2, linux-aarch64-a2b3-2, Qwen3.5-27B-w8a8-A2.yaml) / Qwen3.5-27B-w8a8-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954514)
[查看 Job: single-node (main, Qwen3.5-397B-A17B-w4a8-mtp, linux-aarch64-a2b3-8, Qwen3.5-397B-A17B-w4a8-mtp-A... / Qwen3.5-397B-A17B-w4a8-mtp](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954516)
[查看 Job: single-node (main, test_custom_op, linux-aarch64-a2b3-1, tests/e2e/nightly/single_node/ops/single... / test_custom_op](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77535954524)
[查看 Job: multi-node (main, multi-node-qwen3-235b-dp, Qwen3-235B-A22B-A2.yaml, 2) / Qwen3-235B-A22B-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26338064984/job/77539978848)

**日志片段**:
```
2026-05-23T16:57:18.8688479Z   File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/platform.py", line 151, in pre_register_and_update
2026-05-23T16:57:18.8689219Z     from vllm_ascend.quantization import AscendCompressedTensorsConfig, AscendModelSlimConfig  # noqa: F401
2026-05-23T16:57:18.8689738Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-23T16:57:18.8690158Z   File "<frozen importlib._bootstrap>", line 1229, in _handle_froml
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 17. vLLM Main Schedule Test (Run #26335885645)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26335885645)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26335885645/job/77529403704)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26335885645/job/77529403708)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26335885645/job/77529403720)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26335885645/job/77529403723)

**日志片段**:
```
2026-05-23T15:10:17.9132415Z   UV_NO_CACHE: 1
2026-05-23T15:10:17.9132682Z   UV_SYSTEM_PYTHON: 1
2026-05-23T15:10:17.9132902Z ##[endgroup]
2026-05-23T15:10:17.9211742Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-23T15:10:17.9212952Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-23T15:10:17.9213346Z ##[endgroup]
2026-05-23T15:10:18.4057965Z (node:1381) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 18. Release Code and Wheel (Run #26329744775)

- **状态**: 失败
- **根因分类**: 基础设施问题
- **置信度**: 低
- **具体问题**: 未能明确归类

**分析推理**: 未匹配已知失败模式，建议人工审查

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26329744775)
[查看 Job: build and release wheel (ubuntu-24.04, 3.11)](https://github.com/vllm-project/vllm-ascend/actions/runs/26329744775/job/77513668975)

**日志片段**:
```
2026-05-23T10:00:00.1287597Z   fetch-depth: 1
2026-05-23T10:00:00.1287969Z   fetch-tags: false
2026-05-23T10:00:00.1288358Z   show-progress: true
2026-05-23T10:00:00.1288749Z   lfs: false
2026-05-23T10:00:00.1289101Z   submodules: false
2026-05-23T10:00:00.1289492Z   set-safe-directory: true
2026-05-23T10:00:00.1290118Z ##[endgroup]
2026-05-23T10:00:00.2330022Z Syncing repository: vllm-project/vllm-ascend
2026-05-23T10:00:00.2331831Z ##[group]Getting Git version info
2026-05-23T10:00:00.2332795Z
```

**修复建议**:
- **优先**: 重新触发构建 (低成本)
- 重新触发构建 (低成本)

### 19. vLLM Main Schedule Test (Run #26329602920)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26329602920)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26329602920/job/77513284331)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26329602920/job/77513284332)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26329602920/job/77513284333)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26329602920/job/77513284336)

**日志片段**:
```
2026-05-23T10:30:17.9272466Z   UV_NO_CACHE: 1
2026-05-23T10:30:17.9272681Z   UV_SYSTEM_PYTHON: 1
2026-05-23T10:30:17.9273018Z ##[endgroup]
2026-05-23T10:30:17.9361691Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-23T10:30:17.9362602Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-23T10:30:17.9363046Z ##[endgroup]
2026-05-23T10:30:18.3988018Z (node:1459) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 20. vLLM Main Schedule Test (Run #26324769664)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26324769664)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26324769664/job/77500254545)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26324769664/job/77500254548)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26324769664/job/77500254549)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26324769664/job/77500254550)

**日志片段**:
```
2026-05-23T05:59:11.7925360Z   UV_NO_CACHE: 1
2026-05-23T05:59:11.7925563Z   UV_SYSTEM_PYTHON: 1
2026-05-23T05:59:11.7925725Z ##[endgroup]
2026-05-23T05:59:11.8069517Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-23T05:59:11.8070286Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-23T05:59:11.8070532Z ##[endgroup]
2026-05-23T05:59:12.2607716Z (node:1426) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 21. vLLM Main Schedule Test (Run #26311912901)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26311912901)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26311912901/job/77462422447)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26311912901/job/77462422452)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26311912901/job/77462422454)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26311912901/job/77462422477)

**日志片段**:
```
2026-05-22T21:17:47.7196079Z   UV_NO_CACHE: 1
2026-05-22T21:17:47.7196712Z   UV_SYSTEM_PYTHON: 1
2026-05-22T21:17:47.7197232Z ##[endgroup]
2026-05-22T21:17:47.7298528Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T21:17:47.7300208Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T21:17:47.7300847Z ##[endgroup]
2026-05-22T21:17:48.2190947Z (node:1361) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 22. Nightly-A3 (Run #26302347768)

- **状态**: 失败
- **根因分类**: 基础设施问题
- **置信度**: 中
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'single-node (main, deepseek-v3-2-w8a8, linux-aarch64-a3-16, DeepSeek-V3.2-W8A8.yaml) / deepseek-v3-2-w8a8' 中。 Runner: linux-aarch64-a3-16-l6dgl-runner-87t5n。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP, DeepSeek-V3_2-W8A8-EP.yaml, 4) / DeepSeek-V3_2-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77432034221)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP-aime2025, DeepSeek-V3_2-W8A8-EP-aime2025.yaml, 4) / DeepSeek-V3_2-W8A8-EP-aime2025.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77442806923)
[查看 Job: multi-node (main, multi-node-GLM5_1-W8A8-EP, GLM5_1-W8A8-EP.yaml, 4) / GLM5_1-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77448049992)
[查看 Job: double-node (main, multi-node-deepseek-r1-w8a8-longseq, DeepSeek-R1-W8A8-longseq.yaml, 2) / DeepSeek-R1-W8A8-longseq.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77452228181)
[查看 Job: double-node (main, multi-node-qwen3-dp, Qwen3-235B-A22B.yaml, 2) / Qwen3-235B-A22B.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77452228204)
[查看 Job: double-node (main, multi-node-deepseek-pd, DeepSeek-V3.yaml, 2) / DeepSeek-V3.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77452228233)
[查看 Job: double-node (main, multi-node-qwen3-dp-mooncake-layerwise, Qwen3-235B-A22B-Mooncake-Layerwise.yam... / Qwen3-235B-A22B-Mooncake-Layerwise.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77461752173)
[查看 Job: double-node (main, multi-node-kimi-k2-instruct-w8a8, Kimi-K2-Instruct-W8A8.yaml, 2) / Kimi-K2-Instruct-W8A8.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77468137742)
[查看 Job: double-node (main, multi-node-GLM-5.1-w8a8-A3, GLM5_1-W8A8-A3-dual-nodes.yaml, 2) / GLM5_1-W8A8-A3-dual-nodes.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77470571652)
[查看 Job: single-node (main, deepseek-v3-2-w8a8, linux-aarch64-a3-16, DeepSeek-V3.2-W8A8.yaml) / deepseek-v3-2-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77475510181)
[查看 Job: single-node (main, kimi-k2-thinking, linux-aarch64-a3-16, Kimi-K2-Thinking.yaml) / kimi-k2-thinking](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77475510202)
[查看 Job: single-node (main, deepseek-r1-0528-w8a8-prefix-cache, linux-aarch64-a3-16, Prefix-Cache-DeepSeek... / deepseek-r1-0528-w8a8-prefix-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77475510255)
[查看 Job: single-node (main, qwen3-vl-235b-a22b-instruct-w8a8, linux-aarch64-a3-16, Qwen3-VL-235B-A22B-Inst... / qwen3-vl-235b-a22b-instruct-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26302347768/job/77475510335)

**日志片段**:
```
2026-05-22T18:48:35.8883325Z [36;1m  "file_count": ${FILE_COUNT},[0m
2026-05-22T18:48:35.8883526Z [36;1m  "total_size": ${TOTAL_SIZE},[0m
2026-05-22T18:48:35.8883724Z [36;1m  "created_at": "${CREATED_AT}",[0m
2026-05-22T18:48:35.8883979Z [36;1m  "retention_days": 90,[0m
2026-05-22T18:48:35.8884181Z [36;1m  "workflow": "Nightly-A3",[0m
2026-05-22T18:48:35.8884367Z [36;1m  "job": "e2e",[0m
2026-05-22T18:48:35.8884575Z [36;1m  "sha": "7e817f291bc23935d66440b3576a66c3933ef921"[0m
2026-
```

**修复建议**:
- **优先**: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

### 23. Nightly-A2 (Run #26302345284)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284)
[查看 Job: doc-test / vLLM Ascend test (nightly-main-openeuler)](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77430419919)
[查看 Job: doc-test / vLLM Ascend test (nightly-main)](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77430419942)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-2, linux-aarch64-a2b3-1, ERNIE-4.5-21B-A3B-PT, I... / [
  "ERNIE-4.5-21B-A3B-PT",
  "InternVL3_5-8B-hf",
  "Molmo-7B-D-0924",
  "Llama-3.2-3B-Instruct",
  "llava-onevision-qwen2-0.5b-ov-hf"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349466)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-3, linux-aarch64-a2b3-2, Qwen3-30B-A3B, Qwen3-VL... / [
  "Qwen3-30B-A3B",
  "Qwen3-VL-30B-A3B-Instruct",
  "Qwen3-30B-A3B-W8A8"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349475)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-4, linux-aarch64-a2b3-4, Qwen3-Next-80B-A3B-Inst... / [
  "Qwen3-Next-80B-A3B-Instruct",
  "Qwen3-Omni-30B-A3B-Instruct",
  "Hunyuan-A13B-Instruct",
  "Mixtral-8x7B-Instruct-v0.1"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349503)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-1, linux-aarch64-a2b3-1, Qwen3-VL-8B-Instruct-W8... / [
  "Qwen3-VL-8B-Instruct-W8A8",
  "Qwen3-8B",
  "Qwen2-Audio-7B-Instruct",
  "Qwen3-8B-W8A8",
  "Qwen3-VL-8B-Instruct",
  "Minitron-8B-Base"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349549)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A2, linux-aarch64-a2b3-8, MiniMax-M2.5-w8a8-QuaRot-A2... / MiniMax-M2.5-w8a8-QuaRot-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349579)
[查看 Job: single-node (main, test_custom_op, linux-aarch64-a2b3-1, tests/e2e/nightly/single_node/ops/single... / test_custom_op](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349628)
[查看 Job: single-node (main, Qwen3.5-397B-A17B-w4a8-mtp, linux-aarch64-a2b3-8, Qwen3.5-397B-A17B-w4a8-mtp-A... / Qwen3.5-397B-A17B-w4a8-mtp](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349635)
[查看 Job: single-node (main, Qwen3.5-27B-w8a8-A2, linux-aarch64-a2b3-2, Qwen3.5-27B-w8a8-A2.yaml) / Qwen3.5-27B-w8a8-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77432349646)
[查看 Job: multi-node (main, multi-node-qwen3-235b-dp, Qwen3-235B-A22B-A2.yaml, 2) / Qwen3-235B-A22B-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26302345284/job/77444467978)

**日志片段**:
```
2026-05-22T18:06:02.1252239Z   File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/platform.py", line 151, in pre_register_and_update
2026-05-22T18:06:02.1253120Z     from vllm_ascend.quantization import AscendCompressedTensorsConfig, AscendModelSlimConfig  # noqa: F401
2026-05-22T18:06:02.1253672Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-22T18:06:02.1254065Z   File "<frozen importlib._bootstrap>", line 1229, in _handle_froml
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 24. vLLM Main Schedule Test (Run #26299256650)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26299256650)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26299256650/job/77419892425)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26299256650/job/77419892428)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26299256650/job/77419892456)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26299256650/job/77419892544)

**日志片段**:
```
2026-05-22T17:35:08.3574646Z   UV_NO_CACHE: 1
2026-05-22T17:35:08.3575451Z   UV_SYSTEM_PYTHON: 1
2026-05-22T17:35:08.3575936Z ##[endgroup]
2026-05-22T17:35:08.3715944Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T17:35:08.3717134Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T17:35:08.3717506Z ##[endgroup]
2026-05-22T17:35:08.8600945Z (node:1296) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 25. vLLM Main Schedule Test (Run #26283288369)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26283288369)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26283288369/job/77364544126)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26283288369/job/77364544137)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26283288369/job/77364544147)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26283288369/job/77364544177)

**日志片段**:
```
2026-05-22T11:03:07.5945801Z   UV_NO_CACHE: 1
2026-05-22T11:03:07.5946040Z   UV_SYSTEM_PYTHON: 1
2026-05-22T11:03:07.5946237Z ##[endgroup]
2026-05-22T11:03:07.6018506Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T11:03:07.6019669Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T11:03:07.6019966Z ##[endgroup]
2026-05-22T11:03:08.0776760Z (node:1349) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 26. Release Code and Wheel (Run #26271541708)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26271541708)
[查看 Job: build and release wheel (A3) (ubuntu-24.04, 3.11)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271541708/job/77325925753)
[查看 Job: build and release wheel (ubuntu-24.04, 3.11)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271541708/job/77325925785)
[查看 Job: build and release wheel (310P) (ubuntu-24.04, 3.11)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271541708/job/77325925793)

**日志片段**:
```
2026-05-22T06:12:35.5413116Z 
2026-05-22T06:12:35.5413581Z #8 [4/6] COPY . /workspace/vllm-ascend/
2026-05-22T06:12:36.1237246Z #8 DONE 0.7s
2026-05-22T06:12:36.2749193Z 
2026-05-22T06:12:36.2750578Z #9 [5/6] RUN python3 -m pip install -r vllm-ascend/requirements.txt --extra-index https://download.pytorch.org/whl/cpu/ &&     python3 -m pip install twine attrs psutil
2026-05-22T06:12:36.7260799Z #9 0.602 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cpu/
2026-05-22
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 27. vLLM Main Schedule Test (Run #26271314173)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189839)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189849)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189867)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26271314173/job/77325189883)

**日志片段**:
```
2026-05-22T06:18:49.9029998Z   UV_HTTP_TIMEOUT: 120
2026-05-22T06:18:49.9030270Z   UV_NO_CACHE: 1
2026-05-22T06:18:49.9030456Z   UV_SYSTEM_PYTHON: 1
2026-05-22T06:18:49.9030664Z ##[endgroup]
2026-05-22T06:18:49.9127344Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-22T06:18:49.9128239Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-22T06:18:49.9128535Z ##[endgroup]
2026-05-22T06:18:50.3643904Z (node:1508) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usab
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 28. Image build lint (Run #26254056723)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26254056723)
[查看 Job: vllm-ascend lint image build](https://github.com/vllm-project/vllm-ascend/actions/runs/26254056723/job/77272297499)

**日志片段**:
```
2026-05-21T21:28:23.2009520Z #11 2.904 ERROR: Ignored the following versions that require a different python version: 1.6.2 Requires-Python >=3.7,<3.10; 1.6.3 Requires-Python >=3.7,<3.10; 1.7.0 Requires-Python >=3.7,<3.10; 1.7.1 Requires-Python >=3.7,<3.10; 1.7.2 Requires-Python >=3.7,<3.11; 1.7.3 Requires-Python >=3.7,<3.11; 1.8.0 Requires-Python >=3.8,<3.11; 1.8.0rc1 Requires-Python >=3.8,<3.11; 1.8.0rc2 Requires-Python >=3.8,<3.11; 1.8.0rc3 Requires-Python >=3.8,<3.11; 1.8.0rc4 Requires-Pytho
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 29. vLLM Main Schedule Test (Run #26253935630)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26253935630)
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

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 30. Nightly-A2 (Run #26243068887)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26243068887)
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

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 31. Nightly-A3 (Run #26243065104)

- **状态**: 失败
- **根因分类**: 基础设施问题
- **置信度**: 中
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'single-node (main, deepseek-r1-0528-w8a8-prefix-cache, linux-aarch64-a3-16, Prefix-Cache-DeepSeek... / deepseek-r1-0528-w8a8-prefix-cache' 中。 Runner: linux-aarch64-a3-16-l6dgl-runner-6q6xv。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP, DeepSeek-V3_2-W8A8-EP.yaml, 4) / DeepSeek-V3_2-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77236255641)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP-aime2025, DeepSeek-V3_2-W8A8-EP-aime2025.yaml, 4) / DeepSeek-V3_2-W8A8-EP-aime2025.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77247531120)
[查看 Job: double-node (main, multi-node-deepseek-r1-w8a8-longseq, DeepSeek-R1-W8A8-longseq.yaml, 2) / DeepSeek-R1-W8A8-longseq.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77259937866)
[查看 Job: double-node (main, multi-node-qwen3-dp, Qwen3-235B-A22B.yaml, 2) / Qwen3-235B-A22B.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77259937880)
[查看 Job: double-node (main, multi-node-qwenw8a8-2node-eplb, Qwen3-235B-W8A8-EPLB.yaml, 2) / Qwen3-235B-W8A8-EPLB.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77268166242)
[查看 Job: double-node (main, multi-node-qwen3-dp-mooncake-layerwise, Qwen3-235B-A22B-Mooncake-Layerwise.yam... / Qwen3-235B-A22B-Mooncake-Layerwise.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77273586839)
[查看 Job: double-node (main, multi-node-kimi-k2-instruct-w8a8, Kimi-K2-Instruct-W8A8.yaml, 2) / Kimi-K2-Instruct-W8A8.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77281306893)
[查看 Job: double-node (main, multi-node-GLM-5.1-w8a8-A3, GLM5_1-W8A8-A3-dual-nodes.yaml, 2) / GLM5_1-W8A8-A3-dual-nodes.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77284015858)
[查看 Job: single-node (main, deepseek-r1-0528-w8a8-prefix-cache, linux-aarch64-a3-16, Prefix-Cache-DeepSeek... / deepseek-r1-0528-w8a8-prefix-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77288216757)
[查看 Job: single-node (main, deepseek-v3-2-w8a8, linux-aarch64-a3-16, DeepSeek-V3.2-W8A8.yaml) / deepseek-v3-2-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77288216780)
[查看 Job: single-node (main, deepseek-r1-w8a8-hbm, linux-aarch64-a3-16, DeepSeek-R1-W8A8-HBM.yaml) / deepseek-r1-w8a8-hbm](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77288216825)
[查看 Job: single-node (main, deepseek-r1-0528-w8a8, linux-aarch64-a3-16, DeepSeek-R1-0528-W8A8.yaml) / deepseek-r1-0528-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77288216852)
[查看 Job: single-node (main, glm-5-w4a8, linux-aarch64-a3-16, GLM-5.yaml) / glm-5-w4a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26243065104/job/77290014146)

**日志片段**:
```
2026-05-21T18:59:42.6009723Z [36;1m  "file_count": ${FILE_COUNT},[0m
2026-05-21T18:59:42.6010149Z [36;1m  "total_size": ${TOTAL_SIZE},[0m
2026-05-21T18:59:42.6010433Z [36;1m  "created_at": "${CREATED_AT}",[0m
2026-05-21T18:59:42.6010705Z [36;1m  "retention_days": 90,[0m
2026-05-21T18:59:42.6010970Z [36;1m  "workflow": "Nightly-A3",[0m
2026-05-21T18:59:42.6011241Z [36;1m  "job": "e2e",[0m
2026-05-21T18:59:42.6011536Z [36;1m  "sha": "68a4db5554475d8e413f13d84016b86f5d2c18b7"[0m
2026-
```

**修复建议**:
- **优先**: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

### 32. vLLM Main Schedule Test (Run #26239472511)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26239472511)
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

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 33. Release Code and Wheel (Run #26223112224)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26223112224)
[查看 Job: build and release wheel (310P) (ubuntu-24.04-arm, 3.11)](https://github.com/vllm-project/vllm-ascend/actions/runs/26223112224/job/77162969097)
[查看 Job: build and release wheel (ubuntu-24.04, 3.10)](https://github.com/vllm-project/vllm-ascend/actions/runs/26223112224/job/77162969098)
[查看 Job: build and release wheel (A3) (ubuntu-24.04-arm, 3.10)](https://github.com/vllm-project/vllm-ascend/actions/runs/26223112224/job/77162969166)

**日志片段**:
```
2026-05-21T11:33:40.7590454Z 
2026-05-21T11:33:40.7590546Z #8 [4/6] COPY . /workspace/vllm-ascend/
2026-05-21T11:33:41.8887259Z #8 DONE 1.3s
2026-05-21T11:33:42.0428591Z 
2026-05-21T11:33:42.0429783Z #9 [5/6] RUN python3 -m pip install -r vllm-ascend/requirements.txt --extra-index https://download.pytorch.org/whl/cpu/ &&     python3 -m pip install twine attrs psutil
2026-05-21T11:33:42.6404503Z #9 0.748 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cpu/
2026-05-21
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 34. vLLM Main Schedule Test (Run #26222654971)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26222654971)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26222654971/job/77161372566)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26222654971/job/77161372593)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26222654971/job/77161372597)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26222654971/job/77161372631)

**日志片段**:
```
2026-05-21T11:40:36.6378862Z   UV_NO_CACHE: 1
2026-05-21T11:40:36.6379024Z   UV_SYSTEM_PYTHON: 1
2026-05-21T11:40:36.6379270Z ##[endgroup]
2026-05-21T11:40:36.6463330Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T11:40:36.6464133Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T11:40:36.6464384Z ##[endgroup]
2026-05-21T11:40:37.1072587Z (node:1505) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 35. Release Code and Wheel (Run #26208851000)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26208851000)
[查看 Job: build and release wheel (ubuntu-24.04, 3.10)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208851000/job/77114682200)
[查看 Job: build and release wheel (310P) (ubuntu-24.04, 3.10)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208851000/job/77114682208)
[查看 Job: build and release wheel (A3) (ubuntu-24.04, 3.10)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208851000/job/77114682222)

**日志片段**:
```
2026-05-21T06:16:49.2278134Z 
2026-05-21T06:16:49.2278318Z #8 [4/6] COPY . /workspace/vllm-ascend/
2026-05-21T06:16:49.9295800Z #8 DONE 0.9s
2026-05-21T06:16:50.0806530Z 
2026-05-21T06:16:50.0807911Z #9 [5/6] RUN python3 -m pip install -r vllm-ascend/requirements.txt --extra-index https://download.pytorch.org/whl/cpu/ &&     python3 -m pip install twine attrs psutil
2026-05-21T06:16:50.5750275Z #9 0.645 Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cpu/
2026-05-21
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 36. vLLM Main Schedule Test (Run #26208639745)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26208639745)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208639745/job/77113990018)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208639745/job/77113990020)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208639745/job/77113990034)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26208639745/job/77113990040)

**日志片段**:
```
2026-05-21T06:21:20.3234345Z   UV_NO_CACHE: 1
2026-05-21T06:21:20.3234523Z   UV_SYSTEM_PYTHON: 1
2026-05-21T06:21:20.3234711Z ##[endgroup]
2026-05-21T06:21:20.3324127Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T06:21:20.3325078Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T06:21:20.3325363Z ##[endgroup]
2026-05-21T06:21:20.8006822Z (node:1573) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 37. Image build lint (Run #26192072868)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26192072868)
[查看 Job: vllm-ascend lint image build](https://github.com/vllm-project/vllm-ascend/actions/runs/26192072868/job/77062715314)

**日志片段**:
```
2026-05-20T21:53:51.2340626Z #11 5.373 ERROR: Ignored the following versions that require a different python version: 1.6.2 Requires-Python >=3.7,<3.10; 1.6.3 Requires-Python >=3.7,<3.10; 1.7.0 Requires-Python >=3.7,<3.10; 1.7.1 Requires-Python >=3.7,<3.10; 1.7.2 Requires-Python >=3.7,<3.11; 1.7.3 Requires-Python >=3.7,<3.11; 1.8.0 Requires-Python >=3.8,<3.11; 1.8.0rc1 Requires-Python >=3.8,<3.11; 1.8.0rc2 Requires-Python >=3.8,<3.11; 1.8.0rc3 Requires-Python >=3.8,<3.11; 1.8.0rc4 Requires-Pytho
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 38. vLLM Main Schedule Test (Run #26191916523)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26191916523)
[查看 Job: e2e-test / multicard-4-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26191916523/job/77062180150)
[查看 Job: e2e-test / multicard-2-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26191916523/job/77062180159)
[查看 Job: e2e-test / singlecard-full (1)](https://github.com/vllm-project/vllm-ascend/actions/runs/26191916523/job/77062180167)
[查看 Job: e2e-test / singlecard-full (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26191916523/job/77062180171)

**日志片段**:
```
2026-05-21T02:39:39.3750969Z   UV_NO_CACHE: 1
2026-05-21T02:39:39.3751234Z   UV_SYSTEM_PYTHON: 1
2026-05-21T02:39:39.3751491Z ##[endgroup]
2026-05-21T02:39:39.3834763Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T02:39:39.3835867Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T02:39:39.3836223Z ##[endgroup]
2026-05-21T02:39:39.8391426Z (node:1541) [DEP0005] DeprecationWarning: Buffer() is deprecated due to security and usability issues. Please use the Buffer.alloc(), Buffer.
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 39. Nightly-A2 (Run #26180770916)

- **状态**: 失败
- **根因分类**: 代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916)
[查看 Job: doc-test / vLLM Ascend test (nightly-main)](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77022929683)
[查看 Job: doc-test / vLLM Ascend test (nightly-main-openeuler)](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77022929718)
[查看 Job: single-node (main, test_custom_op, linux-aarch64-a2b3-1, tests/e2e/nightly/single_node/ops/single... / test_custom_op](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77093806507)
[查看 Job: single-node (main, MiniMax-M2.5-w8a8-QuaRot-A2, linux-aarch64-a2b3-8, MiniMax-M2.5-w8a8-QuaRot-A2... / MiniMax-M2.5-w8a8-QuaRot-A2](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77093806514)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-3, linux-aarch64-a2b3-2, Qwen3-30B-A3B, Qwen3-VL... / [
  "Qwen3-30B-A3B",
  "Qwen3-VL-30B-A3B-Instruct",
  "Qwen3-30B-A3B-W8A8"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77093881236)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-1, linux-aarch64-a2b3-1, Qwen3-VL-8B-Instruct-W8... / [
  "Qwen3-VL-8B-Instruct-W8A8",
  "Qwen3-8B",
  "Qwen2-Audio-7B-Instruct",
  "Qwen3-8B-W8A8",
  "Qwen3-VL-8B-Instruct",
  "Minitron-8B-Base"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77093881260)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-4, linux-aarch64-a2b3-4, Qwen3-Next-80B-A3B-Inst... / [
  "Qwen3-Next-80B-A3B-Instruct",
  "Qwen3-Omni-30B-A3B-Instruct",
  "Hunyuan-A13B-Instruct",
  "Mixtral-8x7B-Instruct-v0.1"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77093881273)
[查看 Job: single-node-accuracy-tests (main, accuracy-group-2, linux-aarch64-a2b3-1, ERNIE-4.5-21B-A3B-PT, I... / [
  "ERNIE-4.5-21B-A3B-PT",
  "InternVL3_5-8B-hf",
  "Molmo-7B-D-0924",
  "Llama-3.2-3B-Instruct",
  "llava-onevision-qwen2-0.5b-ov-hf"
] accuracy test](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77093881293)
[查看 Job: multi-node (main, multi-node-deepseek-dp, DeepSeek-R1-W8A8-A2.yaml, 2) / DeepSeek-R1-W8A8-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77117953745)
[查看 Job: multi-node (main, multi-node-Kimi-K2.5-W4A8-A2, Kimi-K2_5-W4A8-A2-dual-nodes.yaml, 2) / Kimi-K2_5-W4A8-A2-dual-nodes.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77117953749)
[查看 Job: multi-node (main, multi-node-qwen3-235b-dp, Qwen3-235B-A22B-A2.yaml, 2) / Qwen3-235B-A22B-A2.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180770916/job/77117953754)

**日志片段**:
```
2026-05-21T02:49:59.7381843Z   File "/tmp/vllm_venv/lib/python3.11/site-packages/vllm_ascend/platform.py", line 151, in pre_register_and_update
2026-05-21T02:49:59.7383605Z     from vllm_ascend.quantization import AscendCompressedTensorsConfig, AscendModelSlimConfig  # noqa: F401
2026-05-21T02:49:59.7386252Z     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-05-21T02:49:59.7387418Z   File "<frozen importlib._bootstrap>", line 1229, in _handle_froml
```

**修复建议**:
- **优先**: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 40. Nightly-A3 (Run #26180748860)

- **状态**: 失败
- **根因分类**: 基础设施问题
- **置信度**: 中
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'single-node (main, deepseek-r1-0528-w8a8-prefix-cache, linux-aarch64-a3-16, Prefix-Cache-DeepSeek... / deepseek-r1-0528-w8a8-prefix-cache' 中。 Runner: linux-aarch64-a3-16-l6dgl-runner-rq7js。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP, DeepSeek-V3_2-W8A8-EP.yaml, 4) / DeepSeek-V3_2-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77093358629)
[查看 Job: multi-node (main, multi-node-deepseek-v3.2-W8A8-EP-aime2025, DeepSeek-V3_2-W8A8-EP-aime2025.yaml, 4) / DeepSeek-V3_2-W8A8-EP-aime2025.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77095463134)
[查看 Job: multi-node (main, multi-node-GLM5_1-W8A8-EP, GLM5_1-W8A8-EP.yaml, 4) / GLM5_1-W8A8-EP.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77097582790)
[查看 Job: double-node (main, multi-node-deepseek-pd, DeepSeek-V3.yaml, 2) / DeepSeek-V3.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77099709237)
[查看 Job: double-node (main, multi-node-deepseek-r1-w8a8-longseq, DeepSeek-R1-W8A8-longseq.yaml, 2) / DeepSeek-R1-W8A8-longseq.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77099709251)
[查看 Job: double-node (main, multi-node-qwen3-dp, Qwen3-235B-A22B.yaml, 2) / Qwen3-235B-A22B.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77099709266)
[查看 Job: double-node (main, multi-node-qwenw8a8-2node, Qwen3-235B-W8A8.yaml, 2) / Qwen3-235B-W8A8.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77101674866)
[查看 Job: double-node (main, multi-node-qwenw8a8-2node-eplb, Qwen3-235B-W8A8-EPLB.yaml, 2) / Qwen3-235B-W8A8-EPLB.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77101757824)
[查看 Job: double-node (main, multi-node-dpsk3.2-2node, DeepSeek-V3_2-W8A8-A3-dual-nodes.yaml, 2) / DeepSeek-V3_2-W8A8-A3-dual-nodes.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77101775571)
[查看 Job: double-node (main, multi-node-qwen3-dp-mooncake-layerwise, Qwen3-235B-A22B-Mooncake-Layerwise.yam... / Qwen3-235B-A22B-Mooncake-Layerwise.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77103719006)
[查看 Job: double-node (main, multi-node-qwenw8a8-2node-longseq, Qwen3-235B-W8A8-longseq.yaml, 2) / Qwen3-235B-W8A8-longseq.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77103787976)
[查看 Job: double-node (main, multi-node-qwen-disagg-pd, Qwen3-235B-disagg-pd.yaml, 2) / Qwen3-235B-disagg-pd.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77103804896)
[查看 Job: double-node (main, multi-node-qwen-vl-disagg-pd, Qwen3-VL-235B-disagg-pd.yaml, 2) / Qwen3-VL-235B-disagg-pd.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77105786077)
[查看 Job: double-node (main, multi-node-kimi-k2-instruct-w8a8, Kimi-K2-Instruct-W8A8.yaml, 2) / Kimi-K2-Instruct-W8A8.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77105934078)
[查看 Job: double-node (main, multi-node-deepseek-v3.1, DeepSeek-V3.1-BF16.yaml, 2) / DeepSeek-V3.1-BF16.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77106004558)
[查看 Job: double-node (main, multi-node-glm4.7-w8a8c8-layerwise, GLM-4.7-W8A8C8-Mooncake-Layerwise.yaml, 2) / GLM-4.7-W8A8C8-Mooncake-Layerwise.yaml](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77107934162)
[查看 Job: single-node (main, deepseek-r1-0528-w8a8-prefix-cache, linux-aarch64-a3-16, Prefix-Cache-DeepSeek... / deepseek-r1-0528-w8a8-prefix-cache](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77110190708)
[查看 Job: single-node (main, mtpx-deepseek-r1-0528-w8a8, linux-aarch64-a3-16, MTPX-DeepSeek-R1-0528-W8A8.yaml) / mtpx-deepseek-r1-0528-w8a8](https://github.com/vllm-project/vllm-ascend/actions/runs/26180748860/job/77110190747)

**日志片段**:
```
2026-05-21T02:52:01.0908429Z [36;1m  "file_count": ${FILE_COUNT},[0m
2026-05-21T02:52:01.0908633Z [36;1m  "total_size": ${TOTAL_SIZE},[0m
2026-05-21T02:52:01.0908849Z [36;1m  "created_at": "${CREATED_AT}",[0m
2026-05-21T02:52:01.0909065Z [36;1m  "retention_days": 90,[0m
2026-05-21T02:52:01.0909271Z [36;1m  "workflow": "Nightly-A3",[0m
2026-05-21T02:52:01.0909581Z [36;1m  "job": "e2e",[0m
2026-05-21T02:52:01.0909804Z [36;1m  "sha": "cdfd642a826b84414dda5e812e349001e3015bb4"[0m
2026-
```

**修复建议**:
- **优先**: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

## 修复建议

### 优先修复（代码问题）

- **vLLM Main Schedule Test (#26419606840)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26412181441)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26409927217)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26398978835)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26386592221)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26372402659)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26366938206)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26364582559)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Docs link check (#26362038335)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-upstream (#26358050036)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26358021964)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26353449009)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26343078965)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26338064984)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26335885645)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26329602920)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26324769664)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26311912901)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26302345284)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26299256650)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26283288369)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Release Code and Wheel (#26271541708)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26271314173)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Image build lint (#26254056723)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26253935630)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26243068887)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26239472511)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Release Code and Wheel (#26223112224)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26222654971)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Release Code and Wheel (#26208851000)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26208639745)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Image build lint (#26192072868)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **vLLM Main Schedule Test (#26191916523)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **Nightly-A2 (#26180770916)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

### 建议关注（基础设施问题）

- **Nightly-A3 (#26366927091)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复
- **Nightly-A3 (#26338068996)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复
- **Release Code and Wheel (#26329744775)**: 重新触发构建 (低成本) - 基础设施问题通常会自动恢复
- **Nightly-A3 (#26302347768)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复
- **Nightly-A3 (#26243065104)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复
- **Nightly-A3 (#26180748860)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复






---
报告生成时间: 2026-05-26T03:12:15.266166+00:00
