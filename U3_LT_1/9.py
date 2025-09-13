# 9. Data:
# Full Name=['John Smith','Alice Johnson',None,'Bob Brown']
# Split into first,last name, fill missing with 'Unknown'

import pandas as pd
data={
    'FullName' : ['John Smith','Alice Johnson',None,'Bob Brown']
}

df = pd.DataFrame(data)
print(df)

df['FullName'] = df['FullName'].fillna('Unknown Unknown')

df[['firstname','lastname']] = df['FullName'].str.split(" ", n=1,expand=True)

print(df)