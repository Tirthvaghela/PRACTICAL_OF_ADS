# 1. Create a 2D array for 5 patients (Systolic, Diastolic).
# Options:
# a) Print blood pressure of the 3rd patient.
# b) Display all diastolic readings.
# c) Replace all systolic readings below 100 with 100.

import numpy as np

patients = np.random.randint(50,120,size=10)

new = patients.reshape(5,2)

print(new)
print("=====================================================")
print("a) Print blood pressure of the 3rd patient.")

print("Display 3rd column : ",new[2:3])

print("=====================================================")
print("b) Display all diastolic readings.")

print("ALL Diastolic : \n",new[0:,1:2])

print("=====================================================")
print("c) Replace all systolic readings below 100 with 100")

for i in range(len(patients)) :
    if  patients[i] < 100:
        patients[i]= 100
print(patients)