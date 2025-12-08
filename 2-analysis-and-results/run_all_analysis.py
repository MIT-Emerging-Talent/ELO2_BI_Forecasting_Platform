import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from scipy.stats import pearsonr

FILE_DIR = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(FILE_DIR, '..'))
PROCESSED_DIR = os.path.join(ROOT, '1-Datasets', 'Processed_Data')
RESULTS_DIR = os.path.join(FILE_DIR, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

print('Running consolidated analysis runner...')

# 1) Exploratory: simple plots
try:
    olist = pd.read_csv(os.path.join(PROCESSED_DIR, 'master_dataset.csv'), parse_dates=['order_purchase_timestamp'])
    superstore = pd.read_csv(os.path.join(PROCESSED_DIR, 'superstore_clean.csv'))
    try:
        econ_combined = pd.read_csv(os.path.join(PROCESSED_DIR, 'economic_indicators_combined.csv'))
    except FileNotFoundError:
        econ_combined = None

    print('Loaded datasets: olist', olist.shape, 'superstore', superstore.shape, 'economic:', econ_combined is not None)

    plt.figure(figsize=(8,4))
    plt.hist(olist['price'].dropna(), bins=50, color='teal')
    plt.title('Olist price distribution')
    plt.xlabel('Price')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, '01_exploratory_price_dist.png'), dpi=150)
    print('Saved exploratory plot')
except Exception as e:
    print('Exploratory step failed:', e)

# 2) Olist processing
try:
    master = pd.read_csv(os.path.join(PROCESSED_DIR, 'master_dataset.csv'), parse_dates=['order_purchase_timestamp'])
    before = len(master)
    master = master[(master['price'] > 0) & (master['price'] < 10000)].copy()
    after = len(master)
    master['year'] = master['order_purchase_timestamp'].dt.year
    master['month'] = master['order_purchase_timestamp'].dt.month
    master['year_month'] = master['order_purchase_timestamp'].dt.to_period('M')
    master.to_csv(os.path.join(RESULTS_DIR, 'master_dataset_cleaned.csv'), index=False)
    print(f'Olist cleaned saved ({before}->{after})')
    # category summary -- be tolerant to differing column names
    if 'product_category_name_english' in master.columns:
        category_col = 'product_category_name_english'
    elif 'product_category_name' in master.columns:
        category_col = 'product_category_name'
    else:
        # fallback to any column that contains 'category' in its name
        category_col = next((c for c in master.columns if 'category' in c.lower()), None)

    if category_col is not None:
        cat = master.groupby(category_col).agg(Orders=('order_id','nunique'), Revenue=('price','sum')).sort_values('Revenue', ascending=False)
        cat.to_csv(os.path.join(RESULTS_DIR, 'olist_category_analysis.csv'))
    else:
        print('No category column found in master dataset; skipping category summary')

    # monthly
    monthly = master.groupby('year_month').agg(order_count=('order_id','count'), revenue=('price','sum')).reset_index()
    # convert Period to timestamp for downstream consumers
    try:
        monthly['year_month'] = monthly['year_month'].dt.to_timestamp()
    except Exception:
        # if it's already a datetime/string, attempt conversion
        try:
            monthly['year_month'] = pd.to_datetime(monthly['year_month'])
        except Exception:
            pass
    # Save monthly_sales.csv as produced earlier
    monthly.to_csv(os.path.join(RESULTS_DIR, 'olist_monthly_analysis.csv'), index=False)
    print('Olist summaries saved')
except Exception as e:
    print('Olist processing failed:', e)

# 3) Superstore processing
try:
    ss = pd.read_csv(os.path.join(PROCESSED_DIR, 'superstore_clean.csv'))
    ss['Order Date'] = pd.to_datetime(ss['Order Date'], errors='coerce')
    ss['year_month'] = ss['Order Date'].dt.to_period('M')
    category = ss.groupby('Category').agg(Sales=('Sales','sum'), Profit=('Profit','sum')).reset_index()
    category.to_csv(os.path.join(RESULTS_DIR, 'superstore_category_profitability.csv'), index=False)
    region = ss.groupby('Region').agg(Sales=('Sales','sum'), Profit=('Profit','sum')).reset_index()
    region.to_csv(os.path.join(RESULTS_DIR, 'superstore_regional_analysis.csv'), index=False)
    print('Superstore summaries saved')
except Exception as e:
    print('Superstore processing failed:', e)

# 4) Economic visualizations
try:
    if econ_combined is not None:
        econ_combined['date'] = pd.to_datetime(econ_combined['date'])
        plt.figure(figsize=(8,3))
        plt.plot(econ_combined['date'], econ_combined['annual_inflation_rate'], marker='o')
        plt.title('Annual inflation rate')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(RESULTS_DIR, '04_economic_inflation.png'), dpi=150)
        econ_combined.to_csv(os.path.join(RESULTS_DIR, 'economic_indicators_summary.csv'), index=False)
        print('Economic plots & summary saved')
    else:
        print('Economic combined file not found; skipping economic visualization')
except Exception as e:
    print('Economic step failed:', e)

# 5) Forecasting (simple time-based model on monthly_sales if available)
try:
    monthly_sales_path = os.path.join(PROCESSED_DIR, 'monthly_sales.csv')
    if os.path.exists(monthly_sales_path):
        ms = pd.read_csv(monthly_sales_path, parse_dates=['year_month'])
        ms = ms.sort_values('year_month')
        ms['month_num'] = range(1, len(ms) + 1)
        X = ms[['month_num']].values
        y = ms['revenue'].values
        if len(X) >= 6:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
            model = GradientBoostingRegressor(n_estimators=50, learning_rate=0.1, max_depth=3)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            r2 = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            res = pd.DataFrame({'Model':['Revenue'],'R2_Score':[r2],'MAE':[mae],'RMSE':[rmse]})
            res.to_csv(os.path.join(RESULTS_DIR, 'forecast_results.csv'), index=False)
            print('Forecasting results saved')
        else:
            print('Not enough monthly points to train forecasting model')
    else:
        print('monthly_sales.csv not found; skipping forecasting')
except Exception as e:
    print('Forecasting failed:', e)

# 6) Correlation analysis
try:
    monthly_sales_path = os.path.join(PROCESSED_DIR, 'monthly_sales.csv')
    brazil_inflation_path = os.path.join(PROCESSED_DIR, 'brazil_inflation.csv')
    if os.path.exists(monthly_sales_path) and os.path.exists(brazil_inflation_path):
        ms = pd.read_csv(monthly_sales_path, parse_dates=['year_month'])
        bi = pd.read_csv(brazil_inflation_path, parse_dates=['date'])
        # aggregate inflation by month timestamp
        bi['year_month'] = pd.to_datetime(bi['date']).dt.to_period('M').dt.to_timestamp()
        bi_agg = bi.groupby('year_month').agg(annual_inflation_rate=('annual_inflation_rate','mean')).reset_index()
        merged = ms.merge(bi_agg, left_on='year_month', right_on='year_month', how='inner')
        if not merged.empty:
            corr, p = pearsonr(merged['revenue'], merged['annual_inflation_rate'])
            out = pd.DataFrame({'Variable Pair':['Revenue vs Inflation'],'Correlation':[corr],'P_Value':[p]})
            out.to_csv(os.path.join(RESULTS_DIR, 'correlation_analysis.csv'), index=False)
            print('Correlation analysis saved')
        else:
            print('Merged data empty: cannot compute correlations')
    else:
        print('Monthly sales or Brazil inflation not available; skipping correlation analysis')
except Exception as e:
    print('Correlation analysis failed:', e)

# 7) Business insights summary
try:
    key_metrics = []
    if os.path.exists(os.path.join(PROCESSED_DIR, 'master_dataset.csv')):
        olist_full = pd.read_csv(os.path.join(PROCESSED_DIR, 'master_dataset.csv'), parse_dates=['order_purchase_timestamp'])
        key_metrics.append(('Total Olist Orders', len(olist_full)))
        key_metrics.append(('Total Olist Revenue', olist_full['price'].sum()))
    if os.path.exists(os.path.join(PROCESSED_DIR, 'superstore_clean.csv')):
        ss = pd.read_csv(os.path.join(PROCESSED_DIR, 'superstore_clean.csv'))
        key_metrics.append(('Superstore Total Sales', ss['Sales'].sum()))
        key_metrics.append(('Superstore Total Profit', ss['Profit'].sum()))
    summary_df = pd.DataFrame(key_metrics, columns=['Metric','Value'])
    summary_df.to_csv(os.path.join(RESULTS_DIR, 'key_findings.csv'), index=False)
    print('Key findings saved')
except Exception as e:
    print('Business insights failed:', e)

print(f'Runner complete. Check {RESULTS_DIR} for outputs.')
