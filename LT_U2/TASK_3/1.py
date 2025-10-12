# 1. Customer Purchase Data (Random Array + Attributes)
# A retail company wants to analyze daily customer purchase counts across 7 stores for 30 days.
# • Generate a 7x30 NumPy array using random integers between 20 and 200 (inclusive).
# • Display the shape, size, number of dimensions, and data type of the array.

import numpy as np

print("=====================================================")
print("1. Customer Purchase Data")
purchase_data = np.random.randint(20, 201, size=(7, 30))
print("=====================================================")
print("Array shape:", purchase_data.shape)
print("=====================================================")
print("Array size:", purchase_data.size)
print("=====================================================")
print("Number of dimensions:", purchase_data.ndim)
print("=====================================================")
print("Data type:", purchase_data.dtype)
print("=====================================================")