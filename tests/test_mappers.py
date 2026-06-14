from src.cleaning.mappers import map_row, GOOGLE_ADS_MAPPING

# Google Ads Mapping Test
def test_google_ads_mapping():
    row = {
        "Day": "2026/05/01",
        "Campaign": "Brand Search",
        "Cost": "1,234",
        "Clicks": "56"
    }

    mapped = map_row(row, GOOGLE_ADS_MAPPING)

    assert mapped["date"] == "2026/05/01"
    assert mapped["campaign_name"] == "Brand Search"
    assert mapped["cost"] == "1,234"
    assert mapped["clicks"] == "56"


# Meta Ads Mapping Test
from src.cleaning.mappers import map_row, META_ADS_MAPPING


def test_meta_ads_mapping():
    row = {
        "Date": "2026/05/01",
        "Campaign Name": "Brand Campaign",
        "Amount Spent": "500",
        "Link Clicks": "20"
    }

    mapped = map_row(row, META_ADS_MAPPING)

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

    mapped = map_row(row, GOOGLE_ADS_MAPPING)

    assert "date" in mapped
    assert "campaign_name" in mapped
    assert "RandomColumn" not in mapped    