import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate dates for 12 months of 2023
dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
sales = np.random.randint(100, 250, size=12) # Sample sales data

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dates, sales, marker='o')

# Add titles and labels, and rotate date labels
plt.title('Monthly Sales Trend for 2023')
plt.xlabel('Date')
plt.ylabel('Sales (Units)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout() # Adjust layout to prevent labels from overlapping

# Show the plot
plt.show()