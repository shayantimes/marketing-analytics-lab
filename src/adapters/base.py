from abc import ABC, abstractmethod
import pandas as pd

from src.core.canonical.campaign_record import CampaignRecord


class BaseCampaignAdapter(ABC):
    """
    Contract for all ad platform adapters.
    Every platform MUST convert raw data into CampaignRecord.
    """

    @abstractmethod
    def adapt(self, df: pd.DataFrame) -> list[CampaignRecord]:
        pass