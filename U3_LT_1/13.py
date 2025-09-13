# 13. Excel file employees.xlsx with Name,DOB columns.
# Convert DOB to datetime, display age in years.

import pandas as pd
from datetime import datetime

df = pd.read_excel('employees.xlsx')

df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')

today = pd.to_datetime("today")

df['Age'] = (today - df['DOB']).dt.days // 365

print(df)
