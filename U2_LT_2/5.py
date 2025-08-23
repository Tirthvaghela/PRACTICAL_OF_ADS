# 5. Create an array of annual salaries for 5 faculty members.
# Options:
# a) Add a fixed bonus of 25,000 to each salary.₹
# b) Find the faculty member with the lowest salary after bonus.
# c) Print salaries greater than 8,00,000₹ .

import numpy as np

salary= np.random.randint(10000,1100000,size=5)

print(salary)

print("=====================================================")
print("a) Add a fixed bonus of 25,000 to each salary.")

for i in range(len(salary)):
    add_bouns = salary+25000
print(add_bouns)

print("=====================================================")
print("b) Find the faculty member with the lowest salary after bonus.")
     
print(f"Lowest Salary : {min(add_bouns)}")

print("=====================================================")
print("c) Print salaries greater than 8,00,000₹ .")

count = 0
for i in range(len(salary)):
    if salary[i] > 800000:
        count+=1
print(f"Greter than 800,000₹ : {count}")
     