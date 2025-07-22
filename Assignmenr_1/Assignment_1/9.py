# 9. Generate Fibonacci Series
def fibonacci_series(count):
    a, b = 0, 1
    if count <= 0:
        print("Please enter a positive number.")
    elif count == 1:
        print("Fibonacci series:", a)
    else:
        print("Fibonacci series:")
        for _ in range(count):
            print(a, end=" ")
            a, b = b, a + b

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_series(n)
