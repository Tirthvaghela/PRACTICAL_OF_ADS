# 2. Temperature Monitoring (Slicing + Reshaping + Flattening)
# A weather station records the temperature every hour for 7 days.
# • Generate a 7x24 NumPy array with random integers between 15 and 45.
# • Extract the temperature data for Day 3 (all 24 hours).
# • Extract the temperature recorded at 6 AM for all 7 days.
# • Reshape the array into a single 1D array (flatten) for quick aggregation.

import numpy as np

temperature = np.random.randint(15, 46, size=(7, 24))
print("=====================================================")
print(temperature)
print("=====================================================")
data_3 = temperature[2]  
print(f"temperature data for Day 3 (all 24 hours): {data_3}")
print("=====================================================")

ad_6h = temperature[:, 6]
print(f"Extract the temperature recorded at 6 AM for all 7 days.: {ad_6h}")
print("=====================================================")

flat_temp = temperature.flatten()
print(f"single 1D array (flatten) for quick aggregation.: {flat_temp}")
print("=====================================================")
