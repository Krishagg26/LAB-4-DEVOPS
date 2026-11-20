def calculate_deployment_score(passed_tests: int, total_tests: int) -> float:
    if total_tests <= 0:
        raise ValueError("Total tests must be greater than zero")
    return round((passed_tests / total_tests) * 100, 2)

def health_check_endpoint() -> dict:
    return {"status": "healthy", "service": "enterprise-api", "version": "1.0.0"}

def validate_release_gate(score: float, threshold: float = 95.0) -> bool:
    return score >= threshold
