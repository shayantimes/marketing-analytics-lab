import csv

from src.pipeline.row_processor import process_row
from src.mappings.registry import MAPPINGS


def process_csv(file_path: str, source: str):
    """
    Process full CSV file into canonical dataset
    """

    mapping = MAPPINGS.get(source)

    if not mapping:
        raise ValueError(f"Unknown source: {source}")

    valid_rows = []
    errors = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):

            result = process_row(row, mapping, i, source)

            if result["valid"]:
                valid_rows.append(result["data"])
            else:
                errors.append(result["error"])

    return {
        "valid_rows": valid_rows,
        "errors": errors,
        "summary": {
            "total": len(valid_rows) + len(errors),
            "valid": len(valid_rows),
            "invalid": len(errors),
        }
    }