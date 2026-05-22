"""Pipeline Detector 测试。"""
import pytest
from scripts.monitor.pipeline_detector import PipelineDetector, PIPELINE_PR, PIPELINE_NIGHTLY, PIPELINE_WEEKLY, PIPELINE_MANUAL


PIPELINE_CONFIG = {
    "nightly": {
        "name_patterns": ["Nightly-*", "*_nightly_*", "schedule_nightly_*"],
        "schedule_patterns": ["0 3 * * *"],
        "alert_on_consecutive_failures": 2
    },
    "weekly": {
        "name_patterns": ["Weekly-*", "*_weekly_*"],
        "schedule_patterns": ["0 3 * * 0"]
    }
}


def test_detect_nightly_by_name():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "Nightly-A2", "event": "schedule"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_NIGHTLY
    assert result["source"] == "name_pattern"


def test_detect_nightly_by_name_pattern():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "schedule_nightly_test_a2", "event": "schedule"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_NIGHTLY


def test_detect_weekly_by_name():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "Weekly-Smoke-Test", "event": "schedule"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_WEEKLY


def test_detect_manual_dispatch():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "E2E-Full", "event": "workflow_dispatch"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_MANUAL
    assert result["source"] == "event"


def test_detect_pr_default():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "E2E-Light", "event": "push"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_PR
    assert result["source"] == "default"


def test_detect_schedule_without_name_match():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "Some-Custom-Schedule", "event": "schedule"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_NIGHTLY
    assert result["source"] == "event_fallback"


def test_detect_all():
    detector = PipelineDetector(PIPELINE_CONFIG)
    runs = [
        {"name": "Nightly-A2", "event": "schedule"},
        {"name": "E2E-Full", "event": "push"},
        {"name": "Weekly-Smoke", "event": "schedule"}
    ]
    results = detector.detect_all(runs)
    assert results[0]["pipeline_info"]["pipeline_type"] == PIPELINE_NIGHTLY
    assert results[1]["pipeline_info"]["pipeline_type"] == PIPELINE_PR
    assert results[2]["pipeline_info"]["pipeline_type"] == PIPELINE_WEEKLY


def test_filter_by_type():
    detector = PipelineDetector(PIPELINE_CONFIG)
    runs = [
        {"name": "Nightly-A2", "event": "schedule", "pipeline_info": {"pipeline_type": PIPELINE_NIGHTLY}},
        {"name": "E2E-Full", "event": "push", "pipeline_info": {"pipeline_type": PIPELINE_PR}},
        {"name": "Weekly-Smoke", "event": "schedule", "pipeline_info": {"pipeline_type": PIPELINE_WEEKLY}}
    ]
    nightly = detector.filter_by_type(runs, PIPELINE_NIGHTLY)
    assert len(nightly) == 1


def test_wildcard_pattern():
    detector = PipelineDetector({"nightly": {"name_patterns": ["nightly_*"]}})
    run = {"name": "nightly_test", "event": "schedule"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_NIGHTLY


def test_empty_config():
    detector = PipelineDetector({})
    run = {"name": "SomeWorkflow", "event": "push"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_PR


if __name__ == "__main__":
    pytest.main([__file__, "-v"])