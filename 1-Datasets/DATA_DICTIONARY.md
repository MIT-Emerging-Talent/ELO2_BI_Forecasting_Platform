# Data Dictionary

## master_dataset (Olist)

- order_id: Unique order identifier
- customer_id: Customer identifier
- order_status: Status (delivered, shipped, etc.)
- order_purchase_timestamp: Purchase date/time
- order_delivered_customer_date: Delivery date
- price: Order price
- shipping_cost: Shipping cost
- product_category_name_english: Product category

## superstore_clean (Retail)

- Order ID: Unique order ID
- Order Date: Purchase date
- Sales: Revenue amount
- Quantity: Units sold
- Discount: Discount percentage
- Profit: Profit amount
- Cost: Calculated cost
- Profit_Margin_Pct: Profit margin %
- Region: Geographic region
- Category: Product category

## economic_indicators_combined (World Bank)

- date: Date (monthly)
- annual_inflation_rate: Yearly inflation %
- annual_gdp_growth: Yearly GDP growth %
- economic_health: Calculated health score
- economic_status: Status (Strong/Moderate/Weak)

---

## analysis-and-results (overview)

Purpose

Store all analysis files, notebooks, and findings.

Contents

### Python Analysis (analysis/notebooks/)

```bash
analysis/notebooks/
├── 01_exploratory_analysis.ipynb
├── 02_olist_processing.ipynb
├── 03_superstore_processing.ipynb
├── 04_economic_indicators.ipynb
├── 05_forecasting_models.ipynb
├── 06_correlation_analysis.ipynb
└── 07_business_insights.ipynb
```

### Analysis Results (analysis/results/)

```bash
analysis/results/
├── key_findings.md (Top 10 insights)
├── correlation_analysis.csv (Statistical correlations)
├── forecast_results.csv (Model predictions)
├── scenario_analysis.csv (Economic scenarios)
├── category_resilience.csv (Category performance)
└── revenue_decomposition.csv (Real vs nominal growth)
```

### Documentation (analysis/docs/)

```bash
analysis/docs/
├── README.md (Analysis overview)
├── methodology.md (Statistical methods)
├── model_performance.md (ML model details)
├── data_quality_report.md (Validation results)
└── limitations.md (Constraints and assumptions)
```

---

## Key Findings Summary (example)

### 1. Inflation Impact on Consumer Behavior

- 2016: 8.74% inflation → 18% reduction in order frequency
- Customers shifted to larger order values (stockpiling)
- Revenue remained stable despite lower transaction count

### 2. Economic Cycle Correlation

- Sales volume: -0.42 correlation with inflation
- GDP growth: +0.68 correlation with sales
- Economic health score predicts revenue within 92% accuracy

### 3. Category Resilience

- Essential categories (Household): Recession-proof (↑5% during downturn)
- Discretionary (Electronics): High sensitivity (-23% during recession)
- Strategy: Shift mix during contraction periods

### 4. Real vs Nominal Growth

- Nominal growth 2016-2018: +15%
- Real (inflation-adjusted) growth: +6%
- GDP-adjusted: +4.2%
- Implication: Actual business growth slower than headline figures

### 5. Margin Protection Strategy

- High inflation pricing: +4.2% margin improvement vs cost increases
- Cost control during growth: -2.1% cost ratio while scaling
- Balanced approach more effective than aggressive discounting

### 6. Forecasting Accuracy

- Revenue model: R² = 0.94, MAE = $12,500
- Cost model: R² = 0.92, MAE = $8,200
- Margin model: R² = 0.87, RMSE = 2.1%

### 7. Customer Behavior Patterns

- Q4 peak: +45% above average
- Inflation-sensitive categories show -0.3 correlation
- Premium segment: Counter-cyclical (grows during inflation)

### 8. Operational Efficiency

- Shipping cost per unit: -8% improvement with automation
- Average delivery time: Reduced from 12 to 9 days
- Cost as % of sales: Declined 2.1% year-over-year

### 9. Geographic Insights

- Regional disparities: Up to 3x difference in margin
- Urban centers: Higher inflation impact but larger volume
- Rural: Stable growth but lower margins

### 10. Strategic Recommendations

- Develop recession-proof product mix (40% essential, 60% discretionary)
- Implement dynamic pricing tied to economic indicators
- Build cash reserves during high-inflation periods
- Focus on cost control during GDP growth phases

---

## Communication & Presentation (overview)

### Presentations (communication/presentations/)

```bash
communication/presentations/
├── Project_Showcase_Presentation.pptx (Main deck)
├── Executive_Summary.pdf (1-page summary)
├── Technical_Deep_Dive.pptx (For technical audience)
└── Business_Impact_Report.pdf (For stakeholders)
```

### Power BI Dashboard (communication/powerbi/)

```bash
communication/powerbi/
├── BusinessInsights.pbix (Main dashboard file)
├── Dashboard_Screenshot_Page1_Executive.png
├── Dashboard_Screenshot_Page2_Revenue.png
├── Dashboard_Screenshot_Page3_Cost.png
├── Dashboard_Screenshot_Page4_Operations.png
├── Dashboard_Screenshot_Page5_Customer.png
└── Dashboard_Screenshot_Page6_Economic.png
```

### Documentation (communication/docs/)

```bash
communication/docs/
├── PROJECT_OVERVIEW.md (High-level summary)
├── HOW_TO_USE_DASHBOARD.md (User guide)
├── TECHNICAL_ARCHITECTURE.md (System design)
├── DATA_SOURCES.md (Data provenance)
└── GLOSSARY.md (Term definitions)
```

---

## Planning (overview)

```bash
planning/
├── PROJECT_PLAN.md (Scope, timeline, deliverables)
├── REQUIREMENTS.md (Functional requirements)
├── TIMELINE.md (Milestones and dates)
├── DECISION_LOG.md (Key decisions made)
├── RISK_REGISTER.md (Identified risks)
├── RETROSPECTIVE.md (Lessons learned - see section 4)
└── CONSTRAINTS.md (Limitations and assumptions)
```

---

## Notes on repo organization & size

- Keep raw data under `data/raw/` and processed outputs under `data/processed/`.
- Use Git LFS for large CSVs if storing them in the repo.
- Document regeneration steps in README files so processed data can be reproduced from raw sources and scripts.
