# 13. Uses a function and string slicing to check if the input word is a palindrome.

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input("Enter a word to check if it is a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
