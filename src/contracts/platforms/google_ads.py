from datetime import date

from pydantic import BaseModel


class GoogleAdsRecord(BaseModel):

    date: date

    campaign_name: str

    impressions: float
    clicks: float

    cost: float

    conversions: float

    revenue: float