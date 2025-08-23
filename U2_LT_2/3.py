# 3. Generate 12 random marks between 30–100.
# Options:
# a) Print only marks above 60.
# b) Replace marks below 40 with “Fail”.
# c) Find how many marks are in the range 70–90.

import numpy as np

# marks = np.random.randint(30, 100, size=12)  
marks = [66 ,53, 46, 63 ,35 ,53 ,79 ,30 ,60 ,35 ,96 ,64]

print("Original Weekly Working marks of 12 Employees:")
print(marks)

new = np.array(marks)
print("=====================================================")
print("a) Print only marks above 60.")

count = 0
for i in range(len(marks)):
    if marks[i] > 60:
        print(marks[i])
    if marks[i] < 40:
        marks[i]="Fail"



print("=====================================================")
print("b) Replace marks below 40 with “Fail”.")
print(marks)



print("=====================================================")
print("c) Count how many marks are in the range 70–90.")
for i in range(len(new)):
    if new[i]>70 and new[i]<90:
        count+=1
print(f"Number of marks between 70 and 90: {count}")
