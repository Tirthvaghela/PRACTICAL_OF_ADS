import pandas as pd

# 9. Data:
# Full Name=['John Smith','Alice Johnson',None,'Bob Brown']
# Split into first,last name, fill missing with 'Unknown'.

data = {
	'name':['John Smith','Alice Johnson',None,'Bob Brown']
}

df = pd.DataFrame(data)

print("-----Data Frame-----")
print(df)
print("--------------------")

df['name'] = df['name'].fillna('Unknown Unknown')

df[['first_name', 'last_name']] = df['name'].str.split(' ', n=1, expand=True)

print("-----Data Frame after splitting and replacing-----")
print(df)
print("--------------------")