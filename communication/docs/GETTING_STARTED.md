# Getting Started (5–10 minutes)

Quick steps to run the core pipeline locally and view outputs.

1. Set up Python environment

- Recommended: Python 3.10+ (3.13 used in dev runs)
- Create a venv: `python -m venv .venv` ; `.\.venv\Scripts\Activate.ps1`
- Install packages: `pip install -r requirements.txt`

2. Run ETL

- `python 2-Data_preparation/process_raw_data.py`
- Outputs written to `1-Datasets/Processed_Data/`.

3. Run analysis

- `python 2-analysis-and-results/run_all_analysis.py`
- Results (CSV + PNG) written to `2-analysis-and-results/results/`.

4. View presentation

- Open `communication/presentations/Combined_Project_Presentation_final.pptx` in PowerPoint.

5. Open dashboard

- Open `communication/powerbi/BusinessInsights.pbix` in Power BI Desktop.

Notes

- If GDP data is missing, the Economic Context page will show gaps.
- For automated PDF export of PPTX, PowerPoint + `comtypes` are required for programmatic export.