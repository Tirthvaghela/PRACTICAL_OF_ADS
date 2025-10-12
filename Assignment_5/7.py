import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=50, scale=10, size=200)

sns.histplot(data, kde=True, bins=20)
plt.title("Distribution of Exam Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()