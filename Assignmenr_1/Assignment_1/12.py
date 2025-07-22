# 12. larger of three numbers

def larger_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

result = larger_of_three(num1, num2, num3)

print(f"The largest of the three numbers is: {result}")