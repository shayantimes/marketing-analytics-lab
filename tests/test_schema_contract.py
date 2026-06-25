from src.core.canonical.campaign_record import CampaignRecord
from src.mappings.registry import MAPPINGS


def test_mapping_contract():
    schema_fields = set(CampaignRecord.model_fields.keys())
    mapped_fields = set(MAPPINGS["google_ads"].values())

    missing = schema_fields - mapped_fields - {"source"}
    extra = mapped_fields - schema_fields

    print("Missing fields:", missing)
    print("Extra fields:", extra)

    assert missing == set(), f"Missing fields in mapping: {missing}"