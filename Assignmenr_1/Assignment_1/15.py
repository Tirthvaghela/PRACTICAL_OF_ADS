# 15. Calculates the sum of first N natural numbers using a loop.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Please enter a positive integer."
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a positive integer to calculate the sum of first N natural numbers: "))
result = sum_of_natural_numbers(n)