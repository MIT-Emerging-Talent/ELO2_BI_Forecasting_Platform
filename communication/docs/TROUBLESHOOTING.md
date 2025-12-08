# Troubleshooting

Common issues and how to resolve them.

1. Missing GDP or inflation data

- Symptom: Economic Context visuals are empty or show N/A
- Fix: Place `gdp_growth_brazil.csv` and/or `inflation.csv` into `1-Datasets/Raw_Data/` and re-run `python 2-Data_preparation/process_raw_data.py`.

2. Programmatic PPTX→PDF export fails

- Symptom: `No module named 'comtypes'` or COM errors
- Fix: `pip install comtypes` and ensure PowerPoint is installed and licensed on the machine. Alternatively, open the PPTX and Save As → PDF manually.

3. Analysis runner errors or missing columns

- Symptom: KeyError `product_category_name_english` or similar
- Fix: Inspect `1-Datasets/Processed_Data/master_dataset.csv` for the correct column name and update `2-analysis-and-results/run_all_analysis.py` accordingly.

4. Notebook execution fails with nbconvert errors

- Symptom: Running notebooks directly fails due to environment or kernel mismatch
- Fix: Use the consolidated runner `python 2-analysis-and-results/run_all_analysis.py` which replicates the notebook logic.

5. Presentation images not appearing

- Symptom: Slides missing images
- Fix: Ensure PNG images exist in `2-analysis-and-results/results/` and re-run `tools/insert_images_into_pptx.py` with correct paths and slide numbers.

If problems persist

Open an issue in the repository describing the steps to reproduce and include console output and the versions of Python and major packages.