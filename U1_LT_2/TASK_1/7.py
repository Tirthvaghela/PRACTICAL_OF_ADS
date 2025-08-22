# 7. Create roll numbers from 101 to 116 using np.arange().
# Options:
# a) Reshape into 4×4 and print.
# b) Print the first two rows.
# c) Print the last column.

import numpy as np

roll_numbers = np.arange(101, 117)  

reshaped = roll_numbers.reshape(4, 4)
print("=====================================================")
print("a) 4×4 Reshaped Roll Numbers:")
print(reshaped)

print("=====================================================")
print("b) First two rows:")
print(reshaped[:2])

print("=====================================================")
print("c) Last column:")
print(reshaped[:, -1])
