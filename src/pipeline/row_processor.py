from typing import Dict, Any

from src.cleaning.mappers import map_row
from src.cleaning.cleaners import clean_number, clean_string, clean_date
from src.contracts.validator import validate_record
from src.models.errors import RowError


NUMERIC_FIELDS = {
    "cost",
    "clicks",
    "impressions",
    "conversions",
    "revenue",
}


def process_row(
    row: Dict[str, Any],
    mapping: Dict[str, str],
    row_index: int,
    source: str,
    schema: Any,
) -> Dict:
    """
    Single-row canonical transformation pipeline.
    """

    # 1. MAP
    mapped = map_row(row, mapping)

    # 2. CLEAN
    cleaned = {}

    for key, value in mapped.items():

        if key in NUMERIC_FIELDS:
            cleaned[key] = clean_number(value)

        elif key == "date":
            cleaned[key] = clean_date(value)

        elif key == "campaign_name":
            cleaned[key] = clean_string(value)

        else:
            cleaned[key] = value

    # 3. ENRICH
    cleaned["source"] = source

    # 4. VALIDATE
    is_valid, errors = validate_record(cleaned, schema)

    if is_valid:
        return {
            "valid": True,
            "data": cleaned,
        }

    return {
        "valid": False,
        "error": RowError(
            row_index=row_index,
            errors=errors,
            raw_row=row,
        ),
    }