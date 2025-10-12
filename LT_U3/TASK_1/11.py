# 11. Data:
# Date=['2024-01-01','2024-02-01','2024-03-01']
# Convert Date to datetime format.

import pandas as pd

Date = ['2024-01-01', '2024-02-01', '2024-03-01']

date_series = pd.to_datetime(Date)
print(date_series)
print("=====================================================")
print(date_series.dtype)
print("File Saved.")
