from src.pipeline.batch_processor import process_csv


def test_pipeline_smoke():
    result = process_csv(
        "data/google_ads_sample.csv",
        "google_ads"
    )

    assert "summary" in result
    assert result["summary"]["total"] > 0