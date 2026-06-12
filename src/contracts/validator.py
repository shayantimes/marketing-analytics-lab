from src.contracts.canonical_schema import CampaignRecord
from pydantic import ValidationError


def validate_record(record: dict):
    try:
        CampaignRecord(**record)
        return True, None

    except ValidationError as e:
        return False, e.errors()