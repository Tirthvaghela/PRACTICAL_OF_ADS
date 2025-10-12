# 2. Create an array of body temperatures (in °C) of 8 patients.
# Options:
# a) Display the minimum and maximum temperature.
# b) Find the number of patients with temperature above 37.5°C.
# c) Change all temperatures above 39°C to 39°C.


import numpy as np

# patients = np.array([])

# for n in range(1,11):
#     i = int(input("Enter Number : "))
#     patients=np.append(patients,i)

patients = np.array([34.5 , 38.4 , 32.9 , 31.4 , 39.9 , 40.1 , 34.9 ,42.0 , 34.1 ,35.0 ])

print(patients)


print ("a) Display the minimum and maximum temperature.")
print(f"MIN temperature is : {min(patients)}")
print(f"MAX temperature is : {max(patients)}")


print("b) Find the number of patients with temperature above 37.5°C.")
count=0
for i in patients:
    if i >= 37.5:
        print("Above 37.5 temperature: ",i)
        count+=1

print("COUNT : ",count)


print("c) Change all temperatures above 39°C to -2.")
for i in range(len(patients)) :
    if  patients[i] >=39:
        patients[i]=-2
print(patients)


