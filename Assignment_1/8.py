# 8. Calculate Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number to calculate its factorial: "))

print(f"The factorial of {number} is {factorial(number)}.")
