# 11. Prices stored as strings:
# ['100','200','300']
# Convert to numeric

import pandas as pd
import numpy as np

prices = ['100', '200', '300']
price_series = pd.to_numeric(prices)

print(price_series)

# Check datatype
print("=====================================================")  
print(price_series.dtype)
print("=====================================================")