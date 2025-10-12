import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Generate random normal data for exam scores
np.random.seed(42) # for reproducibility
scores = np.random.normal(loc=75, scale=10, size=200) # Mean=75, StdDev=10

# Create the histogram
plt.figure(figsize=(8, 5))
sns.histplot(scores, bins=20, kde=True)

# Add titles and labels
plt.title('Distribution of Exam Scores')
plt.xlabel('Score')
plt.ylabel('Number of Students')

# Show the plot
plt.show()