# 44 Uses zip() to combine two lists into key-value pairs.

keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]

combined_dict = dict(zip(keys, values))

print(f"Keys list: {keys}")
print(f"Values list: {values}")
print(f"Combined dictionary: {combined_dict}")
