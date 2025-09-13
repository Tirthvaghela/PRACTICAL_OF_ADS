import numpy as np
import pandas as pd

# # 1. Create a Pandas Series for monthly expenses: 
# Rent=12000, Groceries=5000, Utilities=2000,
# # Entertainment=3000. 
# Tasks: Display total and average expenses. Access Groceries using label and
# # 2nd element using index.

data = {"Rent":12000,"Groceries":5000,"Utilities":2000,"Entertainment":3000}

s_1 = pd.Series(data)
print("-----Series-----")
print(s_1)
print("----------------")

sum_of = pd.Series(sum(data.values()))
avg_of = pd.Series(sum_of/len(s_1))
print("-----Total and Average Expenses-----")
print("Total Expenses: ",sum_of.iloc[0])
print("Average Expenses: ",avg_of.iloc[0])

print("-----Accessing Series Using Label-----")
print(s_1['Groceries'])
print("----------------")

print("-----Accessing 2nd Element of Series Using Index-----")
print(s_1.iloc[1])
print("----------------")
