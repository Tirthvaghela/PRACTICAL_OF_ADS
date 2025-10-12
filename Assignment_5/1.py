import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 170, 140, 180]
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales (Units)")
plt.grid(True)
plt.show()
