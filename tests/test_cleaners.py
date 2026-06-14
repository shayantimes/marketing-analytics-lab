from src.cleaning.cleaners import (
    clean_number,
    clean_string,
    clean_date
)


def test_clean_number():
    assert clean_number("1,234") == 1234.0


def test_clean_string():
    assert clean_string("  brand  ") == "brand"


def test_clean_date():
    assert str(clean_date("2026/05/01")) == "2026-05-01"