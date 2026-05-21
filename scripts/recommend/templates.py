"""修复建议模板 - 标准化的修复指令模板。"""


def get_code_fix_template(issue_type: str) -> dict:
    """获取代码问题修复模板。"""
    
    templates = {
        "test_assertion": {
            "title": "测试断言失败修复",
            "steps": [
                {
                    "action": "定位失败测试",
                    "detail": "在日志中找到具体的测试函数名和断言错误"
                },
                {
                    "action": "分析失败原因",
                    "detail": "确认测试失败是否因 PR 代码变更导致"
                },
                {
                    "action": "修复代码或测试",
                    "detail": "根据原因修改相应代码或更新测试预期"
                }
            ]
        },
        "compilation": {
            "title": "编译错误修复",
            "steps": [
                {
                    "action": "检查编译错误",
                    "detail": "查看 CMake 或 clang 的具体错误信息"
                },
                {
                    "action": "修复语法问题",
                    "detail": "修复代码中的语法或类型错误"
                },
                {
                    "action": "重新编译",
                    "detail": "确保修复后编译通过"
                }
            ]
        },
        "import_error": {
            "title": "导入错误修复",
            "steps": [
                {
                    "action": "确认依赖",
                    "detail": "检查缺失的模块或包"
                },
                {
                    "action": "添加依赖",
                    "detail": "在 requirements.txt 中添加缺失依赖"
                },
                {
                    "action": "或修复导入路径",
                    "detail": "更新导入语句使用正确路径"
                }
            ]
        },
        "vllm_api": {
            "title": "vLLM API 兼容性修复",
            "steps": [
                {
                    "action": "检查 vLLM 版本",
                    "detail": "确认使用的 vLLM 版本和 API 变化"
                },
                {
                    "action": "适配新 API",
                    "detail": "根据 vLLM 最新 API 更新代码"
                },
                {
                    "action": "添加兼容处理",
                    "detail": "如需支持多版本，添加兼容性处理"
                }
            ]
        }
    }
    
    return templates.get(issue_type, templates["test_assertion"])


def get_infra_fix_template(issue_type: str) -> dict:
    """获取基础设施问题修复模板。"""
    
    templates = {
        "cache_service": {
            "title": "K8s cache-service 故障处理",
            "steps": [
                {
                    "action": "等待服务恢复",
                    "detail": "cache-service 通常会自动恢复，等待 10-30 分钟"
                },
                {
                    "action": "重新触发构建",
                    "detail": "服务恢复后重新运行 workflow"
                },
                {
                    "action": "联系运维",
                    "detail": "如果持续失败，联系基础设施团队"
                }
            ]
        },
        "runner": {
            "title": "Runner 不可用处理",
            "steps": [
                {
                    "action": "等待 Runner",
                    "detail": "等待 Runner 恢复在线状态"
                },
                {
                    "action": "重新触发",
                    "detail": "Runner 可用后重新运行 workflow"
                },
                {
                    "action": "切换 Runner",
                    "detail": "如特定 Runner 持续不可用，尝试其他类型"
                }
            ]
        },
        "npu": {
            "title": "NPU 硬件问题处理",
            "steps": [
                {
                    "action": "检查 NPU 状态",
                    "detail": "运行 npu-smi info 检查 NPU 状态"
                },
                {
                    "action": "联系运维",
                    "detail": "硬件问题需要运维团队介入"
                },
                {
                    "action": "切换 Runner",
                    "detail": "如特定 Runner 的 NPU 有问题，尝试其他 Runner"
                }
            ]
        },
        "hccl": {
            "title": "HCCL 通信失败处理",
            "steps": [
                {
                    "action": "检查多卡状态",
                    "detail": "确认所有 NPU 卡状态正常"
                },
                {
                    "action": "重新触发",
                    "detail": "HCCL 问题可能是暂时性，重试可解决"
                },
                {
                    "action": "检查网络",
                    "detail": "如持续失败，检查 NPU 间网络通信"
                }
            ]
        },
        "timeout": {
            "title": "构建超时处理",
            "steps": [
                {
                    "action": "重新触发",
                    "detail": "超时可能是 Runner 问题，重试通常可解决"
                },
                {
                    "action": "检查测试时长",
                    "detail": "如持续超时，检查测试是否过慢"
                },
                {
                    "action": "调整 timeout",
                    "detail": "必要时增加 workflow timeout 设置"
                }
            ]
        },
        "docker_image": {
            "title": "Docker 镜像拉取失败处理",
            "steps": [
                {
                    "action": "等待镜像可用",
                    "detail": "镜像仓库可能暂时不可用"
                },
                {
                    "action": "重新触发",
                    "detail": "镜像恢复后重新运行"
                },
                {
                    "action": "联系运维",
                    "detail": "如果持续失败，联系镜像仓库运维"
                }
            ]
        }
    }
    
    return templates.get(issue_type, templates["cache_service"])


def get_interference_fix_template() -> dict:
    """获取干扰问题修复模板。"""
    
    return {
        "title": "多PR并发干扰处理",
        "steps": [
            {
                "action": "等待相关构建完成",
                "detail": "等待其他并发 PR 的构建完成"
            },
            {
                "action": "重新触发构建",
                "detail": "干扰消除后重新运行 workflow"
            },
            {
                "action": "协调合入顺序",
                "detail": "如持续失败，协调多个 PR 的合入时机"
            },
            {
                "action": "联系相关作者",
                "detail": "必要时联系其他 PR 作者协调"
            }
        ]
    }