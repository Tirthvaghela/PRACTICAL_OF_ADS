import numpy as np

# 7. Publications by 4 faculty over 3 years
publications = np.array([[2, 3, 4], [1, 5, 2], [3, 2, 6], [4, 3, 5]])
print("\nTotal Publications per Faculty:", np.sum(publications, axis=1))