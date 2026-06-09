import time
from datetime import datetime

import pandas as pd

from tools.asset_search_tool import AssetSearchTool

# ==========================================
# Project Version
# ==========================================

PROJECT_VERSION = "v1.0"

# ==========================================
# Load Data
# ==========================================

questions_df = pd.read_csv(
    "eval_questions.csv",
    encoding="utf-8-sig"
)

tool = AssetSearchTool()

results = []

total_tests = len(questions_df)

print("\n==============================")
print("RAG Evaluation Started")
print("==============================\n")

# ==========================================
# Run Tests
# ==========================================

for index, row in questions_df.iterrows():

    query = row["query"]
    expected_asset = row["expected_asset"]

    start_time = time.time()

    result = tool.search_business_asset(query)

    end_time = time.time()

    response_time = end_time - start_time

    actual_asset = result["image_id"]

    similarity = result["similarity"]

    success = actual_asset == expected_asset

    results.append({
        "version": PROJECT_VERSION,
        "query": query,
        "expected_asset": expected_asset,
        "actual_asset": actual_asset,
        "success": success,
        "similarity": round(similarity, 4),
        "response_time_sec": round(response_time, 4)
    })

    print(f"Test #{index + 1}")
    print(f"Query      : {query}")
    print(f"Expected   : {expected_asset}")
    print(f"Actual     : {actual_asset}")
    print(f"Success    : {success}")
    print(f"Similarity : {similarity:.4f}")
    print(f"Time       : {response_time:.4f} sec")
    print("-" * 40)

# ==========================================
# Summary Metrics
# ==========================================

success_count = sum(
    result["success"]
    for result in results
)

accuracy = (
    success_count / total_tests
) * 100

success_rate = accuracy

average_similarity = (
    sum(result["similarity"] for result in results)
    / total_tests
)

average_response_time = (
    sum(result["response_time_sec"] for result in results)
    / total_tests
)

# ==========================================
# Save Detailed Results
# ==========================================

results_df = pd.DataFrame(results)

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

results_file = (
    f"evaluation_results_{timestamp}.csv"
)

results_df.to_csv(
    results_file,
    index=False,
    encoding="utf-8-sig"
)

# ==========================================
# Save Summary
# ==========================================

summary_df = pd.DataFrame([
    {
        "version": PROJECT_VERSION,
        "total_tests": total_tests,
        "success_count": success_count,
        "accuracy_percent": round(accuracy, 2),
        "success_rate_percent": round(success_rate, 2),
        "avg_similarity": round(
            average_similarity,
            4
        ),
        "avg_response_time_sec": round(
            average_response_time,
            4
        )
    }
])

summary_df.to_csv(
    f"evaluation_summary_{timestamp}.csv",
    index=False,
    encoding="utf-8-sig"
)

# ==========================================
# Final Report
# ==========================================

print("\n==============================")
print("EVALUATION SUMMARY")
print("==============================")

print(f"Version: {PROJECT_VERSION}")
print(f"Total Tests: {total_tests}")
print(f"Successes: {success_count}")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Success Rate: {success_rate:.2f}%")
print(f"Average Similarity: {average_similarity:.4f}")
print(
    f"Average Response Time: "
    f"{average_response_time:.4f} sec"
)

print("\nDetailed Results:")
print(results_file)

print("\nSummary Results:")
print(
    f"evaluation_summary_{timestamp}.csv"
)