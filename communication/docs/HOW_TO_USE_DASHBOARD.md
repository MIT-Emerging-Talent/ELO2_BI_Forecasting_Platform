# How to Use the Dashboard

Overview

This guide explains how to use the `BusinessInsights.pbix` Power BI dashboard generated for the project.

Open the file

1. Install Power BI Desktop (latest stable release).
2. Open `communication/powerbi/BusinessInsights.pbix`.

Pages & purpose

1. Executive Summary — quick KPIs and trend tiles.
2. Revenue Forecasting — model outputs and forecast bands.
3. Cost & Margin Analysis — COGS, margins, and drivers.
4. Operational Metrics — fulfillment and latency metrics.
5. Customer Insights — segments and cohort behaviour.
6. Economic Context — inflation and GDP impact (GDP may be blank if file missing).

Interacting with visuals

- Date slicers: limit date ranges across pages.
- Cross-filter: click a bar or point to filter other visuals.
- Tooltips: hover to see details.
- Export: use the export data functionality from a visual to get underlying CSV.

Suggested workflows

- Weekly review: open Executive Summary, check key metrics and forecast deviations.
- Monthly planning: use Revenue Forecasting page to update targets.

Troubleshooting

- If visuals show N/A values for GDP or inflation, make sure `gdp_growth_brazil.csv` is present in `1-Datasets/Raw_Data/` and ETL is re-run.
- If measures are missing or broken, check `2-analysis-and-results/results/` for the corresponding `*.csv` files.

Contact & support

If you need changes to visuals or new measures, open an issue or contact the data engineering owner documented in `planning/STAKEHOLDERS.md`.