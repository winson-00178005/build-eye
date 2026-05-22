"""Pipeline Detector 测试。"""
import pytest
from scripts.monitor.pipeline_detector import PipelineDetector, PIPELINE_PR, PIPELINE_NIGHTLY, PIPELINE_WEEKLY, PIPELINE_UNMONITORED


PIPELINE_CONFIG = {
    "nightly": {
        "name_patterns": ["Nightly-*", "*_nightly_*", "schedule_nightly_*"],
        "alert_on_consecutive_failures": 2
    },
    "weekly": {
        "name_patterns": ["Weekly-*", "*_weekly_*"]
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


def test_detect_manual_dispatch_is_unmonitored():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "E2E-Full", "event": "workflow_dispatch"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_UNMONITORED


def test_detect_push_to_main_is_unmonitored():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "E2E-Light", "event": "push", "pull_requests": []}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_UNMONITORED


def test_detect_push_with_pr_is_pr_type():
    detector = PipelineDetector(PIPELINE_CONFIG)
    run = {"name": "E2E-Light", "event": "push", "pull_requests": [{"number": 999}]}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_PR


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
        {"name": "E2E-Full", "event": "push", "pull_requests": [{"number": 123}]},
        {"name": "Weekly-Smoke", "event": "schedule"},
        {"name": "E2E-Light", "event": "push", "pull_requests": []},
        {"name": "E2E-Manual", "event": "workflow_dispatch"}
    ]
    results = detector.detect_all(runs)
    assert results[0]["pipeline_info"]["pipeline_type"] == PIPELINE_NIGHTLY
    assert results[1]["pipeline_info"]["pipeline_type"] == PIPELINE_PR
    assert results[2]["pipeline_info"]["pipeline_type"] == PIPELINE_WEEKLY
    assert results[3]["pipeline_info"]["pipeline_type"] == PIPELINE_UNMONITORED
    assert results[4]["pipeline_info"]["pipeline_type"] == PIPELINE_UNMONITORED


def test_filter_by_type():
    detector = PipelineDetector(PIPELINE_CONFIG)
    runs = [
        {"name": "Nightly-A2", "event": "schedule", "pipeline_info": {"pipeline_type": PIPELINE_NIGHTLY}},
        {"name": "E2E-Full", "event": "push", "pipeline_info": {"pipeline_type": PIPELINE_PR}},
        {"name": "Weekly-Smoke", "event": "schedule", "pipeline_info": {"pipeline_type": PIPELINE_WEEKLY}}
    ]
    nightly = detector.filter_by_type(runs, PIPELINE_NIGHTLY)
    assert len(nightly) == 1


def test_filter_exclude_unmonitored():
    detector = PipelineDetector(PIPELINE_CONFIG)
    runs = [
        {"pipeline_info": {"pipeline_type": PIPELINE_NIGHTLY}},
        {"pipeline_info": {"pipeline_type": PIPELINE_UNMONITORED}},
        {"pipeline_info": {"pipeline_type": PIPELINE_PR}},
        {"pipeline_info": {"pipeline_type": PIPELINE_UNMONITORED}}
    ]
    filtered = detector.filter_by_type(runs, PIPELINE_UNMONITORED, exclude=True)
    assert len(filtered) == 2
    assert all(r["pipeline_info"]["pipeline_type"] != PIPELINE_UNMONITORED for r in filtered)


def test_wildcard_pattern():
    detector = PipelineDetector({"nightly": {"name_patterns": ["nightly_*"]}})
    run = {"name": "nightly_test", "event": "schedule"}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_NIGHTLY


def test_empty_config_push_without_pr():
    detector = PipelineDetector({})
    run = {"name": "SomeWorkflow", "event": "push", "pull_requests": []}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_UNMONITORED


def test_empty_config_push_with_pr():
    detector = PipelineDetector({})
    run = {"name": "SomeWorkflow", "event": "push", "pull_requests": [{"number": 1}]}
    result = detector.detect(run)
    assert result["pipeline_type"] == PIPELINE_PR


if __name__ == "__main__":
    pytest.main([__file__, "-v"])