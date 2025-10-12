# 3. Store salaries of 6 employees in an array.
# Options:
# a) Increase salaries by 15% and display updated salaries.
# b) Find the highest and lowest salary.
# c) Calculate the mean salary.


import numpy as np

# employees = np.array([])

# for n in range(1,11):
#     i = int(input("Enter Number : "))
#     employees=np.append(employees,i)

employees = np.array([34000, 38000, 32000, 31000, 39000, 40000, 34000,42000, 34000 ,35000 ])

print("=====================================================")
print("ORIGNAL : ",employees)
print("=====================================================")

print("a) Increase salaries by 15% and display updated salaries.")
for i in range(len(employees)):
    hike = (employees[i]*15)/100
    update = employees[i]+hike
    employees[i]=update
print("UPDATED SALARY : ",employees)
print("=====================================================")

print ("b) Find the highest salary and lowest salary.")
print(f"Lowest salary is : {min(employees)}")
print(f"Highest salary is : {max(employees)}")
print("=====================================================")


print("c) Calculate the mean salary.")
print(f"Avarage MEAN is : {sum(employees)/len(employees)}")
