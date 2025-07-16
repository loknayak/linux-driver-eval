
def calculate_overall_score(metrics):
    weights = {
        "compilation": 0.4,
        "functionality": 0.2,
        "security": 0.2,
        "code_quality": 0.1,
        "performance": 0.1
    }

    score = 0.0
    for category, weight in weights.items():
        if category in metrics:
            category_score = sum(metrics[category].values()) / len(metrics[category])
            score += category_score * weight * 100  # Convert to percentage
    return round(score, 2)


# Example structure (to be filled by other scripts dynamically)
evaluation_metrics_template = {
    "compilation": {
        "success_rate": 1.0,
        "warnings_count": 0,
        "errors_count": 0
    },
    "functionality": {
        "basic_operations": 0.9,
        "error_handling": 0.8,
        "edge_cases": 0.6
    },
    "security": {
        "buffer_safety": 0.95,
        "race_conditions": 0.8,
        "input_validation": 0.7
    },
    "code_quality": {
        "style_compliance": 0.85,
        "documentation": 0.6,
        "maintainability": 0.75
    },
    "performance": {
        "efficiency": 0.9,
        "memory_usage": 0.85,
        "scalability": 0.8
    }
}
