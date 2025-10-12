import pandas as pd

# 8. Data:
# Name=['A','B','C','D']
# Salary=[30000,None,40000,None]
# Fill missing salary with mean.

data = {
	'name':['A','B','C','D'],
	'salary': [30000,None,40000,None],
}

df = pd.DataFrame(data)

print("-----Data Frame-----")
print(df)
print("--------------------")


print("-----After mean replacement data frame-----")
print(df.fillna(df['salary'].mean()))
print("--------------------")