from typing import Any, Dict, Tuple, List, Optional

from pydantic import ValidationError

from src.models.errors import StructuredError


def validate_record(record: Dict[str, Any], schema=None) -> Tuple[bool, List[StructuredError]]:
    """
    Validate a single canonical record against schema.

    Returns:
        (is_valid, list of StructuredError)
    """

    # -------------------------
    # fallback schema
    # -------------------------
    if schema is None:
        from src.core.canonical.campaign_record import CampaignRecord
        schema = CampaignRecord

    errors: List[StructuredError] = []

    # -------------------------
    # validation
    # -------------------------
    try:
        # Pydantic v2 style
        schema.model_validate(record)

        return True, []

    except ValidationError as e:

        for err in e.errors():

            errors.append(
                StructuredError(
                    row_index=None,
                    field=err.get("loc", [None])[0] if err.get("loc") else None,
                    message=err.get("msg", "validation error"),
                    error_type="VALIDATION",
                    stage="validate",
                    raw_value=err.get("input"),
                    raw_row=record,
                )
            )

        return False, errors

    except Exception as e:

        # fallback safety net
        return False, [
            StructuredError(
                row_index=None,
                field=None,
                message=str(e),
                error_type="VALIDATION",
                stage="validate",
                raw_value=None,
                raw_row=record,
            )
        ]