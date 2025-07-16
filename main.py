import os
import json
from evaluation.compiler import evaluate_compilation
from evaluation.analyzer import analyze_code
from evaluation.metrics import calculate_final_score
# from evaluation.style_checker import check_style  # Optional

def main():
    driver_path = "samples/ai_generated_driver.c"
    
    # Run compilation evaluation
    print("🔧 Running compilation checks...")
    compilation_result = evaluate_compilation(driver_path)
    
    # Run static analysis
    print("📊 Running static analysis...")
    analysis_result = analyze_code(driver_path)
    
    # Optionally, style checking
    # print("🎨 Running style checker...")
    # style_result = check_style(driver_path)

    # Combine all results (basic)
    combined_results = {
        "compilation": compilation_result,
        "functionality": analysis_result.get("functionality", {}),
        "security": analysis_result.get("security", {}),
        "code_quality": analysis_result.get("code_quality", {}),
    }

    # Final score
    print("📈 Calculating final metrics...")
    combined_results["overall_score"] = calculate_final_score(combined_results)

    # Output as JSON
    os.makedirs("test_results", exist_ok=True)
    with open("test_results/final_score.json", "w") as f:
        json.dump(combined_results, f, indent=4)

    print("✅ Evaluation complete. Results saved to test_results/final_score.json")

if __name__ == "__main__":
    main()
