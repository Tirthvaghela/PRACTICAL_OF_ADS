# 11. Data:
# Date=['2024-01-01','2024-02-01','2024-03-01']
# Convert Date to datetime format.

import pandas as pd

dict1 = {
    'Date':['2024-01-01','2024-02-01','2024-03-01']
}

df = pd.DataFrame(dict1)

dt = pd.to_datetime(df['Date'])

print(dt)