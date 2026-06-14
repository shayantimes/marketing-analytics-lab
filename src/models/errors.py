from pydantic import BaseModel
from typing import List, Any


class RowError(BaseModel):
    row_index: int
    errors: List[Any]
    raw_row: dict