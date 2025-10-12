# 6. Students:
# Name=['A','B','C']
# Math=[45,35,60]
# Science=[50,30,70]
# Filter students passed both subjects>=40

import numpy as np
import pandas as pd

Name=['A','B','C']
Math=[45,35,60]
Science=[50,30,70]

data = {
    'Name':Name,
    'Math':Math,
    'Science':Science
}

df = pd.DataFrame(data)

print("-----Full Data Frame-----")
print(df)
print("-------------------------")

print("-----Students Passed in Both Subjects (>=40)-----")
filt = df[(df.Math >= 40) & (df.Science >= 40)]
print(filt)
print("-------------------------------------------------")