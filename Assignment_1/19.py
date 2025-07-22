# 19 This program shows set operations such as union and intersection.
print("Select operation:")
print("1. Union")
print("2. Intersection")
print("3. Exit")

choice = input("Enter choice(1/2/3): ")

if choice == '3':
    print("Exiting the program.")
elif choice in ['1', '2']:
    set1_input = input("Enter elements of the first set separated by space: ").split()
    set2_input = input("Enter elements of the second set separated by space: ").split()
    
    set1 = set(set1_input)
    set2 = set(set2_input)

    if choice == '1':
        result = set1.union(set2)
        print(f"\nUnion: {result}")
    elif choice == '2':
        result = set1.intersection(set2)
        print(f"\nIntersection: {result}")
else:
    print("Invalid Input. Please enter a number from 1 to 3.")