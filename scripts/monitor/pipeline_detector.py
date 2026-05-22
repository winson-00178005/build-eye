"""流水线类型检测器 - 根据 workflow 名称和触发方式识别 PR/Nightly/Weekly/Manual 类型。"""
import re
from typing import Dict, Any, List


PIPELINE_PR = "pr"
PIPELINE_NIGHTLY = "nightly"
PIPELINE_WEEKLY = "weekly"
PIPELINE_MANUAL = "manual"


class PipelineDetector:
    """根据配置中的名称模式识别 workflow run 的流水线类型。"""

    def __init__(self, pipeline_types: Dict[str, Any] | None = None):
        self.pipeline_types = pipeline_types or {}

    def detect(self, workflow_run: Dict[str, Any]) -> Dict[str, Any]:
        """检测单个 workflow run 的流水线类型。"""
        workflow_name = workflow_run.get("name", "")
        event = workflow_run.get("event", "")

        if event == "workflow_dispatch":
            return {
                "pipeline_type": PIPELINE_MANUAL,
                "pipeline_type_label": "手动触发",
                "source": "event"
            }

        for ptype, patterns in self.pipeline_types.items():
            name_patterns = patterns.get("name_patterns", [])

            for pattern in name_patterns:
                if self._match_pattern(workflow_name, pattern):
                    label_map = {
                        PIPELINE_NIGHTLY: "每日定时",
                        PIPELINE_WEEKLY: "每周定时",
                        PIPELINE_PR: "PR 流水线"
                    }
                    return {
                        "pipeline_type": ptype,
                        "pipeline_type_label": label_map.get(ptype, ptype),
                        "source": "name_pattern",
                        "matched_pattern": pattern
                    }

        if event == "schedule":
            return {
                "pipeline_type": PIPELINE_NIGHTLY,
                "pipeline_type_label": "每日定时",
                "source": "event_fallback"
            }

        return {
            "pipeline_type": PIPELINE_PR,
            "pipeline_type_label": "PR 流水线",
            "source": "default"
        }

    def detect_all(self, workflow_runs: List[Dict]) -> List[Dict]:
        """批量检测流水线类型，将结果嵌入各 run。"""
        for run in workflow_runs:
            result = self.detect(run)
            run["pipeline_info"] = result
        return workflow_runs

    def filter_by_type(self, workflow_runs: List[Dict], pipeline_type: str) -> List[Dict]:
        """按流水线类型过滤。"""
        return [
            r for r in workflow_runs
            if r.get("pipeline_info", {}).get("pipeline_type") == pipeline_type
        ]

    def _match_pattern(self, name: str, pattern: str) -> bool:
        """匹配 workflow 名称（支持通配符 * 和 fnmatch 语法）。"""
        regex = pattern.replace("*", ".*").replace("?", ".")
        return bool(re.match(regex, name, re.IGNORECASE))