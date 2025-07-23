# 21. Sorting a List and Finding the Second Largest Number
numbers = [5, 1, 8, 3, 2]
print(f"Original list: {numbers}")
# 1. sort() - sorts the list in ascending order
numbers.sort()
print(f"After sort(): {numbers}")

# 2. Finding the second largest number
if len(numbers) < 2:
    print("List does not have enough elements to find the second largest number.")
else:  
    second_largest = sorted(set(numbers))[-2]
    print(f"The second largest number is: {second_largest}")