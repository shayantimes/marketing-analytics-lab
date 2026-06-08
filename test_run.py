from src.loaders.unified_loader import UnifiedLoader


loader = UnifiedLoader()

records = loader.load(
    source="google_ads",
    filepath="data/sample_google_ads_campaign.csv"
)

print("TOTAL RECORDS:", len(records))
print("-" * 40)

for r in records:
    print(r)