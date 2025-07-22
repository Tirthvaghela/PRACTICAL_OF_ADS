#  16 A menu-driven calculator using separate functions for each operation.
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def power(a, b):
    return a ** b

def menu():
    print("Menu:")
    print("1. Multiply")
    print("2. Divide")
    print("3. Modulus")
    print("4. Power")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        print("Exiting calculator.")
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == '1':
        print("Result:", multiply(a, b))
    elif choice == '2':
        print("Result:", divide(a, b))
    elif choice == '3':
        print("Result:", modulus(a, b))
    elif choice == '4':
        print("Result:", power(a, b))
    else:
        print("Invalid choice. Please try again.")