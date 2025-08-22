import Q1_menu

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choice = int(input("Enter choice(1/2/3/4/5): "))
while (choice!= '5'):
   
    num1_input = int(input("Enter first number: "))
    num2_input = int(input("Enter second number: "))

    
    if choice == 1:
        print(f"{num1_input} + {num2_input} = {Q1_menu.add(num1_input, num2_input)}")
    elif choice == 2:
            print(f"{num1_input} - {num2_input} = {Q1_menu.subtract(num1_input, num2_input)}")
    elif choice == 3:
            print(f"{num1_input} * {num2_input} = {Q1_menu.multiply(num1_input, num2_input)}")
    elif choice == 4:
            print(f"{num1_input} / {num2_input} = {Q1_menu.divide(num1_input, num2_input)}")
    elif choice == 5:
            print("Exiting the program")
            break
    
    else:
        print("Invalid Input. Please enter a number from 1 to 5.")
    print("\n")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice(1/2/3/4/5): ")
     