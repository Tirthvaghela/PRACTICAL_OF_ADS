# Creating a nested dictionary to store student data
students = {
    101: {"name": "Tirth", "marks": 85, "course": "Mathematics"},
    102: {"name": "Dhruv", "marks": 78, "course": "Physics"},
    103: {"name": "Sakshi", "marks": 75, "course": "Computer Science"}
}

# Accessing and displaying data
for student_id, details in students.items():
    print(f"Student ID: {student_id}")
    print(f"  Name: {details['name']}")
    print(f"  Marks: {details['marks']}")
    print(f"  Course: {details['course']}\n")
