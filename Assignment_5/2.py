import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Books", "Toys"]
sales = [500, 700, 300, 400]
plt.bar(categories, sales, color=["blue", "green", "orange", "red"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Units Sold")
plt.show()
