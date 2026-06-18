import logging

logger = logging.getLogger("pipeline")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
logger.addHandler(handler)


def log_row(index, status, info=None):
    logger.info(f"[ROW {index}] {status} {info or ''}")