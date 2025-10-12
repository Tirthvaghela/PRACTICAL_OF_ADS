import pandas as pd
# ---------------------------------------------
# 4. DataFrame Creation from Real Data
# ---------------------------------------------
data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Priya', 'Karan'],
    'Age': [25, 28, 30, 26, 29],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
}

df = pd.DataFrame(data)
print("\nFirst 3 rows:\n", df.head(3))
print("Shape of DataFrame:", df.shape)
print("Data Types:\n", df.dtypes)
