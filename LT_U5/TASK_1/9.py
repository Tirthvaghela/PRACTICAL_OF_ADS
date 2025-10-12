import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generate random salary data
np.random.seed(0)
salaries = np.random.normal(loc=60000, scale=15000, size=100)
# Add some outliers for demonstration
salaries = np.append(salaries, [120000, 135000, 5000])

# Create the boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(y=salaries)

# Add titles and labels
plt.title('Income Spread of Employees')
plt.ylabel('Salary (USD)')

# Show the plot
plt.show()