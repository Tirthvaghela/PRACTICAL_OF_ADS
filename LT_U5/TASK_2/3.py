import matplotlib.pyplot as plt

# Sample Data
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D'] # [cite: 21]
market_share = [300, 200, 150, 100] # [cite: 22]
explode = (0.1, 0, 0, 0)  # Explode the 'Brand A' slice 

# Create the pie chart
plt.figure(figsize=(7, 7))
plt.pie(market_share, labels=brands, autopct='%1.1f%%', startangle=90, explode=explode) # 

# Add title and ensure it's a circle
plt.title('Market Share by Brand')
plt.axis('equal')

# Show the plot
plt.show()