# 2. Store number of books in 6 categories.
# Options:
# a) Find the total number of books.
# b) Replace any category with less than 50 books to 50.
# c) Print books in categories 3 to 5.

import numpy as np

books= np.random.randint(10,70,size=48)

book = books.reshape(6,8)

print(book)

print("=====================================================")
print("a) Find the total number of books.")

print(f"SUM of  : {sum(books)}")

print("=====================================================")
print("b) Replace any category with less than 50 books to 50.")


for i in range(len(books)):
    if books[i] < 50:
        books[i] = 50  

print("Updated Book Matrix:")
print(books)

print("=====================================================")
print("c) Print books in categories 3 to 5.")

print("Books in Categories 3 to 5:")
print(book[2:5])