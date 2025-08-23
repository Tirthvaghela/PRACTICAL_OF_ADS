import numpy as np

# 8. Employee skill ratings (4×5)
skills = np.array([[7, 8, 9, 6, 7],
                   [6, 7, 8, 7, 6],
                   [8, 9, 7, 8, 9],
                   [7, 6, 7, 8, 7]])
print("\nAverage score per employee:", np.mean(skills, axis=1))
