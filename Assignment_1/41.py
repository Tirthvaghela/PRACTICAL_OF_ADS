# 41 Uses get() to safely access values with default fallback.

student_data = {
    "Tirth": {"age": 20, "major": "Computer Science"},
    "Dhruv": {"age": 21, "major": "Physics"}
}

# Accessing an existing key using get()
tirth_major = student_data.get("Tirth", {}).get("major", "N/A")
print(f"Tirth's major: {tirth_major}")

# Accessing a non-existing nested key with a default fallback
dhruv_minor = student_data.get("Dhruv", {}).get("minor", "Undeclared")
print(f"Dhruv's minor: {dhruv_minor}")

# Accessing a non-existing top-level key with a default dictionary fallback
non_existent_student = student_data.get("Priya", {"age": "N/A", "major": "N/A"})
print(f"Dhruvee's data: {non_existent_student}")
