import pandas as pd
# ---------------------------------------------
# 5. Customer Filtering by Age & City
# ---------------------------------------------
customers = pd.DataFrame({
    'Name': ['Rahul', 'Neha', 'Alok', 'Priya'],
    'Age': [24, 30, 28, 22],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Chennai']
})

print("\nCustomers with Age > 25:\n", customers[customers['Age'] > 25])
print("\nCustomers in Delhi (Name & Age):\n", customers.loc[customers['City'] == 'Delhi', ['Name', 'Age']])
