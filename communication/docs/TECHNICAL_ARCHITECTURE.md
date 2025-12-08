# Technical Architecture

Overview

This document describes the data flow, components, and responsibilities for the BI & Forecasting platform.

High-level architecture

1. Raw data landing: `1-Datasets/Raw_Data/` (CSV files, API dumps)
2. ETL / Data preparation: `2-Data_preparation/process_raw_data.py` → `1-Datasets/Processed_Data/`
3. Analysis & modeling: `2-analysis-and-results/run_all_analysis.py` and Jupyter notebooks under `2-analysis-and-results/notebooks/`
4. Artifacts & results: `2-analysis-and-results/results/` (CSV + PNG outputs)
5. Communication: `communication/presentations/` and `communication/docs/`

Key components

- Python ETL (Pandas): cleans, merges, and outputs master CSVs
- Modeling: Scikit-learn for regression/forecasting models
- Visualization: Matplotlib/Seaborn (exports PNGs) + Power BI for stakeholder dashboards
- Presentation pipeline: python-pptx scripts in `tools/` for automated deck generation

Deployment & automation

- Local or cloud runner: jobs can be scheduled as a cron/Task Scheduler to run ETL + analyses nightly
- Containerization: wrap ETL and analysis in a Docker container if running in CI/CD

Data schemas & contracts

- Master dataset: `master_dataset.csv` columns include `order_id`, `order_date`, `price`, `product_category`, `country`, `inflation_rate`, `gdp_growth` (when supplied)
- Confidence: include provenance columns and timestamps to ensure reproducibility

Monitoring & alerts

- Model performance tracking (R², MAE) in a log file + alert if performance drops > 10%
- Data quality checks: missing-rate thresholds and row-count deltas

Security & access

- Keep raw data access restricted to the ETL role
- Exported dashboards distributed as PBIX or via secure share (Power BI Service)

Next steps

- Add automated ingestion for GDP and inflation sources
- Add a small REST health endpoint for job status reporting