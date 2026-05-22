---
report_id: 1e3e987d
pr_number: 9433
group_key: pr-9433
generated_at: 2026-05-22T03:50:13.211568+00:00
overall_classification: code
total_failed_workflows: 5
category_counts:
  code: 4
  infrastructure: 1
  interference: 0
---

# 构建失败报告: PR #9433

## 概要

PR #9433 触发了 5 个 workflow，均失败。

- **代码问题**: 4 次
- **基础设施问题**: 1 次

| # | Workflow | 根因分类 | 置信度 | 具体问题 |
|---|---|---|---|---|
| 1 | E2E-Light (#26263731339) | 基础设施问题 | 中 | K8s内部服务失败 |
| 2 | E2E-Light (#26230463344) | PR代码问题 | 高 | 编译错误 |
| 3 | E2E-Light (#26228842405) | PR代码问题 | 中 | 编译错误 |
| 4 | E2E-Light (#26227809577) | PR代码问题 | 中 | 编译错误 |
| 5 | E2E-Light (#26227255860) | PR代码问题 | 中 | 编译错误 |


## Workflow 详细分析
### 1. E2E-Light (Run #26263731339)

- **根因分类**: 基础设施问题
- **置信度**: 中
- **具体问题**: K8s内部服务失败

**分析推理**: 检测到基础设施问题: cache_service, cache_service。 问题出现在 job 'e2e-light (v0.20.2) / singlecard-light (0)' 中。 Runner: linux-aarch64-a2b3-1-zsnst-runner-x25jf。 不是PR代码问题，建议检查基础设施状态。

**匹配模式**:
- cache_service: `cache-service\.nginx-pypi-cache`
- cache_service: `svc\.cluster\.local`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26263731339)
[查看 Job: e2e-light (v0.20.2) / singlecard-light (0)](https://github.com/vllm-project/vllm-ascend/actions/runs/26263731339/job/77302942586)

**日志片段**:
```
2026-05-22T02:00:50.6562100Z [36;1mpython3 .github/workflows/scripts/ci_log_summary.py \[0m
2026-05-22T02:00:50.6562445Z [36;1m  --step-name "Run singlecard-light test" \[0m
2026-05-22T02:00:50.6562786Z [36;1m  --log-file /tmp/e2e-singlecard-light-part0.log \[0m
2026-05-22T02:00:50.6563097Z [36;1m  --output "$GITHUB_STEP_SUMMARY"[0m
2026-05-22T02:00:50.6563389Z shell: sh -e {0}
2026-05-22T02:00:50.6563861Z env:
2026-05-22T02:00:50.6564210Z   UV_INDEX_URL: http://cache-service.nginx-pypi-
```

**建议**:
- 优先: 等待服务恢复 (低成本)
- 等待服务恢复 (低成本)

### 2. E2E-Light (Run #26230463344)

- **根因分类**: PR代码问题
- **置信度**: 高
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9433 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26230463344)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26230463344/job/77189225435)

**日志片段**:
```
2026-05-21T14:00:23.2484914Z [36;1m  tools/mypy.sh 1 "$python_version"[0m
2026-05-21T14:00:23.2485182Z [36;1m  echo "============================"[0m
2026-05-21T14:00:23.2485407Z [36;1mdone[0m
2026-05-21T14:00:23.2485666Z shell: sh -e {0}
2026-05-21T14:00:23.2485834Z ##[endgroup]
2026-05-21T14:00:23.2595920Z ##[group]Run '/home/runner/k8s/index.js'
2026-05-21T14:00:23.2596730Z shell: /home/runner/externals/node20/bin/node {0}
2026-05-21T14:00:23.2597056Z ##[endgroup]
2026-05-21T14:00:23.71
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 3. E2E-Light (Run #26228842405)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9433 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26228842405)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26228842405/job/77183804193)

**日志片段**:
```
2026-05-21T13:31:06.9744526Z                          pertoken_scale=kv_s_dummy,[m
2026-05-21T13:31:06.9745019Z [31m-                        output_dtype=hidden_states.dtype)[m
2026-05-21T13:31:06.9745570Z [32m+[m[32m                        output_dtype=hidden_states.dtype,[m
2026-05-21T13:31:06.9745974Z [32m+[m[32m                    )[m
2026-05-21T13:31:06.9746261Z                  else:[m
2026-05-21T13:31:06.9746596Z                      _ = impl.cv_wkv.quantize(dummy)[m
2026-05-
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 4. E2E-Light (Run #26227809577)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9433 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26227809577)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26227809577/job/77179620346)

**日志片段**:
```
2026-05-21T13:08:28.0918929Z                          pertoken_scale=kv_s_dummy,[m
2026-05-21T13:08:28.0919409Z [31m-                        output_dtype=hidden_states.dtype)[m
2026-05-21T13:08:28.0919954Z [32m+[m[32m                        output_dtype=hidden_states.dtype,[m
2026-05-21T13:08:28.0920368Z [32m+[m[32m                    )[m
2026-05-21T13:08:28.0920647Z                  else:[m
2026-05-21T13:08:28.0921000Z                      _ = impl.cv_wkv.quantize(dummy)[m
2026-05-
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

### 5. E2E-Light (Run #26227255860)

- **根因分类**: PR代码问题
- **置信度**: 中
- **具体问题**: 编译错误

**分析推理**: 检测到代码问题模式: compilation。 问题出现在 PR #9433 代码中。 建议检查 PR 的代码修改和测试用例。

**匹配模式**:
- compilation: `error:\s+`

[查看 Workflow Run](https://github.com/vllm-project/vllm-ascend/actions/runs/26227255860)
[查看 Job: lint / pre-commit](https://github.com/vllm-project/vllm-ascend/actions/runs/26227255860/job/77177636157)

**日志片段**:
```
2026-05-21T12:57:58.7734005Z                          pertoken_scale=kv_s_dummy,[m
2026-05-21T12:57:58.7734595Z [31m-                        output_dtype=hidden_states.dtype)[m
2026-05-21T12:57:58.7735240Z [32m+[m[32m                        output_dtype=hidden_states.dtype,[m
2026-05-21T12:57:58.7735786Z [32m+[m[32m                    )[m
2026-05-21T12:57:58.7736151Z                  else:[m
2026-05-21T12:57:58.7736585Z                      _ = impl.cv_wkv.quantize(dummy)[m
2026-05-
```

**建议**:
- 优先: 检查编译错误位置 (低成本)
- 检查编译错误位置 (低成本)
- 修复编译问题 (中等成本)

## 修复建议

**整体根因**: PR代码问题

### 优先建议

- **E2E-Light (#26263731339)**: 等待服务恢复 (低成本) - cache-service.nginx-pypi-cache 通常会自动恢复
- **E2E-Light (#26230463344)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26228842405)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26227809577)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行
- **E2E-Light (#26227255860)**: 检查编译错误位置 (低成本) - 查看 CMake 或 clang 报错的具体文件和行

---
报告生成时间: 2026-05-22T03:50:13.211622+00:00
