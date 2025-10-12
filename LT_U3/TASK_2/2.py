# 2. Orders:
# OrderID=[1,2,3,4]
# Amount=[200,800,600,400]
# Select OrderID,Amount where Amount>500.

import pandas as pd
order_id = [1, 2, 3, 4]
amount = [200, 800, 600, 400]
df = pd.DataFrame({'OrderID': order_id, 'Amount': amount})
filtered_df = df[df['Amount'] > 500]
print("=====================================================")
print(filtered_df)
print("=====================================================")