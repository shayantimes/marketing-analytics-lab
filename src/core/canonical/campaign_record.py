from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class CampaignRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: date
    source: str
    campaign_name: str

    impressions: Optional[float] = None
    clicks: Optional[float] = None
    cost: Optional[float] = None
    conversions: Optional[float] = None
    revenue: Optional[float] = None