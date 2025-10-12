# 5. Vehicles:
# Model=['X','Y','Z']
# Price=[500000,700000,600000]
# Mileage=[15,18,20]
# Display rows sorted by Price descending

import pandas as pd

data = {'Model': ['X', 'Y', 'Z'],
        'Price': [500000, 700000, 600000],
        'Mileage': [15, 18, 20]}

df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Price', ascending=False)
print("=====================================================")
print(sorted_df)
print("=====================================================")