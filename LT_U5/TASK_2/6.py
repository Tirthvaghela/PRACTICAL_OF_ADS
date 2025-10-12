import matplotlib.pyplot as plt
import numpy as np

# Sample Data
products = ['P1', 'P2', 'P3', 'P4'] # [cite: 36]
warehouse_a_demand = [200, 300, 150, 250] # [cite: 37]
warehouse_b_demand = [180, 280, 170, 230] # [cite: 38]

# Set position of bars on X axis
x = np.arange(len(products))
width = 0.35

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, warehouse_a_demand, width, label='Warehouse A')
rects2 = ax.bar(x + width/2, warehouse_b_demand, width, label='Warehouse B')

# Add titles, labels, and legend
ax.set_ylabel('Demand (Units)')
ax.set_title('Product Demand: Warehouse A vs. B')
ax.set_xticks(x)
ax.set_xticklabels(products)
ax.legend()

# Show the plot
plt.show()