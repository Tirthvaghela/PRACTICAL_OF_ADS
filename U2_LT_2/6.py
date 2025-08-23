# 6. Create an array for medicine dosages (in mg) for 10 patients.
# Options:
# a) Find the average dosage.
# b) Replace all dosages below 50mg with 50mg.
# c) Print dosages for patients 3 to 7.

import numpy as np

dosages = [45, 60, 30, 80, 55, 70, 25, 90, 50, 65]

print("=====================================================")
print("a) Find the average dosage.")

average = sum(dosages) / len(dosages)
print(f"Average dosage: {average} mg")

print("=====================================================")
print("b) Replace all dosages below 50mg with 50mg.")
for i in range(len(dosages)):
    if dosages[i] < 50:
        dosages[i] = 50

print("Updated dosages (with minimum 50mg):", dosages)

print("=====================================================")
print("c) Print dosages for patients 3 to 7.")

print("Dosages for patients 3 to 7:", dosages[2:7])