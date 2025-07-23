# 45 Uses a nested dictionary where each subject has internal marks.

student_grades = {
    "Tirth": {
        "Math": {"internal1": 85, "internal2": 90, "final": 92},
        "Science": {"internal1": 78, "internal2": 82, "final": 85}
    },
    "Dhruv": {
        "Math": {"internal1": 70, "internal2": 75, "final": 80},
        "Science": {"internal1": 90, "internal2": 88, "final": 95}
    }
}

print("Student Grades:")
for student, subjects in student_grades.items():
    print(f"\nStudent: {student}")
    for subject, marks in subjects.items():
        print(f"  Subject: {subject}")
        for mark_type, score in marks.items():
            print(f"    {mark_type.capitalize()}: {score}")
