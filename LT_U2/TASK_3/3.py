# 3. Salary Data Analysis (Broadcasting + Aggregation)
# A company tracks the monthly salary (in thousands) of 5 employees for 12 months.
# • Generate a 5x12 NumPy array with random integers between 30 and 80.
# • Add a bonus of 5 (in thousands) to each employee’s monthly salary using broadcasting.
# • Find the average annual salary of each employee.
# • Find the maximum and minimum salary across all employees and months.

import numpy as np

salary_data = np.random.randint(30, 81, size=(5, 12))
salary_bonus = salary_data + 5  
average_salary = salary_bonus.mean(axis=1)
max_salary = salary_bonus.max()
min_salary = salary_bonus.min()

print("=====================================================")
print("3. Salary Data Analysis:")
print("=====================================================")
print("Salary data with bonus:\n", salary_bonus)
print("=====================================================")
print("Average annual salary of each employee:", average_salary)
print("=====================================================")
print("Max salary:", max_salary)
print("=====================================================")
print("Min salary:", min_salary)
print("=====================================================")
print()