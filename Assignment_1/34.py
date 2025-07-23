# Existing dictionary of students
students = {
    101: {"name": "Tirth", "marks": 85, "course": "Mathematics"},
    102: {"name": "Dhruv", "marks": 78, "course": "Physics"},
    103: {"name": "Sakshi", "marks": 75, "course": "Computer Science"}
}

# Adding a new student with ID 104
students[104] = {"name": "DHruvee", "marks": 88, "course": "Biology"}

# Display updated dictionary
for student_id, details in students.items():
    print(f"Student ID: {student_id}")
    print(f"  Name: {details['name']}")
    print(f"  Marks: {details['marks']}")
    print(f"  Course: {details['course']}\n")
