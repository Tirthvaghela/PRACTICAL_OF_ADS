# 8. Movies CSV has Movie,Rating. Filter rating>4 and export to Excel.

import pandas as pd

# Read  
df = pd.read_csv('movies.csv')
print("Columns in CSV:", df.columns.tolist())  # Debug: print column names
# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()
filtered_df = df[df['Rating'] > 4]
# Export to Excel
filtered_df.to_excel('filtered_movies.xlsx', index=False)
print("Filtered movies exported to filtered_movies.xlsx")
print("=====================================================")
print(filtered_df)
print("=====================================================")