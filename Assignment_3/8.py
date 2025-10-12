import pandas as pd
import numpy as np

products = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Printer'],
    'Price': [75000, 30000, np.nan, 500000],
    'Stock': [10, np.nan, 30, 15]
})

# Fill missing data
mean_price = products['Price'].mean(skipna=True)
median_stock = products['Stock'].median(skipna=True)

# ✅ Safe assignment (no inplace warning)
products['Price'] = products['Price'].fillna(mean_price)
products['Stock'] = products['Stock'].fillna(median_stock)

# Remove outlier (price > mean + 3*std)
threshold = products['Price'].mean() + 3 * products['Price'].std()
products = products[products['Price'] <= threshold]

print("Cleaned Product Data:\n", products)
