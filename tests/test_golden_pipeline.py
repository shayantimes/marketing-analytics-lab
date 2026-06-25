import json
from src.pipeline.batch_processor import process_csv


def test_google_ads_golden_pipeline():

    result = process_csv(
        "tests/golden/google_ads_input.csv",
        "google_ads"
    )

    with open("tests/golden/google_ads_expected.json", "r") as f:
        expected = json.load(f)

    assert result["valid_rows"] == expected
    assert result["summary"]["valid"] == 1
    assert result["summary"]["invalid"] == 0