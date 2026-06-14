import csv
from src.pipeline.row_processor import process_row
from src.cleaning.mappers import GOOGLE_ADS_MAPPING


def process_csv(file_path: str, mapping=GOOGLE_ADS_MAPPING):
    valid_rows = []
    errors = []

    with open(file_path, mode="r") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader):
            result = process_row(row, mapping, i)

            if result["valid"]:
                valid_rows.append(result["data"])
            else:
                errors.append(result["error"])

    return {
        "valid_rows": valid_rows,
        "errors": errors
    }