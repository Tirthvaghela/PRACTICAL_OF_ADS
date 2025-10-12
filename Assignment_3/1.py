import pandas as pd
import numpy as np

# ---------------------------------------------
# 1. Create and Analyze Sales Data using Series
# ---------------------------------------------
sales = pd.Series([1500, 1800, 2100, 1900, 2500, 3000, 2800],
                  index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
print("Sales Series:\n", sales)

print("\nSales on Wednesday (label indexing):", sales['Wed'])
print("Sales on 5th day (integer indexing):", sales.iloc[4])

print("\nTotal Sales:", sales.sum())
print("Average Sales:", sales.mean())
