# 12. Data:
# Product=['Laptop','Mobile','Tablet','Printer']
# Price=[75000,30000,None,500000]
# Remove outlier price>3*std, fill missing with mean

import pandas as pd
import numpy as np

data = {
    'Product':['Laptop','Mobile','Tablet','Printer'],
    'Price':[75000,30000,None,500000]
}

df = pd.DataFrame(data)
df['Price'].fillna(df['Price'].mean(), inplace=True)
std_price = df['Price'].std()
mean_price = df['Price'].mean()
outlier_threshold = mean_price + 3 * std_price
df = df[df['Price'] <= outlier_threshold]
print(df)