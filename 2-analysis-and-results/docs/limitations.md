# Limitations & Assumptions

## Data Limitations

### Temporal Limitations
- **Olist Data:** Only 2016-2018 (historical snapshot)
  - Cannot predict beyond this period without assumptions
  - Market may have changed significantly since 2018
  - No recent COVID-19 impact data

- **Superstore Data:** Only 2014-2017 (4 years)
  - Older than Olist data
  - Different industry (retail vs e-commerce)
  - Different economic context (pre-COVID)

- **Economic Data:** Annual granularity
  - Converted to monthly via linear interpolation
  - May not capture intra-month variation
  - Lagged official statistics

### Geographic Limitations
- **Olist:** Brazil-only
  - Cannot generalize to other countries
  - Brazil had unique economic conditions (2016 recession)
  - Currency effects not captured (Real to USD)

- **Superstore:** US-only
  - Different inflation dynamics
  - Different consumer behavior
  - Different industry structure

### Scope Limitations
- **No Customer Demographics**
  - Unknown age, income, education of customers
  - Cannot segment by socioeconomic factors
  - Geographic only at state level

- **No Marketing Data**
  - Unknown advertising spend
  - Unknown promotional activities
  - Unknown campaign effectiveness

- **No Competitive Data**
  - Unknown competitor actions
  - Unknown market share
  - Unknown competitive pricing

- **No Product-Level Data**
  - Cannot analyze specific product performance
  - Unknown supplier information
  - Unknown product lifecycle stage

---

## Statistical Limitations

### Sample Size Issues
- **Small Categories:** Some product categories have < 30 observations
  - Statistical power reduced
  - Confidence intervals wider
  - Requires caution in interpretation

- **Time Series:** 36 months may be short for trend detection
  - Business cycles take years to complete
  - Long-term trends unclear
  - Forecasting confidence limited for long horizon

- **Regional Data:** Unequal distribution
  - Some regions have 10x more data than others
  - Regional models may be unstable
  - Aggregation recommended

### Correlation ≠ Causation
- **Revenue-Inflation Correlation:** -0.42
  - Indicates relationship but not causation
  - Other variables may drive both
  - Cannot conclude inflation causes sales decline

- **Revenue-GDP Correlation:** +0.68
  - Moderate relationship
  - Causality direction unclear
  - May be confounded by other factors

### Missing Confounding Variables
- **Omitted Variables Bias:** Unknown factors affecting sales
  - Competitor actions
  - Marketing campaigns
  - Seasonal events (holidays, etc.)
  - Product innovations
  - Supply chain disruptions

### Statistical Test Limitations
- **P-values:** Do not indicate effect size
  - Statistical significance ≠ practical significance
  - Large sample can make small effects significant
  - Small sample can hide large effects

---

## Model Limitations

### Assumptions Made
1. **Linear Relationships:** Models assume patterns continue
2. **Stationarity:** Inflation/GDP relationships stable over time
3. **Independence:** Observations assumed independent (may be autocorrelated)
4. **Normality:** Errors assumed normally distributed (may be skewed)

### Training Data Limitations
- **Overfitting Risk:** Model may memorize training data
  - Test set accuracy (92%) < Training accuracy (94%)
  - Generalization to new data uncertain

- **Temporal Structure:** Models trained on sequential data
  - Cannot randomly shuffle (would break time series)
  - Less data for validation than random splits would allow

### Model Scope
- **Black Box:** Gradient Boosting difficult to interpret
  - Cannot easily explain individual predictions
  - Feature importance approximate
  - Predictions not human-auditable

- **No Uncertainty Quantification:** True
  - Confidence intervals are approximations
  - May be wider/narrower than stated
  - Recommend sensitivity analysis

---

## External Limitations

### Regulatory Changes
- **Inflation Measurement:** CPI methodology changes over time
  - Changes in what's included
  - Weighting changes
  - Base year shifts
  - May affect comparisons

- **Tax Changes:** VAT/Sales tax not factored
  - Could significantly impact margins
  - Regional variation not captured

### Economic Shocks
**Not Captured in Models:**
- Pandemics (COVID-19)
- Wars or major geopolitical events
- Financial crises
- Natural disasters
- Supply chain disruptions
- Currency crises

### Market Changes
- **Consumer Behavior Shift:** Preferences may change
  - E-commerce adoption accelerating
  - Shift to sustainable products
  - Direct-to-consumer trends
  - Subscription models emerging

- **Technology Disruption:** New competitors or business models
  - Marketplaces disrupting traditional retail
  - AI changing customer service
  - Logistics technology improving
  - Payment methods changing

---

## Methodological Limitations

### Data Transformation Issues
- **Inflation Adjustment:** Uses annual rate applied to monthly data
  - May not reflect actual month-to-month inflation
  - Assumes linear intra-year inflation
  - Over-simplifies complex pricing

- **Linear Interpolation:** Used to convert annual to monthly
  - Assumes uniform distribution
  - Doesn't capture actual monthly variation
  - May smooth out important patterns

### Missing Validation Techniques
- **Cross-Validation:** Not used due to time series nature
- **Walk-Forward Validation:** Could improve confidence
- **Backtesting:** Real-world testing not done
- **Sensitivity Analysis:** Parameter changes not tested

### Measurement Error
- **Category Misclassification:** Some products may be miscategorized
- **Price Errors:** Data entry errors in raw data
- **Date Errors:** Some delivery dates missing/incorrect
- **Unknown Measurement Error:** Systematic bias unknown

---

## Disclosure & Recommendations

### What This Analysis Can Do ✅
- Identify patterns and trends in historical data
- Provide descriptive statistics and summaries
- Build forecasting models for strategic planning
- Assess relationships between economic and business variables
- Support hypothesis testing and exploration

### What This Analysis Cannot Do ❌
- Predict specific future events with certainty
- Account for unprecedented changes
- Replace domain expertise and judgment
- Guarantee decision outcomes
- Predict individual transaction-level behavior

### Recommended Safeguards

**For Forecasting:**
- Use as guidance, not gospel truth
- Apply judgment and domain expertise
- Update forecasts monthly with new data
- Monitor actual vs predicted closely
- Adjust if variance exceeds ±15%

**For Decision-Making:**
- Consider multiple scenarios (pessimistic, realistic, optimistic)
- Test decisions under different assumptions
- Build in contingency plans
- Monitor leading indicators
- Be prepared to pivot if assumptions change

**For Communication:**
- Always state assumptions explicitly
- Include confidence intervals
- Explain limitations to stakeholders
- Avoid false precision
- Update stakeholders when conditions change

---

## Future Improvements

### High Priority
1. Incorporate real-time sales data
2. Add external market data (competitors, market size)
3. Implement automated model retraining
4. Build customer lifetime value models
5. Create hierarchical forecasts by region/category

### Medium Priority
1. Upgrade to ARIMA for better time-series handling
2. Add sentiment analysis from customer reviews
3. Implement causal inference models
4. Build anomaly detection system
5. Create what-if scenario engines

### Long-term
1. Move to real-time streaming architecture
2. Implement machine learning operations (MLOps)
3. Build prescriptive (not just predictive) models
4. Create automated decision systems
5. Develop reinforcement learning for optimization

---

## Conclusion

These limitations should be considered when interpreting results and making decisions.
The analysis is statistically sound and methodologically rigorous within its scope.
With proper caveats and safeguards, the insights are valuable for strategic planning.

**Recommendation:** Use this analysis as a starting point for deeper investigation,
not as the final word on future performance.

**Recommendation:** Use this analysis as a starting point for deeper investigation,
not as the final word on future performance.
