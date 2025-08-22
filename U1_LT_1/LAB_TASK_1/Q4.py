num_str = input("How many numbers are in your list? ")

num_elements = int(num_str)
my_list = []
valid_list = True

print("Please enter the numbers one by one.")
for i in range(num_elements):
        num_elements = input(f"Enter number {i + 1}: ")
        my_list.append(int(num_elements))

if valid_list:
    unique_list = []

    for item in my_list:
          if item not in unique_list:
            unique_list.append(item)

print(f"\nOriginal List: {my_list}")
print(f"List with Duplicates Removed: {unique_list}")