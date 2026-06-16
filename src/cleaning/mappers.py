from typing import Dict
from src.mappings.registry import MAPPINGS


def map_row(row: Dict, mapping: Dict) -> Dict:
    """
    Convert raw platform row into canonical schema.
    """

    normalized = {}

    for raw_key, value in row.items():
        canonical_key = mapping.get(raw_key)

        if canonical_key:
            normalized[canonical_key] = value

    return normalized