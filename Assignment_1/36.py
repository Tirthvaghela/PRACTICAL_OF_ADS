# 36 Uses in operator to check for key presence.

student_scores = {
    "Tirth": 95,
    "Dhruv": 88,
    "Sakshi": 72,
    "Dhruvee": 90
}

# Check if a key exists in the dictionary
print("Checking for key presence:")

if "Tirth" in student_scores:
    print("Tirth is in the student_scores dictionary.")
else:
    print("Tirth is not in the student_scores dictionary.")

if "Yash" in student_scores:
    print("Yash is in the student_scores dictionary.")
else:
    print("Yash is not in the student_scores dictionary.")
