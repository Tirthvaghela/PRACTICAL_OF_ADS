import pandas as pd
# ---------------------------------------------
# 6. Import & Export Operations
# ---------------------------------------------
# Assuming products.xlsx exists
df_products = pd.read_excel('products.xlsx')
print("\nTop 5 Rows:\n", df_products.head())

df_products.to_csv('products.csv', index=False)
print("\nImport & Export code ready (commented as file not provided).")
