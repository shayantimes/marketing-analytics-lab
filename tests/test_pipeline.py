from src.pipeline.batch_processor import process_csv


def test_pipeline_runs():
    result = process_csv("data/sample_google_ads_campaign.csv")

    assert "valid_rows" in result
    assert "errors" in result