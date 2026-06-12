# Marketing Analytics Lab

> An end-to-end marketing analytics engine — from raw ad platform exports to KPIs, insights, anomaly alerts, dashboards, budget optimization, experimentation, and forecasting.

---

## Overview

**Marketing Analytics Lab** is a Python-based pipeline that takes raw marketing data (Google Ads, Meta Ads, Yektanet, and more) and turns it into a single, standardized dataset — then builds an entire analytics stack on top of it: KPI calculation, automated insights, performance monitoring, dashboards, budget optimization, A/B testing, and forecasting.

The project is being built incrementally, version by version, with each version adding a new capability on top of a shared canonical data model. The goal is a complete, portfolio-ready marketing analytics system that mirrors how real marketing data teams operate.

```
Raw Data
   ↓
Ingestion          → standardize data from any ad platform
   ↓
KPI Engine         → CTR, CPC, CPA, ROAS, Conversion Rate
   ↓
Insights           → "Google Search has 42% better ROAS than Meta Ads"
   ↓
Monitoring         → anomaly detection & alerts
   ↓
Visualization      → Streamlit dashboards
   ↓
Optimization       → budget allocation recommendations
   ↓
Experiments        → A/B testing & statistical significance
   ↓
Forecasting        → predictive KPI modeling
```

---

## Current Status

🚧 **In active development — currently building V0.0 (Data Ingestion Layer)**

The foundation of the pipeline is in place:

- **Canonical schema** — a unified `CampaignRecord` model that every data source gets mapped into (date, source, campaign, impressions, clicks, cost, conversions, revenue)
- **Adapter pattern** — platform-specific adapters (Google Ads implemented, Meta Ads in progress) convert raw exports into canonical records
- **Unified loader** — single entry point that detects the source and routes data through the correct adapter
- **Validation layer** — Pydantic-based contracts to validate canonical records before they move downstream
- **Tests** — unit tests for the validation layer, with more coverage planned

---

## Roadmap

| Version | Name | Goal | Status |
|---------|------|------|--------|
| **V0.0** | Data Ingestion Layer | Load raw exports (Google Ads, Yektanet) and convert them into a clean, standardized dataset | 🚧 In Progress |
| **V0.1** | KPI Engine | Compute core KPIs — CTR, CPC, CPA, ROAS, Conversion Rate — with a simple CLI report | ⏳ Planned |
| **V0.2** | Ad Performance Detective | Generate business insights: best/worst campaigns, trends, device & channel comparisons | ⏳ Planned |
| **V0.3** | Campaign Health Monitor | Detect CPC spikes, CTR drops, and conversion anomalies, with automated alerts | ⏳ Planned |
| **V0.4** | Visualization Layer | Streamlit dashboard with KPI overview, campaign health, and performance trend pages | ⏳ Planned |
| **V0.5** | Budget Optimizer | Identify high-ROI campaigns and suggest rule-based budget reallocation | ⏳ Planned |
| **V0.6** | Experimentation Lab | A/B test simulation, statistical significance, confidence intervals (Bayesian testing later) | ⏳ Planned |
| **V0.7** | Forecasting & Predictive Analytics | Forecast KPIs (CTR, CPC, ROAS, CPA) using time series models and simulate budget impact | ⏳ Planned |

---

## Project Structure

```
marketing-analytics-lab/
├── data/
│   └── sample_google_ads_campaign.csv   # Sample raw export for testing
├── src/
│   ├── core/
│   │   └── canonical/
│   │       └── campaign_record.py       # Canonical CampaignRecord data model
│   ├── adapters/
│   │   ├── base.py                      # Abstract adapter contract
│   │   ├── google_ads/
│   │   │   └── campaign_adapter.py      # Google Ads → CampaignRecord
│   │   └── meta_ads/
│   │       └── campaign_adapter.py      # Meta Ads → CampaignRecord (in progress)
│   ├── loaders/
│   │   └── unified_loader.py            # Source-aware loader, dispatches to adapters
│   ├── contracts/
│   │   ├── canonical_schema.py          # Pydantic schema for validation
│   │   └── validator.py                 # Record validation logic
│   └── validators/
│       └── csv_validator.py             # Raw CSV validation (in progress)
├── tests/
│   └── test_validator.py                # Unit tests for validation
├── test_run.py                          # End-to-end pipeline demo script
└── requirements.txt
```

---

## How It Works

1. **Adapters** convert raw, platform-specific data (e.g. a Google Ads CSV export) into the canonical `CampaignRecord` format — a consistent structure regardless of where the data came from.
2. The **Unified Loader** picks the right adapter automatically based on the data source.
3. **Contracts** (Pydantic models) validate each record to ensure data quality before it's used downstream.
4. Every future module (KPI engine, insights, dashboards, forecasting, etc.) builds on top of this single canonical dataset — so adding a new ad platform never breaks the rest of the pipeline.

---

## Quickstart

```bash
# Clone the repo
git clone https://github.com/<your-username>/marketing-analytics-lab.git
cd marketing-analytics-lab

# Install dependencies
pip install -r requirements.txt

# Run the end-to-end demo
python test_run.py
```

Example output:

```
TOTAL RECORDS: 2
----------------------------------------
CampaignRecord(source='google_ads', date=datetime.date(2026, 5, 1), platform_campaign_id='123', campaign_name='Brand Search', impressions=10000, clicks=500, cost=250.0, conversions=20.0, revenue=1500.0)
CampaignRecord(source='google_ads', date=datetime.date(2026, 5, 2), platform_campaign_id='123', campaign_name='Brand Search', impressions=12000, clicks=600, cost=300.0, conversions=25.0, revenue=1800.0)
```

---

## Tech Stack

- **Python** — core language
- **Pandas** — data loading and transformation
- **Pydantic** — data validation and contracts
- **Pytest** — testing
- *(Coming soon)* Streamlit, statsmodels/Prophet for forecasting, plotting libraries

---

## Adding a New Data Source

The adapter pattern makes it straightforward to support a new platform:

1. Create a new adapter under `src/adapters/<platform>/campaign_adapter.py` that implements `BaseCampaignAdapter`
2. Map the platform's raw columns to the canonical `CampaignRecord` fields
3. Register the source in `UnifiedLoader`
4. Add a sample CSV under `data/` and a test under `tests/`

---

## Contributing

This project is currently a solo learning/portfolio lab and evolving quickly. Suggestions, issue reports, and ideas are welcome — feel free to open an issue or discussion.

## License

This project is licensed under the MIT License.
