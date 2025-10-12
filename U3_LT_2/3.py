# 3. Assume 'sales.csv' with columns Region,Sales.
# Read CSV and display descriptive stats using describe().

import pandas as pd
df = pd.read_csv('sales.csv')
print("=====================================================")
print(df.describe())    
print("=====================================================")