import numpy as np
import pandas as pd

# 2. A company records weekly sales revenue:
#  [15000, 18000, 21000, 19000].
# Tasks: Create a Series with week labels 
# ['Week1','Week2','Week3','Week4'], 
# find maximum and
# minimum revenue weeks

ar = np.array([15000, 18000, 21000, 19000])

s_2 = pd.Series(ar,index=['Week1','Week2','Week3','Week4'])

print("-----Series-----")
print(s_2)
print("----------------")

print("-----Maximum and Minimum of Series-----")
print("Maximum: ",s_2.max())
print("Minimum: ",s_2.min())
print("----------------")