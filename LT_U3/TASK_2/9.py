# 9. Employees:
# Name=['A','B','A']
# Dept=['HR','IT','HR']
# Remove duplicates.

import pandas as pd
import numpy as np

Name=['A','B','A']
Dept=['HR','IT','HR']

data = {
    'Name':Name,    
    'Dept':Dept
}   

df = pd.DataFrame(data)
print("-----Full Data Frame-----")
print(df)

print("-------------------------")
print("-----After Removing Duplicates-----")
print(df.drop_duplicates())
print("------------------------------------")