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
# 4. str Accessor
# ================================================
print("\n Names starting with 'A' or 'D':\n",
      employee[employee['Name'].str.startswith(('A', 'D'))])

print("\n Names containing letter 'a' (case-insensitive):\n",
      employee[employee['Name'].str.contains('a', case=False)])