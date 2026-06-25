from datetime import date, datetime
from dataclasses import asdict, is_dataclass


def to_json_safe(obj):
    """
    Convert any runtime object into JSON-safe format.
    Used by pipeline + exporter.
    """

    if is_dataclass(obj):
        return asdict(obj)

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    if isinstance(obj, set):
        return list(obj)

    if isinstance(obj, dict):
        return {k: to_json_safe(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [to_json_safe(x) for x in obj]

    return obj