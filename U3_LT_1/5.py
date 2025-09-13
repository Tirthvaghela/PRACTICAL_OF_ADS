import numpy as np
import pandas as pd

# 5. Data:
# Name=['Rahul','Neha','Alok','Priya']
# Age=[24,30,28,22]
# City=['Delhi','Mumbai','Delhi','Chennai']
# Filter students older than 25 living in Delhi.

data = {
	'Name':['Rahul','Neha','Alok','Priya'],
	'Age':[24,30,28,22],
	'City':['Delhi','Mumbai','Delhi','Chennai']
}

print("-----Normal Data-----")
print(data)

print("-----Full Data Frame-----")
df = pd.DataFrame(data)
print(df)
print("-------------------------")

print("-----Students Older than 25 living in Delhi-----")
filt = df[(df.Age > 25) & (df.City == 'Delhi')]
print(filt)
print("-------------------------")