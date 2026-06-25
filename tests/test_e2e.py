import subprocess


def test_cli_pipeline():
    result = subprocess.run(
        [
            "python3",
            "run_pipeline.py",
            "data/google_ads_sample.csv",
            "--source",
            "google_ads"
        ],
        capture_output=True,
        text=True
    )

    assert "PIPELINE TEST" in result.stdout
    assert result.returncode == 0