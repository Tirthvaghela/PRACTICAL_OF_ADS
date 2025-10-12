import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({"Category": ["A", "B", "A", "C", "B", "B", "A", "C", "C", "A"]})

sns.countplot(x="Category", data=df, palette="pastel")
plt.title("Count of Items per Category")
plt.show()
