# 1. City population:
# City=['Mumbai','Delhi','Pune','Mysore']
# Population=[20000000,19000000,5000000,800000]
# Filter cities with population>1 million OR name starts with M.

import pandas as pd

city = ['Mumbai', 'Delhi', 'Pune', 'Mysore']
population = [20000000, 19000000, 5000000, 800000]

df = pd.DataFrame({'City': city, 'Population': population})   

filtered_df = df[(df['Population'] > 1000000) | (df['City'].str.startswith('M'))]
print("=====================================================")
print(filtered_df)
print("=====================================================")