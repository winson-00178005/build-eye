"""流水线类型检测器 - 仅识别 PR/Nightly/Weekly 三种流水线，其余忽略。"""
import re
from typing import Dict, Any, List


PIPELINE_PR = "pr"
PIPELINE_NIGHTLY = "nightly"
PIPELINE_WEEKLY = "weekly"
PIPELINE_UNMONITORED = "unmonitored"


class PipelineDetector:
    """根据配置中的名称模式识别 workflow run 的流水线类型。仅监控 PR/Nightly/Weekly。"""

    def __init__(self, pipeline_types: Dict[str, Any] | None = None):
        self.pipeline_types = pipeline_types or {}

    def detect(self, workflow_run: Dict[str, Any]) -> Dict[str, Any]:
        """检测单个 workflow run 的流水线类型。push到main、手动触发等归为 unmonitored。"""
        workflow_name = workflow_run.get("name", "")
        event = workflow_run.get("event", "")

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

        pull_requests = workflow_run.get("pull_requests", [])
        if pull_requests and event in ("push", "pull_request"):
            return {
                "pipeline_type": PIPELINE_PR,
                "pipeline_type_label": "PR 流水线",
                "source": "has_pr_association"
            }

        return {
            "pipeline_type": PIPELINE_UNMONITORED,
            "pipeline_type_label": "不监控",
            "source": "excluded"
        }

    def detect_all(self, workflow_runs: List[Dict]) -> List[Dict]:
        """批量检测流水线类型，将结果嵌入各 run。"""
        for run in workflow_runs:
            result = self.detect(run)
            run["pipeline_info"] = result
        return workflow_runs

    def filter_by_type(self, workflow_runs: List[Dict], pipeline_type: str, exclude: bool = False) -> List[Dict]:
        """按流水线类型过滤。exclude=True 时排除该类型。"""
        if exclude:
            return [
                r for r in workflow_runs
                if r.get("pipeline_info", {}).get("pipeline_type") != pipeline_type
            ]
        return [
            r for r in workflow_runs
            if r.get("pipeline_info", {}).get("pipeline_type") == pipeline_type
        ]

    def _match_pattern(self, name: str, pattern: str) -> bool:
        """匹配 workflow 名称（支持通配符 * 和 fnmatch 语法）。"""
        regex = pattern.replace("*", ".*").replace("?", ".")
        return bool(re.match(regex, name, re.IGNORECASE))