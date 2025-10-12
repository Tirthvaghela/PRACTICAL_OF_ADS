import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
np.random.seed(10)
data = {
    'Category': ['Electronics'] * 50 + ['Clothing'] * 50 + ['Books'] * 50 + ['Toys'] * 50,
    'Price': np.concatenate([
        np.random.normal(300, 80, 50), # Electronics prices
        np.random.normal(50, 15, 50),  # Clothing prices
        np.random.normal(20, 5, 50),   # Books prices
        np.random.normal(25, 10, 50)   # Toys prices
    ])
}
df = pd.DataFrame(data)

# Create the boxplots
plt.figure(figsize=(10, 7))
sns.boxplot(x='Category', y='Price', data=df)

# Add titles and labels
plt.title('Price Spread by Product Category')
plt.xlabel('Category')
plt.ylabel('Price (USD)')

# Show the plot
plt.show()