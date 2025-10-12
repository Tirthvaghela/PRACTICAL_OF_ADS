import matplotlib.pyplot as plt
import numpy as np

# Sample Data
categories = ['Electronics', 'Clothing', 'Books', 'Toys']
store_a_sales = [500, 700, 300, 400]
store_b_sales = [450, 600, 350, 300]

# Set position of bar on X axis
x = np.arange(len(categories))
width = 0.35

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, store_a_sales, width, label='Store A')
rects2 = ax.bar(x + width/2, store_b_sales, width, label='Store B')

# Add titles, labels, and legend
ax.set_ylabel('Sales (Units)')
ax.set_title('Store A vs. Store B Sales by Category')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Show the plot
plt.show()