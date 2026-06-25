import os


def test_no_legacy_schema():
    matches = []

    for root, _, files in os.walk("src"):
        for f in files:
            if "canonical_schema" in f:
                matches.append(f)

    assert len(matches) == 0, f"Legacy schema still exists: {matches}"