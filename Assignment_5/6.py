import matplotlib.pyplot as plt
import numpy as np

categories = ["Electronics", "Clothing", "Books", "Toys"]
store_A = [500, 700, 300, 400]
store_B = [450, 600, 350, 300]

x = np.arange(len(categories))
width = 0.35
plt.bar(x - width / 2, store_A, width, label="Store A")
plt.bar(x + width / 2, store_B, width, label="Store B")
plt.xticks(x, categories)
plt.xlabel("Category")
plt.ylabel("Sales")
plt.title("Product Category Sales Comparison")
plt.legend()
plt.show()
