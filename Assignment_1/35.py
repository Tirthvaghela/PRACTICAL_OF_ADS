# 35 Demonstrates how to access only keys or only values from a dictionary.

student_scores = {
    "Tirth": 95,
    "Dhruv": 88,
    "Sakshi": 72,
    "Dhruvee": 90
}

# Accessing only keys
print("Keys (student names):")
for name in student_scores.keys():
    print(name)

# Accessing only values
print("\nValues (scores):")
for score in student_scores.values():
    print(score)
