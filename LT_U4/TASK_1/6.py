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

# Min, Max, and IQR
min_age = df['Age'].min()
max_age = df['Age'].max()
Q1_age = df['Age'].quantile(0.25)
Q3_age = df['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age

print(f"Min Age: {min_age}")
print(f"Max Age: {max_age}")
print(f"IQR of Age: {IQR_age}")

# Outlier Detection
lower_bound = Q1_age - 1.5 * IQR_age
upper_bound = Q3_age + 1.5 * IQR_age
outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]

print(f"\nOutlier detection bounds: ({lower_bound}, {upper_bound})")
if outliers.empty:
    print("No outliers found in the Age column.")
else:
    print("Outliers found:\n", outliers)