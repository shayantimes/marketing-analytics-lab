import json
from pathlib import Path
from datetime import date, datetime
from dataclasses import asdict, is_dataclass
from src.observability.serializer import to_json_safe

OUTPUT_DIR = Path("outputs")


def ensure_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def serialize(obj):
    if is_dataclass(obj):
        return asdict(obj)

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    if isinstance(obj, set):
        return list(obj)

    return obj


def export_json(data, filename: str):
    ensure_output_dir()

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            default=serialize,
            indent=4,
            ensure_ascii=False,
        )

    return str(filepath)


def export_text(text: str, filename: str):
    ensure_output_dir()

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    return str(filepath)