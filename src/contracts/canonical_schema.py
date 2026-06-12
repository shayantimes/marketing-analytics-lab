from datetime import date
from pydantic import BaseModel


class CampaignRecord(BaseModel):
    date: date

    source: str

    campaign_name: str

    impressions: int
    clicks: int

    cost: float

    conversions: float

    revenue: float