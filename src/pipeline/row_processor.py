from src.cleaning.mappers import GOOGLE_ADS_MAPPING, map_row
from src.cleaning.cleaners import clean_number, clean_string, clean_date
from src.contracts.validator import validate_record


def process_row(row: dict, mapping: dict, row_index: int):
    """
    Process a single CSV row into canonical record
    """

    # 1. MAP
    mapped = map_row(row, mapping)

    # 2. CLEAN
    cleaned = {}

    for key, value in mapped.items():

        if key in ["cost", "clicks", "impressions", "conversions", "revenue"]:
            cleaned[key] = clean_number(value)

        elif key == "date":
            cleaned[key] = clean_date(value)

        else:
            cleaned[key] = clean_string(value)

    # 3. VALIDATE
    is_valid, errors = validate_record(cleaned)

    if is_valid:
        return {
            "valid": True,
            "data": cleaned
        }

    from src.models.errors import RowError

    return {
        "valid": False,
        "error": RowError(
            row_index=row_index,
            errors=errors,
            raw_row=row
        )
    }