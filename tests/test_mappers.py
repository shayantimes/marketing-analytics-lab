from src.cleaning.mappers import map_row
from src.mappings.registry import MAPPINGS


# Google Ads Mapping Test
def test_google_ads_mapping_exists():
    assert "google_ads" in MAPPINGS
    assert isinstance(MAPPINGS["google_ads"], dict)


# Meta Ads Mapping Test
def test_meta_ads_mapping():
    from src.cleaning.mappers import map_row
    from src.mappings.registry import MAPPINGS

    row = {
        "Date": "2026/05/01",
        "Campaign Name": "Brand Campaign",
        "Amount Spent": "500",
        "Link Clicks": "20"
    }

    mapped = map_row(row, MAPPINGS["meta_ads"])

    assert mapped["date"] == "2026/05/01"
    assert mapped["campaign_name"] == "Brand Campaign"
    assert mapped["cost"] == "500"
    assert mapped["clicks"] == "20"


# Unknown Columns Test
def test_unknown_columns_are_ignored():
    row = {
        "Day": "2026/05/01",
        "Campaign": "Brand",
        "RandomColumn": "SHOULD_BE_IGNORED"
    }

    mapped = map_row(row, MAPPINGS["google_ads"])

    assert "date" in mapped
    assert "campaign_name" in mapped
    assert "RandomColumn" not in mapped