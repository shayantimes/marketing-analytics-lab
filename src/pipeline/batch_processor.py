import csv

from src.pipeline.row_processor import process_row
from src.mappings.registry import MAPPINGS, SCHEMAS


def process_csv(file_path: str, source: str):
    """
    Batch ingestion orchestrator.
    """

    try:
        mapping = MAPPINGS[source]
        schema = SCHEMAS[source]
    except KeyError:
        raise ValueError(f"Unknown source: {source}")

    valid_rows = []
    errors = []

    with open(file_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):

            result = process_row(
                row=row,
                mapping=mapping,
                row_index=i,
                source=source,
                schema=schema,
            )

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
        },
    }