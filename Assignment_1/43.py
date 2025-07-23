# 43 Builds a word frequency counter using a dictionary.

text = "this is a sample text with sample words and this text is for demonstration"

word_frequencies = {}

words = text.lower().split()

for word in words:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1

print("Word Frequencies:")
print(f"word_frequencies = {word_frequencies}")