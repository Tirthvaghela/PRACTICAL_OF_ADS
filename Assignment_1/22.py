# 22.Uses .count() to count how many times an element appears.

fruits = ['apple', 'banana', 'cherry', 'apple', 'banana']
print(f"Original list: {fruits}")

# 1. count() - counts the occurrences of an item in the list
apple_count = fruits.count('apple')
print(f"The number of times 'apple' appears: {apple_count}")
# 2. count() for an item not in the list
banana_count = fruits.count('banana')
print(f"The number of times 'banana' appears: {banana_count}")

# 3. count() for an item not in the list
orange_count = fruits.count('orange')
print(f"The number of times 'orange' appears: {orange_count}")
