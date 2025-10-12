import pandas as pd
import numpy as np

# Create the initial DataFrame
data = {
    'Customer_ID': [1, 2, 3, 4, 5, 6, 7],
    'Name': ['Arjun', 'Beena', 'Chetan', 'Diya', 'Esha', 'Farhan', 'Gita'],
    'Age': [22, 34, np.nan, 41, 26, 29, np.nan],
    'Total_Bill': [1200, 800, 1600, np.nan, 1300, 1400, 1100],
    'Purchase_Date': ['2024-01-12', '2024-01-14', '2024-01-16', '2024-01-17', '2024-01-19', '2023-12-22', '2023-12-25']
}
df = pd.DataFrame(data)

# Ensure Purchase_Date is in datetime format for later tasks
df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])

print("--- Dataset Info ---")
print(df.info())

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Dataset Data Types ---")
print(df.dtypes)