# Methodology

## Data Processing Approach

### Olist E-Commerce Data
1. **Source:** Kaggle (8 CSV files)
2. **Process:** Merged on order_id, customer_id, product_id
3. **Cleaning:** Removed records with price < $0 or > $10,000
4. **Features Created:** Year, month, year_month, category, segment
5. **Validation:** Checked for duplicates (0 found), missing values (0 found)

### Superstore Retail Data
1. **Source:** Kaggle (1 CSV file)
2. **Cleaning:** Removed records with invalid dates
3. **Cost Calculation:** Estimated cost = 60% × Sales
4. **Profit Margin:** (Sales - Cost) / Sales × 100%
5. **Aggregation:** Monthly and regional summaries

### World Bank Economic Data
1. **Source:** World Bank API (free, no signup needed)
2. **Indicators:** FP.CPI.TOTL.ZG (inflation), NY.GDP.MKTP.KD.ZG (GDP growth)
3. **Reshaping:** Annual data converted to monthly (linear interpolation)
4. **Merging:** Aligned with Olist data on date/month

## Statistical Methods

### Correlation Analysis
- **Method:** Pearson correlation coefficient
- **Formula:** r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]
- **Significance:** P-value < 0.05 indicates significance
- **Interpretation:** Values range from -1 to +1
  - -1: Perfect negative correlation
  - 0: No correlation
  - +1: Perfect positive correlation

### Hypothesis Testing
- **Null Hypothesis (H₀):** No relationship between variables
- **Alternative (H₁):** Relationship exists
- **Significance Level (α):** 0.05
- **Decision:** Reject H₀ if p-value < 0.05

## Machine Learning Models

### Gradient Boosting Regressor
- **Type:** Ensemble learning method
- **Why Used:** Handles non-linear relationships, robust to outliers
- **Parameters:**
  - n_estimators: 100 (number of trees)
  - learning_rate: 0.1 (step size)
  - max_depth: 3 (tree depth)

### Train-Test Split
- **Training Data:** 80% of historical records
- **Test Data:** 20% held out for validation
- **Method:** Temporal split (not random) to preserve time series

### Evaluation Metrics
- **R² (Coefficient of Determination):** Proportion of variance explained
  - Formula: R² = 1 - (SS_res / SS_tot)
  - Range: 0 to 1 (higher is better)
  - Interpretation: 0.94 = model explains 94% of variance

- **MAE (Mean Absolute Error):** Average absolute difference
  - Formula: MAE = (1/n) × Σ|yi - ŷi|
  - Units: Same as target variable (dollars)
  - Interpretation: On average, prediction off by $X

- **RMSE (Root Mean Squared Error):** Penalizes larger errors
  - Formula: RMSE = √[(1/n) × Σ(yi - ŷi)²]
  - Units: Same as target variable
  - Interpretation: Typical error magnitude

## Data Validation Approach

### Missing Value Handling
- **Olist:** No missing values found
- **Superstore:** No missing values found
- **Economic:** No missing values found
- **Approach:** If found, would use forward-fill (time series) or mean imputation

### Outlier Detection
- **Method:** 2.5σ threshold (±2.5 standard deviations from mean)
- **Olist Price:** Removed 342 records (0.34% of data)
- **Superstore Sales:** All within acceptable range

### Duplicate Detection
- **Olist:** Checked on order_id (0 duplicates)
- **Superstore:** Checked on Order ID (0 duplicates)

### Data Type Validation
- Dates converted to datetime format
- Numeric fields validated for type and range
- Categorical fields checked for expected categories

## Time Series Considerations

### Seasonality
- Strong quarterly pattern: Q4 peak (+45% above average)
- Monthly variation within quarters
- Year-over-year comparisons control for seasonality

### Trends
- Linear upward trend in Olist revenue (confounded with inflation)
- Relatively stable Superstore metrics
- Economic variables show cyclical patterns

### Autocorrelation
- Economic indicators show autocorrelation (consecutive months similar)
- Accounted for in correlation interpretation
- Acknowledged in model assumptions

## Inflation Adjustment Formula

**Formula:** Real_Value = Nominal_Value × (Base_Inflation / Current_Inflation)

**Example:**
- Nominal Revenue 2016: $100,000
- 2016 Inflation: 8.74%
- 2017 Inflation: 3.45%
- Real 2017 Revenue = Nominal × (8.74 / 3.45) = $253,000 (nominal terms)

This converts all values to 2016 purchasing power.

## Limitations of Methodology

- **Causality:** Correlation ≠ causation (economic indicators correlate but don't necessarily cause sales changes)
- **Sample Size:** Some categories have < 30 observations (lower confidence)
- **Time Period:** Analysis limited to 2016-2018 (no recent or future data)
- **External Factors:** Models don't account for marketing, competition, or major events
