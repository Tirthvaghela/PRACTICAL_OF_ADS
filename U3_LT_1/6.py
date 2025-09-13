import numpy as np
import pandas as pd

# 6. Assume 'products.csv' has columns Product,Price,Stock. 
# Read CSV, display shape, top 5 rows
# and dtypes.

df = pd.read_csv('products.csv')

print("-----Full Data Frame-----")
print(df)
print("-------------------------")

print("-----CSV Shape-----")
print("Shape: ",df.shape)
print("-------------------------")


print("-----First 5 Rows from Data Frame-----")
print(df[:5])
print("-------------------------")

print("-----Data type-----")
print("Data Type: ",df.dtypes)
print("-------------------------")