import numpy as np

# 15. Marks Pass/Fail for 10 students
marks10 = np.array([55, 38, 67, 49, 30, 80, 72, 25, 60, 45])
result = np.where(marks10 < 40, "Fail", "Pass")
print("\nPass/Fail Result:", result)
