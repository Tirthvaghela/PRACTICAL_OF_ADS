# 14. Data:
# Name=['A','B','C']
# Marks=[40,60,80]
# Normalize Marks using min-max scaling between 0 and 1.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {'Name': ['A', 'B', 'C'], 'Marks': [40, 60, 80]}
df = pd.DataFrame(data)

scaler = MinMaxScaler()
df['Normalized_Marks'] = scaler.fit_transform(df[['Marks']])

print(df)