"""分类规则测试 - 样本失败日志。"""
import pytest
from scripts.classify.code_detector import detect_code_issues
from scripts.classify.infra_detector import detect_infrastructure_issues
from scripts.classify.interference_detector import detect_interference_issues


SAMPLE_LOG_TEST_FAILURE = """
FAILED tests/e2e/singlecard/test_inference.py::test_basic_inference
AssertionError: Expected output shape (1, 100) but got (1, 50)
"""

SAMPLE_LOG_COMPILATION_ERROR = """
error: undefined symbol 'vllm_forward'
CMake Error at cmake/CANN.cmake:45
"""

SAMPLE_LOG_CACHE_SERVICE_FAILURE = """
Could not find a version that satisfies the requirement torch>=2.0
cache-service.nginx-pypi-cache.svc.cluster.local connection refused
"""

SAMPLE_LOG_NPU_FAILURE = """
npu-smi info shows ECC error on device 0
NPU memory allocation failed
"""

SAMPLE_LOG_HCCL_FAILURE = """
HCCL error: rank 0 communication timeout
collective operation failed for all_reduce
"""

SAMPLE_LOG_TIMEOUT = """
The job was stopped after 6 hours
Timeout exceeded for job e2e-full
"""


def test_code_issue_detection():
    """测试代码问题检测。"""
    
    result = detect_code_issues(
        SAMPLE_LOG_TEST_FAILURE,
        {"number": 123},
        {}
    )
    
    assert result["detected"] == True
    assert result["category_detail"] is not None


def test_compilation_detection():
    """测试编译错误检测。"""
    
    result = detect_code_issues(
        SAMPLE_LOG_COMPILATION_ERROR,
        {"number": 456},
        {}
    )
    
    assert result["detected"] == True


def test_infra_cache_service_detection():
    """测试 K8s cache-service 失败检测。"""
    
    result = detect_infrastructure_issues(
        SAMPLE_LOG_CACHE_SERVICE_FAILURE,
        {"name": "test-job"},
        {}
    )
    
    assert result["detected"] == True
    assert "cache_service" in str(result["evidence"])


def test_infra_npu_detection():
    """测试 NPU 硬件问题检测。"""
    
    result = detect_infrastructure_issues(
        SAMPLE_LOG_NPU_FAILURE,
        {"runner_name": "linux-aarch64-a2b3-0"},
        {}
    )
    
    assert result["detected"] == True


def test_infra_hccl_detection():
    """测试 HCCL 通信失败检测。"""
    
    result = detect_infrastructure_issues(
        SAMPLE_LOG_HCCL_FAILURE,
        {"name": "e2e-4-cards"},
        {}
    )
    
    assert result["detected"] == True


def test_timeout_detection():
    """测试超时检测。"""
    
    result = detect_infrastructure_issues(
        SAMPLE_LOG_TIMEOUT,
        {"name": "e2e-full"},
        {}
    )
    
    assert result["detected"] == True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])