from pydantic import ValidationError


def validate_record(record: dict, schema):
    """
    Validate a record against a given Pydantic schema.
    Returns:
        (is_valid: bool, errors: list | None)
    """

    try:
        schema(**record)
        return True, None

    except ValidationError as e:
        return False, e.errors()