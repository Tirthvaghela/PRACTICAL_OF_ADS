# 7. Print Multiplication Table
number = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
