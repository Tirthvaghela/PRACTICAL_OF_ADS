# 14. Data:
# Name=['A','B','C']
# Marks=[40,60,80]
# Normalize Marks using min-max scaling between 0 and 1.

import pandas as pd

dic = {
    'Name' : ['A','B','C'],
    'Marks' : [40,60,80]
}


df = pd.DataFrame(dic)

min_val = df['Marks'].min()
max_val = df['Marks'].max()

df ['noraml marks'] = (df['Marks'] - min_val )/ (max_val  - min_val)

print(df)


