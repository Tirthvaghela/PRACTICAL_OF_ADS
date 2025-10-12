# 6. Create a 1D array showing the number of beds occupied in 7 hospital wards.
# Options:
# a) Find the ward with maximum occupancy.
# b) Replace any value below 5 with 5.
# c) Count wards with occupancy above 20

import numpy as np

hospital = np.random.randint(0, 25, size=7)  
print("hospital for 12 students (out of 30):")
print(hospital)
print("=====================================================")

print("a) Find the ward with maximum occupancy.")
print(f"Highestsalary is : {max(hospital)}")

print("=====================================================")
print("b) Replace hospital below 5 with 5.")

for i in range(len(hospital)) :
    if  hospital[i] <=5:
        hospital[i]= 5
print(hospital)

print("=====================================================")
print("c) Count wards with occupancy above 20")

count=0
for i in hospital:
    if i >= 20:
        print("wards : ",i)
        count+=1