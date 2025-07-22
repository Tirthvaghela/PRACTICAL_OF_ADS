num_students = int(input("How many students do you want to enter? "))
students = {}

print("--- Enter Student Details ---")
for i in range(num_students):
    print(f"\n--- Student {i + 1} ---")
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    
    math_mark = int(input("Enter Math marks: "))
    science_mark = int(input("Enter Science marks: "))
    english_mark = int(input("Enter English marks: "))

    students[student_id] = {
        "name": name,
        "marks": {
            "Math": math_mark,
            "Science": science_mark,
            "English": english_mark
        }
    }

print("\n--- Student Records Summary ---")
for student_id, student_info in students.items():
    student_name = student_info["name"]
    
    total_marks = sum(student_info["marks"].values())
    
    print(f"Student: {student_name}, Total Marks: {total_marks}")