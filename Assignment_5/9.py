import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(42)
income = np.random.normal(loc=50000, scale=15000, size=100)
df = pd.DataFrame({"Income": income})
sns.boxplot(x=df["Income"])
plt.title("Income Distribution with Outliers")
plt.xlabel("Income")
plt.show()
