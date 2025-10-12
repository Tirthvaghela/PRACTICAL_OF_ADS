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

# Calculate mean and median from the original data
mean_age_fill = df['Age'].mean()
median_bill_fill = df['Total_Bill'].median()

# Fill missing values
df['Age'].fillna(mean_age_fill, inplace=True)
df['Total_Bill'].fillna(median_bill_fill, inplace=True)

print("Updated Dataset after filling missing values:")
print(df)