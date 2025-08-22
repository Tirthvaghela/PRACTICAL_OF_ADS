import numpy as np

# 2. Number of books in 6 categories
books = np.random.randint(0, 150, size=6)
print("books for 6 categories:")
print(books)

# a) Total books
print("Total books:", sum(books))

# b) Replace categories with < 50 books to 50
books = [50 if b < 50 else b for b in books]
print("After replacing:", books)

# c) Books in categories 3 to 5
print("Categories 3 to 5:", books[2:5])
