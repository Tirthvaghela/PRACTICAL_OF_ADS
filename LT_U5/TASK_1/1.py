import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [120, 150, 170, 140, 180]

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', linestyle='-', color='b')

# Add titles and labels
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.grid(True) # Display grid lines

# Show the plot
plt.show()