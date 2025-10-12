import matplotlib.pyplot as plt

# Sample Data
regions = ['North', 'South', 'East', 'West'] # [cite: 15]
sales = [650, 480, 720, 550] # [cite: 16]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] # Distinct colors

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.bar(regions, sales, color=colors)

# Add titles and labels as required
plt.title("Sales by Region") # 
plt.xlabel("Region") # 
plt.ylabel("Sales (Units)") # 

# Show the plot
plt.show()