# 12. Data:
# Product=['Laptop','Mobile','Tablet','Printer']
# Price=[75000,30000,None,500000]
# Remove outlier price>3*std, fill missing with mean.

import pandas as pd

# Initial data
dic = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Printer'],
    'Price': [75000, 30000, None, 500000]
}

df = pd.DataFrame(dic)

st = df['Price'].std()

mean = df['Price'].mean()

threshold = mean + 3 * st

df = df[df['Price'].isnull() | (df['Price'] <= threshold)]

mean_cleaned = df['Price'].mean()

df['Price'] = df['Price'].fillna(mean_cleaned)

print(df)
