# 12. Word Frequency Counter from Medical Report

report = "Patient has a high fever and high blood pressure. Fever continues for two days."

# Convert to lowercase and split into words
words = report.lower().replace(".", "").split()

# Count frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequency:")
for word, count in freq.items():
    print(f"{word}: {count}")
