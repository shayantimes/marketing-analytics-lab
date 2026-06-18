from datetime import date

from pydantic import BaseModel


class MetaAdsRecord(BaseModel):

    date: date

    campaign_name: str

    impressions: float

    clicks: float

    cost: float