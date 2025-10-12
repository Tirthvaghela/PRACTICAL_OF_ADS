# 10. Exam scores:
# [45,55,65,80,90]
# Find how many scored above 75.

import numpy as np

scores = np.array([45, 55, 65, 80, 90])
above_75 = scores[scores > 75]
print("Number of scores above 75:", len(above_75))
print("Scores above 75:", above_75)