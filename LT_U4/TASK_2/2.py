import pandas as pd
import numpy as np

# Create the initial DataFrame from the provided data
data = {
    'Order_ID': [201, 202, 203, 204, 205, 206, 207, 208],
    'Customer_Name': ['Raj', 'Sneha', 'Karan', 'Leela', 'John', 'Priya', 'Yusuf', 'Pooja'],
    'City': ['Mumbai', 'Delhi', 'Pune', 'Jaipur', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Age': [24, np.nan, 31, 29, 45, np.nan, 36, 27],
    'Order_Amount': [2500, 1800, np.nan, 3200, 1500, 2700, 3500, 4000],
    'Order_Date': ['2024-02-05', '2024-02-06', '2024-02-06', '2024-01-30', '2024-01-29', '2023-12-15', '2023-12-20', '2023-11-22']
}
df = pd.DataFrame(data)

# Ensure Order_Date is in datetime format
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("--- Dataset Info ---")
df.info()

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Dataset Data Types ---")
print(df.dtypes)