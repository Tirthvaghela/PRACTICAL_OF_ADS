# 42 Combines two dictionaries using the update method.

dict1 = {"name": "Tirth", "age": 20}
dict2 = {"major": "Computer Science", "university": "GLS UNIVERSITY"}

print("Original dict1:", dict1)
print("Original dict2:", dict2)

# Combine dict2 into dict1
dict1.update(dict2)

print("Combined dictionary (dict1 after update):", dict1)

# Example with overlapping keys
dict3 = {"city": "Ahmedabad", "age": 21}
dict4 = {"country": "India", "city": "Gandhinagar"}

print("\nOriginal dict3:", dict3)
print("Original dict4:", dict4)

dict3.update(dict4)
print("Combined dictionary (dict3 after update with overlap):", dict3)
