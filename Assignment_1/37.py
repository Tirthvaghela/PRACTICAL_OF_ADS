# 37 Iterates over dictionary key-value pairs using items().

student_scores = {
    "Tirth": 95,
    "Dhruv": 88,
    "Sakshi": 72,
    "Dhruvee": 90
}

print("Iterating over student_scores using items():")
for name, score in student_scores.items():
    print(f"{name}: {score}")
