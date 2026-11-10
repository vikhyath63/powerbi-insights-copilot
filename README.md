# Power BI Insights Copilot (Local Demo)

A lightweight analytics copilot API over sample sales data. It supports filter-aware summaries, KPI aggregation and explainable insight generation. The API is designed as a backend building block for an embedded Power BI chat interface; it does not require or impersonate a Power BI tenant.

## Run
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
POST /insights with optional region, product and status filters. No credentials required.
