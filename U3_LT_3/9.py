import pandas as pd

# Employee dataset
employee = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Jack'],
    'Age': [25, 30, 28, 40, 29, 33, 35, 31, 45, 38],
    'Department_ID': [1, 2, 3, 2, 1, 3, 2, 1, 3, 2],
    'Salary': [50000, 60000, 70000, 80000, 55000, 75000, 62000, 58000, 90000, 68000],
    'Experience_Years': [2, 5, 3, 10, 4, 7, 6, 3, 12, 8]
})

# ================================================
# 9. Joins
# ================================================

department = pd.DataFrame({
    'Department_ID': [1, 2, 3],
    'Department_Name': ['HR', 'Finance', 'IT']
})

print("\n Inner Join:\n", pd.merge(employee, department, on='Department_ID', how='inner'))

print("\n Left Join:\n", pd.merge(employee, department, on='Department_ID', how='left'))

print("\n Right Join:\n", pd.merge(employee, department, on='Department_ID', how='right'))

print("\n Full Outer Join:\n", pd.merge(employee, department, on='Department_ID', how='outer'))