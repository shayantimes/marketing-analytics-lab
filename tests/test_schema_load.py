from src.core.canonical.campaign_record import CampaignRecord


def test_schema_load():
    fields = CampaignRecord.model_fields

    assert "date" in fields
    assert "campaign_name" in fields
    assert "impressions" in fields

    print("✔ Schema loaded correctly")