# 15. Calculates the sum of first N natural numbers using a loop.
def son(n):
    if n < 1:
        return "Please enter a positive integer."
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a positive integer to calculate the sum of first N natural numbers: "))
result = son(n)