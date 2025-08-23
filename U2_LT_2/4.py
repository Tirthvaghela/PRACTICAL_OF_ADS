# 4. Store weekly working hours of 7 employees.
# Options:
# a) Find total and average working hours.
# b) Print hours of employees who worked less than 35 hours.
# c) Increase hours by 2 for all employees.

import numpy as np

hours = np.random.randint(20, 50, size=7)  
print("Original Weekly Working Hours of 7 Employees:")
print(hours)

print("=====================================================")
print("a) Find total and average working hours.")

average_hours = np.mean(hours)


print(f"Average working hours: {average_hours:.2f}")

print("=====================================================")
print("b) Print hours of employees who worked less than 35 hours.")

less_than_35 = hours[hours < 35]
print(f"Employees who worked less than 35 hours: {less_than_35}")

print("=====================================================")
print("c) Increase hours by 2 for all employees.")

updated_hours = hours + 2
print(f"Updated Weekly Hours (+2): {updated_hours}")
