import pandas as pd

from src.adapters.google_ads.campaign_adapter import GoogleAdsCampaignAdapter


class UnifiedLoader:

    def load(self, source: str, filepath: str):

        df = pd.read_csv(filepath)

        if source == "google_ads":
            adapter = GoogleAdsCampaignAdapter()

        else:
            raise ValueError(f"Unsupported source: {source}")

        return adapter.adapt(df)