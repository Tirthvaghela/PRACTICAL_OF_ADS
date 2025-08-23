# 4. Store weekly working hours of 7 employees.
# Options:
# a) Find total and average working hours.
# b) Print hours of employees who worked less than 35 hours.
# c) Increase hours by 2 for all employees.

import numpy as np

hours = np.random.randint(20, 50, size=(7, 4))  
print("Weekly Working Hours of 7 Employees Over 4 Weeks:")
print(hours)

print("=====================================================")
print("a) Find total and average working hours (per employee).")

# Total and average per employee
total_hours = np.sum(hours, axis=1)
average_hours = np.mean(hours, axis=1)

for i in range(7):
    print(f"Employee {i+1}: Total = {total_hours[i]} hrs, Average = {average_hours[i]:.2f} hrs/week")

print("=====================================================")
print("b) Print weekly hours of employees who worked < 35 hours in any week.")

for i in range(7):
    if np.any(hours[i] < 35):
        print(f"Employee {i+1} had weeks with <35 hours: {hours[i]}")

print("=====================================================")
print("c) Increase hours by 2 for all employees (each week).")

updated_hours = hours + 2
print("Updated Working Hours (+2 each week):")
print(updated_hours)
