# 38 Modifies a specific field for a given key.

student_data = {
    "Tirth": {"age": 20, "major": "Computer Science"},
    "Dhruv": {"age": 21, "major": "Physics"},
    "Sakshi": {"age": 19, "major": "Mathematics"}
}

print("Original student data:")
for name, data in student_data.items():
    print(f"{name}: {data}")

# Modify the major for "Tirth"
if "Tirth" in student_data:
    student_data["Tirth"]["major"] = "Software Engineering"
    print("\nModified Tirth's major.")
else:
    print("\nTirth not found in student data.")

print("\nUpdated student data:")
for name, data in student_data.items():
    print(f"{name}: {data}")
