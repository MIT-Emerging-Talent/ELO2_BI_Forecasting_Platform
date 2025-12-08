# Project Overview

Purpose

Create a compact, readable overview of the forecasting and BI project so stakeholders can understand scope, approach, and deliverables.

Scope

- Data sources: Olist transactional data, Superstore sample, World Bank APIs (inflation/GDP)
- Period: 2016–2018 (as available in source files)
- Outputs: processed CSVs, visualizations, predictive models, and a Power BI dashboard

Methodology

1. ETL: clean and join transactional and macro data
2. Feature engineering: price-normalization, rolling aggregates, seasonality features
3. Modeling: gradient boosting + baseline linear models for benchmarking
4. Validation: time-series cross validation and holdout testing

Deliverables

- `1-Datasets/Processed_Data/` — processed CSVs
- `2-analysis-and-results/results/` — charts and model outputs
- `communication/presentations/` — stakeholder decks
- `communication/powerbi/` — Power BI `.pbix` file

Limitations

- GDP macro file missing currently; some economic visuals are incomplete
- Sample period limited to available data

How to contribute

- Fork the repo, create a branch, and open a pull request with tests and updated docs.