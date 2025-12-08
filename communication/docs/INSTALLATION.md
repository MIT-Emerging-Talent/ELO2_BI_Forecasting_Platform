# Installation and Environment Setup

This file documents how to set up a reproducible Python environment for the project.

1. Install Python

- Recommended: Python 3.10–3.13

2. Create virtual environment (Windows PowerShell)

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install packages

```
pip install -r requirements.txt
```

Notes on optional packages

- `python-pptx` — used for generating PPTX files programmatically.
- `comtypes` — required only if you want programmatic PPTX→PDF export via MS PowerPoint COM automation.

System prerequisites

- For PDF export, a local installation of Microsoft PowerPoint is required (Windows).
- For large datasets, ensure you have >= 8GB RAM for reasonable performance.

Troubleshooting

- If `pip install -r requirements.txt` fails, upgrade pip: `python -m pip install --upgrade pip`.
- If package conflicts appear, create a fresh venv and reinstall.