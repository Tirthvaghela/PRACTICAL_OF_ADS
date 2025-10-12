import matplotlib.pyplot as plt

categories = ["Electronics", "Clothing", "Books", "Toys"]
sales = [500, 700, 300, 400]
explode = [0, 0.1, 0, 0]  # highlight Clothing
plt.pie(sales, labels=categories, autopct="%1.1f%%", explode=explode, startangle=90)
plt.title("Category Share in Total Sales")
plt.show()
