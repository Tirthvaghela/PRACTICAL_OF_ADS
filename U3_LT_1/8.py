# 8. Data:
# Name=['A','B','C','D']
# Salary=[30000,None,40000,None]
# Fill missing salary with mean.

import numpy as np
import pandas as pd

data = {
    'Name' :['A','B','C','D'],
    'Salary': [30000,None,40000,None]
}

df =pd.DataFrame(data)
print("-----DATA-----")
print(df)

print("\n-----Fill missing salary with mean-----")

print(df.fillna(df['Salary'].mean()))