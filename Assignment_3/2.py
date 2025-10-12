import pandas as pd
# ---------------------------------------------
# 2. Employee Salary Operations
# ---------------------------------------------
salaries = pd.Series([30000, 45000, 50000, 35000], index=['E1', 'E2', 'E3', 'E4'])
print("Employee Salaries:\n", salaries)

bonus_salaries = salaries * 1.10
print("\nUpdated Salaries with Bonus:\n", bonus_salaries)
print("Salary of E2:", bonus_salaries['E2'])
print("Salary of E4:", bonus_salaries['E4'])
