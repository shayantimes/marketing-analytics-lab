from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class StructuredError:
    row_index: int
    field: Optional[str]
    message: str
    error_type: str
    stage: str
    raw_value: Any
    raw_row: dict


@dataclass
class RowError:
    row_index: int
    errors: list[StructuredError]