# 10. Data:
# Customer=['A','B','C','D']
# Age=[25,-5,0,40]
# Replace invalid age (<=0) with mean of valid ages.

import pandas as pd

dic = {
    'Customer' :['A','B','C','D'],
    'Age':[25,-5,0,40]
}

df = pd.DataFrame(dic)


valid_mean = df.loc[df['Age']>0 ,'Age'].mean()

df.loc[df['Age']<=0 ,'Age'] = valid_mean

print(df)