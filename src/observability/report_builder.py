from collections import Counter
from typing import List, Dict, Any
from src.models.errors import StructuredError


def build_error_summary(errors: List[StructuredError]) -> Dict[str, Any]:
    summary = {
        "total_errors": len(errors),
        "by_type": Counter(),
        "by_field": Counter(),
        "by_stage": Counter(),
    }

    for e in errors:
        # error type (CLEANING / VALIDATION)
        summary["by_type"][e.error_type or "UNKNOWN"] += 1

        # field (impressions / cost / etc)
        field = e.field if e.field else "ROW_LEVEL"
        summary["by_field"][field] += 1

        # stage (clean / validate / map)
        summary["by_stage"][e.stage or "UNKNOWN"] += 1

    return {
        "total_errors": summary["total_errors"],
        "by_type": dict(summary["by_type"]),
        "by_field": dict(summary["by_field"]),
        "by_stage": dict(summary["by_stage"]),
    }