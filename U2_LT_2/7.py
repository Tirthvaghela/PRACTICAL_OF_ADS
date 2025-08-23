# 7. Create an array of marks for 15 students.
# Options:
# a) Replace all marks below 40 with “Fail”.
# b) Count how many students passed (marks ≥ 40).
# c) Print the top 5 marks in sorted order.

import numpy as np

# marks = np.random.randint(30, 100, size=12)  
marks = [66 ,53, 46, 63 ,35 ,53 ,79 ,30 ,60 ,35 ,96 ,64]

print("Original Weekly Working marks of 12 Employees:")
print(marks)

new = np.array(marks)

print("=====================================================")
print("a) Replace all marks below 40 with “Fail”.")

count = 0
for i in range(len(marks)):
    if marks[i] < 40:
        marks[i]="Fail"
print(marks)


print("=====================================================")
print("b) Count how many students passed (marks ≥ 40).")
for i in range(len(new)):
    if new[i] >= 40:
        count+=1
print(f"Passed Student : {count}")

print("=====================================================")
print("c) Print the top 5 marks in sorted order.")

sorttt = np.sort(new)
print(f"Sorted Marks : {sorttt}")

print(f"top 5 marks in sorted order : {sorttt[7:]}")