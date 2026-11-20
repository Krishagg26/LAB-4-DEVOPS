from app import calculate_deployment_score, health_check_endpoint, validate_release_gate

def test_health_endpoint_contract():
    resp = health_check_endpoint()
    assert resp["status"] == "healthy"
    assert "version" in resp

def test_end_to_end_pipeline_gate():
    score = calculate_deployment_score(20, 20)
    assert validate_release_gate(score) is True
