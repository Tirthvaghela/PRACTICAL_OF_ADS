# 12. Data:
# Name=['A','B','C']
# City=['Delhi',None,'Mumbai']
# Fill missing city with Unknown, standardize lowercase.

import pandas as pd
import numpy as np

Name=['A','B','C']
City=['Delhi',None,'Mumbai']

data = {
    'Name':Name,
    'City':City
}

df = pd.DataFrame(data)
df['City'] = df['City'].fillna('Unknown').str.lower()
print("-----Data Frame after filling missing and standardizing-----")
print(df)
print("-----------------------------------------------------------")
