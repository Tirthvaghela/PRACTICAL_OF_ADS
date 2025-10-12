import pandas as pd

# Data
data = {
    'Product': ['Pen', 'Notebook', 'Pencil'],
    'Price': [10, 50, 5]
}

df = pd.DataFrame(data)

df.to_excel('sales.xlsx', index=False)

print("File Saved.")