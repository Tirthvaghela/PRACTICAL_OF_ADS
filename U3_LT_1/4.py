import numpy as np
import pandas as pd

# 4. Create DataFrame for students:
# Name=['Amit','Riya','John','Meena','Sam','Alok']
# Age=[15,16,15,17,14,16]
# Grade=['A','B','A','A','C','B']
# Display top 4 rows and bottom 2 rows.

data = {'Name':['Amit','Riya','John','Meena','Sam','Alok'],
'Age':[15,16,15,17,14,16],
'Grade':['A','B','A','A','C','B']}

print("-----Normal Data-----")
print(data)

print("-----Full Data Frame-----")
df = pd.DataFrame(data)
print(df)
print("-------------------------")

print("-----Top 4 Rows of Data Frame-----")
df = pd.DataFrame(data)
print(df.iloc[:4])
print("-------------------------")

# slicing can be done without using iloc operator
# but since it is dataframe, we use iloc function

print("-----Bottom 2 Rows of Data Frame-----")
df = pd.DataFrame(data)
print(df.iloc[4:])
print("-------------------------")
