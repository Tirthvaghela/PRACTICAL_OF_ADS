# 10. Data:
# Customer=['A','B','C','D']
# Age=[25,-5,0,40]
# Replace invalid age (<=0) with mean of valid ages.

import pandas as pd
import numpy as np

data = {
    'Customer':['A','B','C','D'],
    'Age':[25,-5,0,40]
}

df = pd.DataFrame(data)
mean_age = df[df['Age'] > 0]['Age'].mean()
df.loc[df['Age'] <= 0, 'Age'] = mean_age

print(df)
print("File Saved.")