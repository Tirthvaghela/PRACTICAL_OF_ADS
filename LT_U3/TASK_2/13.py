# 13. Sales data with Region,Amount. Group by region and display avg sales.

import pandas as pd
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Amount': [100, 150, 200, 130, 170, 160]
}

df = pd.DataFrame(data)
region_avg_sales = df.groupby('Region')['Amount'].mean()
print("-----Average Sales by Region-----")
print(region_avg_sales)
print("---------------------------------")

