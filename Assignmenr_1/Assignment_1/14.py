# 14. A function that generates and prints the first n numbers of the Fibonacci series using loops.

def fibonacci_series(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci series:", a)
    else:
        print("Fibonacci series:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()  # for newline after the series

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_series(n)
