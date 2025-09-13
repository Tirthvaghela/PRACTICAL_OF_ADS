import numpy as np
import pandas as pd

# 7. Data:
# Product=['Pen','Notebook','Pencil']
# Price=[10,50,5]
# Export DataFrame to Excel 'sales.xlsx'.


data = {
		'Product':['Pen','Notebook','Pencil'],
		'Price':[10,50,5]
}

df = pd.DataFrame(data)

print(df)

df.to_excel('sale.xlsx',index=False)
print("File Saved.")