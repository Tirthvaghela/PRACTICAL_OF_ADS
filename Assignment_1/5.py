# 5. Simple Interest

Principle = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (Principle * rate * time) / 100
print(f"The simple interest is: {simple_interest:.2f}")
