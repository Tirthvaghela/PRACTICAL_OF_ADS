import matplotlib.pyplot as plt

# Sample Data
categories = ['Electronics', 'Clothing', 'Books', 'Toys']
sales = [500, 700, 300, 400]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold']

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, sales, color=colors)

# Add titles and labels
plt.title('Sales by Product Category')
plt.xlabel('Category')
plt.ylabel('Sales (Units)')

# Show the plot
plt.show()