# 23.Converts a list to a set to remove duplicates

def remove_duplicates(input_list):
    return list(set(input_list))

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(f"Original list: {my_list}")
print(f"unique_list after removing duplicates: {unique_list}")

