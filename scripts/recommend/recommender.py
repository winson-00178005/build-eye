"""修复建议生成器 - 低成本可落地方案。"""
import json
import argparse
import sys
import os
from pathlib import Path
from typing import Dict, Any, List

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))
sys.path.insert(0, str(repo_root / "scripts"))

from recommend.templates import (
    get_code_fix_template,
    get_infra_fix_template,
    get_interference_fix_template
)


class RecommendationGenerator:
    """修复建议生成器。"""
    
    EFFORT_LOW = "低成本"
    EFFORT_MEDIUM = "中等成本"
    EFFORT_HIGH = "高成本"
    
    def generate(self, classification: Dict[str, Any]) -> Dict[str, Any]:
        """为分类结果生成修复建议。"""
        
        classification_type = classification.get("classification", "infrastructure")
        
        if classification_type == "code":
            return self._generate_code_recommendations(classification)
        elif classification_type == "infrastructure":
            return self._generate_infra_recommendations(classification)
        elif classification_type == "interference":
            return self._generate_interference_recommendations(classification)
        
        return {
            "recommendations": [],
            "summary": "无法生成建议，建议人工审查"
        }
    
    def _generate_code_recommendations(self, classification: Dict) -> Dict:
        """生成代码问题修复建议。"""
        
        category_detail = classification.get("category_detail", "")
        evidence = classification.get("evidence", [])
        
        recommendations = []
        
        if "测试" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "检查失败的测试用例",
                "detail": f"查看测试文件中的断言错误",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "查看 job 日志中的具体测试失败信息",
                    "确认测试是否因 PR 代码修改导致"
                ]
            })
            
            recommendations.append({
                "step": 2,
                "action": "修复测试或代码",
                "detail": "根据测试失败原因修改代码或测试用例",
                "effort": self.EFFORT_MEDIUM,
                "commands": [
                    "如果测试预期行为改变，更新测试",
                    "如果代码引入 bug，修复代码逻辑"
                ]
            })
        
        elif "编译" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "检查编译错误位置",
                "detail": "查看 CMake 或 clang 报错的具体文件和行",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "检查 csrc/ 目录中的编译错误",
                    "确认是否因 PR 修改导致"
                ]
            })
            
            recommendations.append({
                "step": 2,
                "action": "修复编译问题",
                "detail": "根据错误类型修复语法或类型问题",
                "effort": self.EFFORT_MEDIUM,
                "commands": [
                    "修复语法错误",
                    "添加缺失的依赖",
                    "更新类型声明"
                ]
            })
        
        elif "vLLM" in category_detail or "导入" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "检查 vLLM API 兼容性",
                "detail": "确认 PR 代码与当前 vLLM 版本兼容",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "检查 vLLM 版本矩阵测试结果",
                    "确认哪个 vLLM 版本导致失败"
                ]
            })
            
            recommendations.append({
                "step": 2,
                "action": "适配 vLLM API 变化",
                "detail": "根据 vLLM 最新 API 更新代码",
                "effort": self.EFFORT_MEDIUM,
                "commands": [
                    "更新导入语句",
                    "适配新的 API 签名",
                    "添加兼容性处理"
                ]
            })
        
        return {
            "recommendations": recommendations,
            "summary": f"代码问题: {category_detail}。建议按步骤修复 PR 代码。",
            "primary_recommendation": recommendations[0] if recommendations else None
        }
    
    def _generate_infra_recommendations(self, classification: Dict) -> Dict:
        """生成基础设施问题修复建议。"""
        
        category_detail = classification.get("category_detail", "")
        evidence = classification.get("evidence", [])
        runner_info = classification.get("runner_info", {})
        
        recommendations = []
        
        if "K8s" in category_detail or "cache-service" in category_detail.lower():
            recommendations.append({
                "step": 1,
                "action": "等待服务恢复",
                "detail": "cache-service.nginx-pypi-cache 通常会自动恢复",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "等待 10-30 分钟后重新触发构建",
                    "如果持续失败，联系基础设施团队"
                ]
            })
        
        elif "Runner" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "等待 Runner 可用",
                "detail": f"Runner {runner_info.get('runner_name', '')} 可能暂时不可用",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "等待 Runner 恢复在线",
                    "或切换到其他 Runner 类型"
                ]
            })
        
        elif "NPU" in category_detail or "CANN" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "检查 NPU 状态",
                "detail": "NPU 硬件或 CANN 可能有问题",
                "effort": self.EFFORT_MEDIUM,
                "commands": [
                    "检查 npu-smi info 输出",
                    "确认 CANN 版本匹配",
                    "如持续失败，联系运维团队"
                ]
            })
        
        elif "HCCL" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "检查多卡通信",
                "detail": "HCCL 通信失败，可能是网络或 NPU 通信问题",
                "effort": self.EFFORT_MEDIUM,
                "commands": [
                    "确认所有 NPU 卡状态正常",
                    "检查 HCCL 配置",
                    "重新触发构建"
                ]
            })
        
        elif "超时" in category_detail:
            recommendations.append({
                "step": 1,
                "action": "重新触发构建",
                "detail": "超时可能是暂时性 Runner 问题",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "重新触发 workflow",
                    "如果持续超时，考虑拆分测试或增加 timeout"
                ]
            })
        
        else:
            recommendations.append({
                "step": 1,
                "action": "重新触发构建",
                "detail": "基础设施问题通常会自动恢复",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "等待几分钟后重新触发 workflow",
                    "如持续失败，联系基础设施团队"
                ]
            })
        
        return {
            "recommendations": recommendations,
            "summary": f"基础设施问题: {category_detail}。不是代码问题，建议重试或联系运维。",
            "primary_recommendation": recommendations[0] if recommendations else None
        }
    
    def _generate_interference_recommendations(self, classification: Dict) -> Dict:
        """生成干扰问题修复建议。"""
        
        related_prs = classification.get("related_prs", [])
        evidence = classification.get("evidence", [])
        
        recommendations = []
        
        recommendations.append({
            "step": 1,
            "action": "重新触发构建",
            "detail": "并发合入导致的干扰通常可通过重试解决",
            "effort": self.EFFORT_LOW,
            "commands": [
                "等待其他 PR 构建完成",
                "重新触发当前 PR 的 workflow"
            ]
        })
        
        if related_prs:
            pr_list = ', '.join([f'#{p.get("number", "?")}' for p in related_prs])
            recommendations.append({
                "step": 2,
                "action": "检查相关 PR",
                "detail": f"查看可能干扰的 PR: {pr_list}",
                "effort": self.EFFORT_LOW,
                "commands": [
                    "检查相关 PR 的构建状态",
                    "确认是否已完成或失败"
                ]
            })
        
        recommendations.append({
            "step": 3,
            "action": "协调合入顺序",
            "detail": "如持续失败，可能需要协调多个 PR 的合入时机",
            "effort": self.EFFORT_MEDIUM,
            "commands": [
                "联系相关 PR 作者",
                "调整合入顺序或时机"
            ]
        })
        
        return {
            "recommendations": recommendations,
            "summary": f"多PR并发干扰。建议重试构建或协调合入顺序。",
            "primary_recommendation": recommendations[0] if recommendations else None,
            "related_prs": related_prs
        }
    
    def generate_all(self, classifications: List[Dict]) -> List[Dict]:
        """为所有分类结果生成建议。"""
        results = []
        
        for c in classifications:
            rec = self.generate(c["classification"])
            
            result = {
                "workflow_run_id": c["workflow_run_id"],
                "pr_number": c["pr_number"],
                "classification": c["classification"],
                "recommendations": rec
            }
            
            results.append(result)
        
        return results


def main():
    parser = argparse.ArgumentParser(description='生成修复建议')
    parser.add_argument('--input', type=str, default='data/classifications.json')
    parser.add_argument('--output', type=str, default='data/recommendations.json')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"输入文件不存在: {input_path}")
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        sys.exit(0)
    
    classifications = json.loads(input_path.read_text(encoding='utf-8'))
    
    if not classifications:
        print("没有分类结果需要生成建议")
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        sys.exit(0)
    
    generator = RecommendationGenerator()
    recommendations = generator.generate_all(classifications)
    
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(recommendations, f, indent=2, ensure_ascii=False)
    
    print(f"已生成 {len(recommendations)} 条建议")


if __name__ == "__main__":
    main()