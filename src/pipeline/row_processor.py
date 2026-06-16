from typing import Dict

from src.cleaning.mappers import map_row
from src.cleaning.cleaners import clean_number, clean_string, clean_date
from src.contracts.validator import validate_record
from src.models.errors import RowError


numeric_fields = [
    "cost",
    "clicks",
    "impressions",
    "conversions",
    "revenue",
]


def process_row(row: Dict, mapping: Dict, row_index: int, source: str) -> Dict:
    """
    Process a single CSV row into canonical record.

    Steps:
        1. MAP
        2. CLEAN
        3. VALIDATE
    """

    # 1. MAP
    mapped = map_row(row, mapping)

    # 2. CLEAN
    cleaned = {}

    for key, value in mapped.items():

        if key in numeric_fields:
            cleaned[key] = clean_number(value)

        elif key == "date":
            cleaned[key] = clean_date(value)

        elif key == "campaign_name":
            cleaned[key] = clean_string(value)

        else:
            cleaned[key] = value

    # 🔥 IMPORTANT: inject BEFORE validation
    cleaned["source"] = source

    # 3. VALIDATE
    is_valid, errors = validate_record(cleaned)

    if is_valid:
        return {
            "valid": True,
            "data": cleaned
        }

    return {
        "valid": False,
        "error": RowError(
            row_index=row_index,
            errors=errors,
            raw_row=row
        )
    }