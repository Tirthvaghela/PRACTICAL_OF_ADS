#  5. Store attendance (out of 30) for 12 students.
# Options:
# a) Display students who attended less than 20 days.
# b) Replace attendance below 15 with 15.
# c) Find the average attendance

import numpy as np

attendance = np.random.randint(0, 31, size=12)  
print("Attendance for 12 students (out of 30):")
print(attendance)
print("=====================================================")


print("a) Display students who attended less than 20 days.")
count=0
for i in attendance:
    if i < 20:
        print("attended less than 20 days : ",i)
        count+=1

print("=====================================================")
print("b) Replace attendance below 15 with 15.")

for i in range(len(attendance)) :
    if  attendance[i] <=15:
        attendance[i]= 15
print(attendance)
print("=====================================================")
print("c) Find the average attendance")

print(f"Avarage  is : {np.mean(attendance)}")
