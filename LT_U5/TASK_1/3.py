import matplotlib.pyplot as plt

# Sample Data
categories = ['Electronics', 'Clothing', 'Books', 'Toys']
sales = [500, 700, 300, 400]
explode = (0, 0.1, 0, 0)  # Explode the 'Clothing' slice

# Create the pie chart
plt.figure(figsize=(7, 7))
plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=140, explode=explode)

# Add title and ensure it's a circle
plt.title('Percentage Share of Sales by Category')
plt.axis('equal')

# Show the plot
plt.show()