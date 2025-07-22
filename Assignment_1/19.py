# 19 This program shows set operations such as union and intersection.
import maths   
print("Select operation:")
print("1. Union")
print("2. Intersection")
print("3. Exit")

choice = input("Enter choice(1/2/3): ")
if choice == '3':
    print("Exiting the program")
else:  
    set1 = set(input("Enter elements of first set separated by space: ").split())
    set2 = set(input("Enter elements of second set separated by space: ").split())

    if choice == '1':
        result = maths.union(set1, set2)
        print(f"Union of {set1} and {set2} is: {result}")
    elif choice == '2':
        result = maths.intersection(set1, set2)
        print(f"Intersection of {set1} and {set2} is: {result}")
    else:
        print("Invalid Input. Please enter a number from 1 to 3.")
