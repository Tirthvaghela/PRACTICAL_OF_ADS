# 8. A company has performance scores of 5 employees in 4 skills (2D array).
# Options:
# a) Calculate the mean score per employee.
# b) Find the employee with the highest overall score.
# c) Print scores of skill 2 for all employees.

import numpy as np

scores = np.array([
    [80, 85, 78, 92],  
    [88, 90, 84, 86],  
    [70, 75, 80, 85],  
    [95, 92, 88, 91],  
    [60, 65, 70, 75]   
])
print("=====================================================")
mean_scores = np.mean(scores, axis=1)
print("a) Mean score per employee:")
for i, mean in enumerate(mean_scores, start=1):
    print(f"Employee {i}: {mean:.2f}")

print("=====================================================")
total = np.sum(scores, axis=1)  
top_emp = np.argmax(total) + 1  

print(f"b) Employee {top_emp} has the highest overall score: {total[top_emp - 1]}")

print("=====================================================")
print("c) Scores of Skill 2 for all employees:")
for i, score in enumerate(scores[:, 1], start=1):
    print(f"Employee {i}: {score}")
