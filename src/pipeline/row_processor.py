from typing import Dict, Any

from src.cleaning.mappers import map_row
from src.cleaning.cleaners import clean_number, clean_string, clean_date
from src.contracts.validator import validate_record
from src.models.errors import StructuredError, RowError
from src.observability.logger import log_row_trace
from src.observability.error_classifier import classify_error


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
    Single-row canonical transformation pipeline:
    MAP → CLEAN → VALIDATE + OBSERVABILITY
    """

    structured_errors = []

    # =========================
    # 1. MAP
    # =========================
    log_row_trace(row_index, "mapping", "start")
    mapped = map_row(row, mapping)
    log_row_trace(row_index, "mapping", "ok")

    # =========================
    # 2. CLEAN
    # =========================
    cleaned = {}

    for key, value in mapped.items():

        # ---- numeric fields ----
        if key in NUMERIC_FIELDS:
            try:
                cleaned[key] = clean_number(value)

            except Exception as e:
                structured_errors.append(
                    StructuredError(
                        row_index=row_index,
                        field=key,
                        message=str(e),
                        error_type="CLEANING",
                        stage="clean",
                        raw_value=value,
                        raw_row=row,
                    )
                )
                cleaned[key] = None

        # ---- date ----
        elif key == "date":
            try:
                cleaned[key] = clean_date(value)

            except Exception as e:
                structured_errors.append(
                    StructuredError(
                        row_index=row_index,
                        field=key,
                        message=str(e),
                        error_type="CLEANING",
                        stage="clean",
                        raw_value=value,
                        raw_row=row,
                    )
                )
                cleaned[key] = None

        # ---- string ----
        elif key == "campaign_name":
            try:
                cleaned[key] = clean_string(value)

            except Exception as e:
                structured_errors.append(
                    StructuredError(
                        row_index=row_index,
                        field=key,
                        message=str(e),
                        error_type="CLEANING",
                        stage="clean",
                        raw_value=value,
                        raw_row=row,
                    )
                )
                cleaned[key] = None

        # ---- passthrough ----
        else:
            cleaned[key] = value

    # =========================
    # 3. ENRICH
    # =========================
    cleaned["source"] = source

    # =========================
    # 4. VALIDATE
    # =========================
    log_row_trace(row_index, "validation", "start")

    is_valid, validation_errors = validate_record(cleaned, schema)

    log_row_trace(
        row_index,
        "validation",
        "ok" if is_valid else "failed"
    )

    # =========================
    # 5. MERGE ERRORS
    # =========================
    all_errors = list(structured_errors)

    for e in (validation_errors or []):
        all_errors.append(
            StructuredError(
                row_index=row_index,
                field=e.get("loc", [None])[0] if isinstance(e, dict) else None,
                message=e.get("msg") if isinstance(e, dict) else str(e),
                error_type="VALIDATION",
                stage="validate",
                raw_value=None,
                raw_row=row,
            )
        )

    # =========================
    # 6. RESULT
    # =========================
    if is_valid and len(all_errors) == 0:
        return {
            "valid": True,
            "data": cleaned,
    }

    return {
        "valid": False,
        "error": RowError(
            row_index=row_index,
            errors=all_errors,
        )
}