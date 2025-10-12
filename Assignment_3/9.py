import pandas as pd
# ---------------------------------------------
# 9. Date and Region Cleaning
# ---------------------------------------------
sales_data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-05', '2024-02-10'],
    'Sales': ['1000', '2000', '3000'],
    'Region': ['North', 'SOUTH', ' East ']
})
print("Original Sales Data:\n", sales_data.dtypes)

sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data['Sales'] = pd.to_numeric(sales_data['Sales'])
sales_data['Region'] = sales_data['Region'].str.strip().str.capitalize()

print("Data Types:\n", sales_data.dtypes)
print("\nCleaned Sales Data:\n", sales_data)