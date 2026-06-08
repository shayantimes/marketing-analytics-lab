import pandas as pd

from src.adapters.base import BaseCampaignAdapter
from src.core.canonical.campaign_record import CampaignRecord


class GoogleAdsCampaignAdapter(BaseCampaignAdapter):
    """
    Converts Google Ads Campaign CSV data into Canonical CampaignRecord.
    """

    def adapt(self, df: pd.DataFrame) -> list[CampaignRecord]:

        records: list[CampaignRecord] = []

        for _, row in df.iterrows():

            record = CampaignRecord(
                source="google_ads",

                date=row["Date"],

                platform_campaign_id=str(row["Campaign ID"]),
                campaign_name=row["Campaign"],

                impressions=int(row["Impressions"]),
                clicks=int(row["Clicks"]),

                cost=float(row["Cost"]),

                conversions=float(row["Conversions"]),
                revenue=float(row["Conversion Value"]),
            )

            records.append(record)

        return records