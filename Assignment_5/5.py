import matplotlib.pyplot as plt
import pandas as pd

dates = pd.date_range(start="2023-01-01", periods=12, freq="M")
sales = [100, 120, 130, 140, 150, 160, 155, 165, 175, 180, 190, 200]

plt.plot(dates, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
