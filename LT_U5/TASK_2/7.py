import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generate random age data for 300 customers
np.random.seed(42) # for reproducibility
ages = np.random.randint(18, 61, size=300) # 

# Create the histogram with 10 bins
plt.figure(figsize=(8, 5))
sns.histplot(ages, bins=10, kde=True, color='teal') # 

# Add titles and labels
plt.title('Customer Age Distribution')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')

# Show the plot
plt.show()