import numpy as np

# 10. Beds occupied in 7 wards
beds = np.array([35, 40, 25, 50, 45, 30, 55])
print("\nWard with Maximum Occupancy:", np.argmax(beds) + 1)