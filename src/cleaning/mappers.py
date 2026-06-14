# Platforms Mapping

# Google Ads
GOOGLE_ADS_MAPPING = {
    "Day": "date",
    "Campaign": "campaign_name",
    "Cost": "cost",
    "Clicks": "clicks",
    "Impressions": "impressions",
    "Conversions": "conversions",
    "Revenue": "revenue",
}

# Meta Ads
META_ADS_MAPPING = {
    "Date": "date",
    "Campaign Name": "campaign_name",
    "Amount Spent": "cost",
    "Link Clicks": "clicks",
    "Impressions": "impressions",
    "Purchases": "conversions",
}


# Mapping Functions
from typing import Dict


def map_row(row: Dict, mapping: Dict) -> Dict:
    """
    Convert platform-specific row into canonical schema keys.
    """

    normalized = {}

    for raw_key, value in row.items():
        canonical_key = mapping.get(raw_key)

        # فقط ستون‌هایی که map شده‌اند وارد می‌شوند
        if canonical_key:
            normalized[canonical_key] = value

    return normalized