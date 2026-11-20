import pytest
from app import calculate_deployment_score, validate_release_gate

def test_score_calculation():
    assert calculate_deployment_score(19, 20) == 95.0

def test_zero_total_tests_raises():
    with pytest.raises(ValueError):
        calculate_deployment_score(0, 0)

def test_release_gate_threshold():
    assert validate_release_gate(98.5) is True
    assert validate_release_gate(80.0) is False
