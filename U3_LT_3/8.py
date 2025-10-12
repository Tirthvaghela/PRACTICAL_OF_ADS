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
# 8. loc and iloc
# ================================================
print("\n Employees with ID 103 to 106:\n",
      employee.loc[(employee['Employee_ID'] >= 103) & (employee['Employee_ID'] <= 106)])

print("\n First 5 rows & first 3 columns:\n", employee.iloc[:5, :3])

employee.loc[employee['Employee_ID'] == 105, 'Salary'] = 60000
print("\n Updated salary for Employee_ID 105:\n", employee[employee['Employee_ID'] == 105])