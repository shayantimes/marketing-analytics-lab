import logging

logger = logging.getLogger("pipeline")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
logger.addHandler(handler)


def log_row_trace(row_index: int, stage: str, status: str, details=None):
    print(f"[ROW {row_index}] {stage.upper()} → {status}")

    if details:
        print(f"   └─ {details}")