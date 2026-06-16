import argparse

from src.pipeline.batch_processor import process_csv


def main():
    parser = argparse.ArgumentParser(description="Run Marketing Analytics Pipeline")

    parser.add_argument("--file", required=True, help="Path to CSV file")
    parser.add_argument("--source", required=True, help="Data source (e.g. google_ads, meta_ads)")

    args = parser.parse_args()

    result = process_csv(
        file_path=args.file,
        source=args.source
    )

    print("\n===== PIPELINE RESULT =====\n")
    print(f"TOTAL ROWS: {result['summary']['total']}")
    print(f"VALID: {result['summary']['valid']}")
    print(f"INVALID: {result['summary']['invalid']}")

    print("\n===== SAMPLE VALID ROWS =====\n")
    for row in result["valid_rows"][:3]:
        print(row)

    print("\n===== ERRORS =====\n")
    for err in result["errors"][:3]:
        print(err)


if __name__ == "__main__":
    main()