\# Marketing Analytics Lab

> A Python-based end-to-end marketing analytics engine — from raw ad platform exports to a structured canonical dataset, ready for KPI computation, insights, monitoring, and forecasting.

---

## Overview

**Marketing Analytics Lab** is built around one core idea: before you can analyze marketing data, you have to trust it.

This project starts by formalizing a **data contract** — a strict canonical schema that every data source must conform to — and builds a full ingestion pipeline on top of it. Then, version by version, it adds an analytics stack: KPI computation, performance insights, anomaly detection, dashboards, budget optimization, A/B testing, and forecasting.

Each version is self-contained and buildable. The project mirrors how real marketing data teams operate: **schema first, analytics second.**

```
Raw CSV Data (Google Ads / Meta Ads / Yektanet / ...)
          ↓
  Column Mapping          →  platform-specific fields → canonical fields
          ↓
  Cleaning Layer          →  normalize values, types, and formats
          ↓
  Validation Layer        →  Pydantic contract enforcement
          ↓
  Canonical Records       →  unified CampaignRecord objects
          ↓
  KPI Engine              →  CTR, CPC, CPA, ROAS, Conversion Rate
          ↓
  Insight Engine          →  "Google Search has 42% better ROAS than Meta Ads"
          ↓
  Monitoring Layer        →  anomaly detection & automated alerts
          ↓
  Visualization Layer     →  Streamlit dashboards
          ↓
  Budget Optimizer        →  rule-based allocation recommendations
          ↓
  Experimentation Lab     →  A/B testing & statistical significance
          ↓
  Forecasting Engine      →  predictive KPI modeling
```

---

## Current Status

🚧 **V0.0 — Data Foundation Layer (In Progress)**

The foundation is in place. The pipeline can load a raw Google Ads CSV export, map it to the canonical schema, and validate every record before it touches any analytics logic.

### ✔ What's implemented

**Canonical Data Model**
- `CampaignRecord` dataclass — the single source of truth for all downstream analytics
- Fields: `source`, `date`, `platform_campaign_id`, `campaign_name`, `impressions`, `clicks`, `cost`, `conversions`, `revenue`

**Adapter Pattern**
- `BaseCampaignAdapter` — abstract contract every platform adapter must implement
- `GoogleAdsCampaignAdapter` — fully implemented, maps Google Ads CSV exports to `CampaignRecord`
- `MetaAdsAdapter` — scaffolded, in progress

**Unified Loader**
- Single entry point: `UnifiedLoader.load(source, filepath)`
- Source-aware routing — dispatches to the correct adapter automatically

**Contract & Validation Layer**
- `CampaignRecord` Pydantic schema for strict type enforcement
- `validate_record()` — returns `(is_valid, errors)` per record
- Invalid records are isolated and reported, not silently dropped

**Testing**
- Pytest-based unit tests for validation logic (valid records, missing fields, error field reporting)
- `test_run.py` — end-to-end demo script: load → adapt → print canonical records

---

## What's Not Built Yet

- Dirty CSV handling (cleaning layer, column normalization utilities)
- Row processor / batch processor pipeline
- Meta Ads adapter (scaffolded, not yet implemented)
- KPI Engine (CTR, CPC, CPA, ROAS, Conversion Rate)
- Insight Generation Layer
- Anomaly Detection & Alert System
- Streamlit Dashboard
- Budget Optimization Engine
- Experimentation / A/B Testing Framework
- Forecasting Models

---

## Roadmap

| Version | Name | Goal | Status |
|---------|------|------|--------|
| **V0.0** | Data Foundation Layer | Canonical schema, adapter pattern, Pydantic validation, unified loader | 🚧 In Progress |
| **V0.1** | Ingestion Engine | Dirty CSV handling, column mapping, cleaning pipeline, batch processing, structured error reports | ⏳ Planned |
| **V0.2** | KPI Engine | CTR, CPC, CPA, ROAS, Conversion Rate — CLI report output | ⏳ Planned |
| **V0.3** | Insight Engine | Best/worst campaign detection, trend analysis, device & channel comparison, insight statements | ⏳ Planned |
| **V0.4** | Campaign Health Monitor | CPC spike detection, CTR drop alerts, conversion anomaly detection | ⏳ Planned |
| **V0.5** | Visualization Layer | Streamlit dashboard — KPI Overview, Campaign Health, Performance Trends pages | ⏳ Planned |
| **V0.6** | Budget Optimizer | Identify high-ROI campaigns, rule-based budget reallocation recommendations | ⏳ Planned |
| **V0.7** | Experimentation Lab | A/B test simulation, statistical significance, confidence intervals, Bayesian testing | ⏳ Planned |
| **V0.8** | Forecasting Engine | KPI forecasting (ARIMA, smoothing), trend decomposition, budget impact simulation | ⏳ Planned |

---

## Project Structure

```
marketing-analytics-lab/
├── data/
│   └── sample_google_ads_campaign.csv      # Sample raw Google Ads export for testing
│
├── src/
│   ├── core/
│   │   └── canonical/
│   │       └── campaign_record.py          # CampaignRecord dataclass — the canonical data model
│   │
│   ├── adapters/
│   │   ├── base.py                         # BaseCampaignAdapter — abstract adapter contract
│   │   ├── google_ads/
│   │   │   └── campaign_adapter.py         # Google Ads CSV → CampaignRecord (implemented)
│   │   └── meta_ads/
│   │       └── campaign_adapter.py         # Meta Ads → CampaignRecord (in progress)
│   │
│   ├── loaders/
│   │   └── unified_loader.py               # UnifiedLoader — source-aware entry point
│   │
│   ├── contracts/
│   │   ├── canonical_schema.py             # Pydantic CampaignRecord schema for validation
│   │   ├── google_ads_campaign_contract.py # Google Ads-specific contract (planned)
│   │   └── validator.py                    # validate_record() — returns (is_valid, errors)
│   │
│   └── validators/
│       └── csv_validator.py                # Raw CSV validation (planned)
│
├── tests/
│   ├── test_validator.py                   # Unit tests for validation logic
│   └── test_unified_loader.py              # Loader tests (planned)
│
├── test_run.py                             # End-to-end pipeline demo
└── requirements.txt
```

---

## Quickstart

```bash
# Clone the repo
git clone https://github.com/shayantimes/marketing-analytics-lab.git
cd marketing-analytics-lab

# Install dependencies
pip install -r requirements.txt

# Run the end-to-end demo
python test_run.py
```

**Example output:**

```
TOTAL RECORDS: 2
----------------------------------------
CampaignRecord(source='google_ads', date='2026-05-01', platform_campaign_id='123', campaign_name='Brand Search', impressions=10000, clicks=500, cost=250.0, conversions=20.0, revenue=1500.0)
CampaignRecord(source='google_ads', date='2026-05-02', platform_campaign_id='123', campaign_name='Brand Search', impressions=12000, clicks=600, cost=300.0, conversions=25.0, revenue=1800.0)
```

**Run tests:**

```bash
pytest tests/
```

---

## How It Works

1. `UnifiedLoader.load(source, filepath)` reads the raw CSV and routes it to the correct adapter based on the source name.
2. The **adapter** (e.g. `GoogleAdsCampaignAdapter`) maps platform-specific column names to the canonical `CampaignRecord` fields.
3. Each record is passed through the **Pydantic validation layer** — type mismatches, missing fields, and invalid values are caught here.
4. Valid records are returned as clean `CampaignRecord` objects. Invalid records return structured error reports — nothing is silently lost.
5. Every future module (KPI engine, insights, dashboards, forecasting) consumes the same canonical records — adding a new platform never breaks downstream logic.

---

## Adding a New Data Source

The adapter pattern makes adding a new platform straightforward:

```python
# 1. Create src/adapters/your_platform/campaign_adapter.py
class YourPlatformAdapter(BaseCampaignAdapter):
    def adapt(self, df: pd.DataFrame) -> list[CampaignRecord]:
        # Map your platform's columns → CampaignRecord fields
        ...

# 2. Register it in UnifiedLoader
if source == "your_platform":
    adapter = YourPlatformAdapter()
```

That's it. The rest of the pipeline — validation, KPI computation, insights, dashboards — works without any changes.

---

## Design Philosophy

- **Schema first.** Every dataset must conform to a single canonical format before any analytics happen.
- **Dirty data is expected, not an exception.** The pipeline is built to handle messy real-world exports.
- **Errors are per record, not per file.** One bad row doesn't discard the entire dataset.
- **Multi-source from day one.** The adapter pattern means adding a new platform is additive, never breaking.
- **Validation happens early.** Catching bad data at ingestion prevents contamination of every downstream layer.

---

## Why This Project Is Structured This Way

Most analytics projects start with cleaning → compute KPIs → visualize.

This project starts with **formalizing the data contract first**, then builds the ingestion pipeline on top of it, then the analytics stack.

The result is a system that is:

- **Extensible** — adding Meta Ads, Yektanet, or TikTok Ads is a single new adapter
- **Debuggable** — every invalid record comes back with a structured error report
- **Trustworthy** — no analytics run on unvalidated data
- **Production-like** — mirrors how real data engineering teams design ingestion systems

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| Data modeling | Pydantic v2 |
| Data processing | Pandas |
| Testing | Pytest |
| Dashboard *(planned)* | Streamlit |
| Forecasting *(planned)* | statsmodels / Prophet |

---

## License

MIT License
