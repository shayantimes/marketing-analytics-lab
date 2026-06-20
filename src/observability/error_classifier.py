def classify_error(exception, field=None, stage="unknown"):
    error_str = str(exception).lower()

    if "missing" in error_str:
        return "MISSING_FIELD"

    if "float" in error_str or "number" in error_str:
        return "INVALID_TYPE"

    if stage == "clean":
        return "CLEANING_FAILED"

    return "UNKNOWN_ERROR"