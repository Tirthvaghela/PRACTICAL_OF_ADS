num_entries = int(input("How many entries do you want to add to the dictionary? "))

user_dict = {}
for _ in range(num_entries):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    user_dict[key] = value

print("Dictionary:", user_dict)