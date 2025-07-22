# 20. List Operations: Append, Insert, Remove, and Pop
fruits = ['apple', 'banana', 'cherry']
print(f"Original list: {fruits}")
# 1. append() - adds an item to the end
fruits.append('orange')
print(f"After append('orange'): {fruits}")

# 2. insert() - adds an item at a specified index
fruits.insert(1, 'blueberry')
print(f"After insert(1, 'blueberry'): {fruits}")

# 3. remove() - removes the first occurrence of an item
fruits.remove('cherry')
print(f"After remove('cherry'): {fruits}")

# 4. pop() - removes the item at a specified index (or the last item if not specified)
popped_fruit = fruits.pop(2)
print(f"After pop(2): {fruits}, Popped item: {popped_fruit}")