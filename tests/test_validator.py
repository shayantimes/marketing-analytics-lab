from src.contracts.validator import validate_record


def test_valid_record():
    valid_record = {
        "date": "2026-05-01",
        "source": "google_ads",
        "campaign_name": "brand",

        "impressions": 1000,
        "clicks": 50,

        "cost": 10.5,
        "conversions": 3,
        "revenue": 100
    }

    is_valid, errors = validate_record(valid_record)

    assert is_valid is True
    assert errors is None


def test_missing_field():
    invalid_record = {
        "date": "2026-05-01",
        "source": "google_ads"
    }

    is_valid, errors = validate_record(invalid_record)

    assert is_valid is False
    assert errors is not None

    #error مربوط به فیلدهاست
    error_fields = [e["loc"][0] for e in errors]

    assert "campaign_name" in error_fields
    assert "impressions" in error_fields
    assert "clicks" in error_fields
    assert "cost" in error_fields
    assert "conversions" in error_fields
    assert "revenue" in error_fields