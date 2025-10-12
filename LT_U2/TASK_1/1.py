# 1. Create a 1D NumPy array for marks obtained by 10 students.
# Options:
# a) Print the array and display dtype, shape, and size.
# b) Find the average mark and highest mark.
# c) Count how many students scored above 75.

import numpy as np

# student = np.array([])

# for n in range(1,11):
#     i = int(input("Enter Number : "))
#     student=np.append(student,i)

student = np.array([1,2,3,4,5,65,75,85,95,78])

print(student)

print("a) Print the array and display dtype, shape, and size.")

print("TYPE : ",student.dtype)
print("shape : ",student.shape)
print("size : ",student.size)

print ("b) Find the average mark and highest mark.")
print(f"Avarage marks is : {sum(student)/len(student)}")
print(f"MAX marks is : {max(student)}")

print("c) Count how many students scored above 75.")
count=0
for i in student:
    if i >= 75:
        print("MARKS : ",i)
        count+=1

print("COUNT : ",count)

