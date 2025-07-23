num = input("How many numbers are in your list? ")

element = int(num)
my_list = []
valid_list = True

print("Please enter the numbers one by one.")
for i in range(element):
    elements = input(f"Enter number {i + 1}: ")
    my_list.append(int(elements))

if valid_list:        
    print(f"\nYour list is: {my_list}")

    if len(my_list) < 2:
        print("A second largest number does not exist.")
    else:
        my_list.sort(reverse=True)
        second_largest = my_list[1]
        print(f"The second largest number is: {second_largest}")