# 39 Deletes a specific entry using del.

student_data = {
    "Tirth": {"age": 20, "major": "Computer Science"},
    "Dhruv": {"age": 21, "major": "Physics"},
    "Sakshi": {"age": 19, "major": "Mathematics"}
}

print("Original student data:")
for name, data in student_data.items():
    print(f"{name}: {data}")

# Delete "Dhruv" from the dictionary
if "Sakshi" in student_data:
    del student_data["Sakshi"]
    print("\nDeleted Sakshi from student data.")
else:
    print("\nSakshi not found in student data.")

print("\nUpdated student data:")
for name, data in student_data.items():
    print(f"{name}: {data}")
