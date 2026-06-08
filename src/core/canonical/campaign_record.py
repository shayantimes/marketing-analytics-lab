from dataclasses import dataclass
from datetime import date


@dataclass
class CampaignRecord:
    source: str

    date: date

    platform_campaign_id: str | None

    campaign_name: str

    impressions: int
    clicks: int

    cost: float

    conversions: float
    revenue: float