from src.pipeline.batch_processor import process_csv


def test_valid_google_ads_file():

    result = process_csv(
        "data/sample_google_ads_campaign.csv",
        "google_ads"
    )

    assert result["summary"]["valid"] == 2
    assert result["summary"]["invalid"] == 0


def test_missing_columns():

    result = process_csv(
        "data/missing_columns.csv",
        "google_ads"
    )

    assert result["summary"]["invalid"] > 0


def test_invalid_numbers():

    result = process_csv(
        "data/invalid_numbers.csv",
        "google_ads"
    )

    assert result["summary"]["invalid"] > 0


def test_bad_date():

    result = process_csv(
        "data/bad_date.csv",
        "google_ads"
    )

    assert result["summary"]["invalid"] > 0