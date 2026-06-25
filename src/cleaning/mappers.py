from typing import Dict
from src.mappings.registry import MAPPINGS


def map_row(row, mapping):
    result = {}

    for raw_key, canonical_key in mapping.items():
        if raw_key in row:
            result[canonical_key] = row[raw_key]

    return result