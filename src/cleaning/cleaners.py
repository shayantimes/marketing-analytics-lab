# Cleaning functions for different data types

# Numeric cleaning
def clean_number(value):
    try:
        if value is None:
            return None

        value = str(value).strip().replace(",", "")

        if value == "":
            return None

        return float(value)

    except Exception:
        raise ValueError(f"Invalid number: {value}")

# String cleaning
def clean_string(value):
    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    return value

from datetime import datetime

# Date cleaning
def clean_date(value):
    if value is None:
        return None

    value = str(value).strip()

    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d/%m/%Y"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Unsupported date format: {value}")

