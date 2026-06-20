from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class StructuredError:
    row_index: int
    field: Optional[str]
    message: str
    error_type: str          # CLEANING / VALIDATION / MAPPING
    stage: str               # map / clean / validate
    raw_value: Any
    raw_row: dict