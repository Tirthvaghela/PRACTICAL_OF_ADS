# 4. Product stock:
# Product=['Pen','Pencil','Book']
# Stock=[100,200,300]
# Apply 5% restock and display updated stock.

import pandas as pd

product = ['Pen', 'Pencil', 'Book']
stock = [100, 200, 300]

df = pd.DataFrame({'Product': product, 'Stock': stock})

df['Restock'] = df['Stock'] * 0.05
df['Updated_Stock'] = df['Stock'] + df['Restock']

print("=====================================================")
print(df)
print("=====================================================")