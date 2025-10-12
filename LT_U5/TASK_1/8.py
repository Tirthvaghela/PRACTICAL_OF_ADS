import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
data = ['A', 'B', 'A', 'C', 'B', 'B', 'A', 'C', 'C', 'A']

# Create the countplot
plt.figure(figsize=(7, 5))
sns.countplot(x=data)

# Add titles and labels
plt.title('Count of Items per Category')
plt.xlabel('Category')
plt.ylabel('Count')

# Show the plot
plt.show()