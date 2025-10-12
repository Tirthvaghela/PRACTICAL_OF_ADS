import pandas as pd
import numpy as np

# ==============================================================================
# --- Prepare the Dataset ---
# ==============================================================================
# This section reconstructs the dataset from the provided PDF file.
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Jack', 'Kiran', 'Lily', 'Mohan', 'Nina', 'Oscar', 'Priya', 'Quinn', 'Ravi', 'Sara', 'Tom'],
    # A value for Age is missing for Charlie.
    'Age': [25, 30, np.nan, 40, 29, 33, 35, 35, 45, 38, 31, 28, 36, 42, 34, 34, 39, 41, 27, 32],
    'Department': ['HR', 'Finance', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT', 'HR', 'Finance'],
    # Salary values are missing for Eva and Lily.
    'Salary': [50000, 60000, 70000, 80000, np.nan, 75000, 62000, 55000, 90000, 68000, 72000, np.nan, 58000, 64000, 78000, 81000, 56000, 87000, 52000, 66000],
    'Experience_Years': [2, 5, 3, 10, 3, 7, 6, 3, 12, 8, 4, 3, 3, 11, 7, 9, 4, 13, 2, 5],
    'Performance_Score': [3, 4, 5, 4, 4, 5, 4, 3, 5, 4, 4, 6, 5, 4, 5, 4, 4, 5, 2, 5],
    'Joining_Date': pd.to_datetime(['2020-01-15', '2019-03-20', '2021-07-10', '2018-05-25', '2020-09-01', '2022-01-10', '2021-03-15', '2019-06-12', '2018-11-05', '2020-12-30', '2019-08-22', '2021-09-11', '2020-04-15', '2018-03-10', '2022-07-20', '2019-10-01', '2020-06-18', '2017-05-05', '2021-11-11', '2019-12-25'])
}
df = pd.DataFrame(data)

print("="*50)
print("--- Assignment 4: Employee Data Analysis ---")
print("="*50)


# [cite_start]15. Find how many employees joined per year [cite: 181]
print("\n--- 15. Number of Employees Joined Per Year ---")
employees_per_year = df.groupby(df['Joining_Date'].dt.year)['Employee_ID'].count()
employees_per_year.index.name = 'Year'
print(employees_per_year)