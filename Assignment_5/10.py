import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Sample data with matching lengths
df = pd.DataFrame({
 "Category": ["Electronics", "Clothing", "Books", "Toys"] * 20,
 "Price": [200, 150, 50, 80] * 10 + [250, 180, 60, 90] * 10
})
sns.boxplot(x="Category", y="Price", data=df, palette="Set2")
plt.title("Price Spread by Category")
plt.show()