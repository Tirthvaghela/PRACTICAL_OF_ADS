import numpy as np

# 5. Attendance of 12 students
attendance = np.array([28, 26, 30, 22, 25, 29, 18, 27, 20, 24, 30, 21])
print("\nStudents attended >25 days:", np.sum(attendance > 25))