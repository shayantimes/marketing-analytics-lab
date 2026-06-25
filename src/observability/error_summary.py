from collections import Counter
from typing import List
from src.models.errors import StructuredError


def build_error_summary(errors: List[StructuredError]):
    summary = {
        "by_type": Counter(),
        "by_field": Counter(),
        "by_stage": Counter(),
    }

    for error in errors:
        summary["by_type"][error.error_type] += 1
        summary["by_field"][error.field or "ROW_LEVEL"] += 1
        summary["by_stage"][error.stage] += 1

    return summary