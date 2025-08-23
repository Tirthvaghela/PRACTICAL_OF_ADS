import numpy as np

# 13. Medicine dosages
dosages = np.array([45, 60, 30, 75, 90, 40, 55, 100])
dosages[dosages < 50] = 50
print("\nUpdated Dosages:", dosages)