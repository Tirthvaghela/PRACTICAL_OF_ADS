import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
product_A = [120, 150, 170, 140, 180]
product_B = [80, 100, 90, 110, 130]

plt.plot(months, product_A, marker="o", label="Product A")
plt.plot(months, product_B, marker="s", label="Product B")
plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales (Units)")
plt.legend()
plt.grid(True)
plt.show()
