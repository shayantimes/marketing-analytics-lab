from src.mappings.google_ads import GOOGLE_ADS_MAPPING
from src.contracts.platforms.google_ads import GoogleAdsRecord

from src.mappings.meta_ads import META_ADS_MAPPING
from src.contracts.platforms.meta_ads import MetaAdsRecord


# ----------------------------
# Mapping Registry
# ----------------------------
MAPPINGS = {
    "google_ads": GOOGLE_ADS_MAPPING,
    "meta_ads": META_ADS_MAPPING,
}


# ----------------------------
# Schema Registry
# ----------------------------
SCHEMAS = {
    "google_ads": GoogleAdsRecord,
    "meta_ads": MetaAdsRecord,
}