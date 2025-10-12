import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate dates for 12 months of 2024
dates = pd.date_range(start='2024-01-01', periods=12, freq='M') # 
# Generate sample revenue data
revenue = np.random.randint(50000, 80000, size=12)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates, revenue, marker='o', color='green')

# Add titles and labels, and rotate date labels
plt.title('Monthly Revenue Trend for 2024')
plt.xlabel('Month')
plt.ylabel('Revenue (USD)')
plt.xticks(rotation=45) # 
plt.grid(True, linestyle=':')
plt.tight_layout()

# Show the plot
plt.show()