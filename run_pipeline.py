from src.pipeline.batch_processor import process_csv


def run_test():
    result = process_csv(
        file_path="data/invalid_numbers.csv",
        source="google_ads",
    )

    print("\n===== PIPELINE TEST =====\n")

    summary = result["summary"]

    print(f"TOTAL: {summary['total']}")
    print(f"VALID: {summary['valid']}")
    print(f"INVALID: {summary['invalid']}")

    print("\n--- VALID ROWS ---\n")
    for row in result["valid_rows"]:
        print(row)

    print("\n--- ERROR SUMMARY ---\n")

    for error_type, count in result["error_summary"].items():
        print(f"{error_type}: {count}")


if __name__ == "__main__":
    run_test()