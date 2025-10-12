import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
product_a_sales = [120, 150, 170, 140, 180]
product_b_sales = [80, 100, 90, 110, 130]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(months, product_a_sales, marker='o', label='Product A')
plt.plot(months, product_b_sales, marker='s', label='Product B')

# Add titles, labels, legend, and grid
plt.title('Product A vs. Product B Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()