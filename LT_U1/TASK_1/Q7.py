num_students = int(input("How many students do you want to enter? "))

students_data = {}

for i in range(num_students):
    print(f"\n--- Entering details for Student {i + 1} ---")
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    math_mark = int(input("Enter Math marks: "))
    science_mark = int(input("Enter Science marks: "))
    english_mark = int(input("Enter English marks: "))

    students_data[student_id] = {
        'name': student_name,
        'marks': {
            'Math': math_mark,
            'Science': science_mark,
            'English': english_mark
        }
    }

topper_name = ''
highest_total = -1

print("\n--- Student Total Marks ---")
for student_id, details in students_data.items():
    name = details['name']
    marks = details['marks']
    total_marks = sum(marks.values())
    
    print(f"Student: {name}, Total Marks: {total_marks}")
    
    if total_marks > highest_total:
        highest_total = total_marks
        topper_name = name

print("\n--- Topper ---")
print(f"The topper is {topper_name} with {highest_total} marks.")

print("\n--- All Students and Their Total Marks ---")
for student_id, details in students_data.items():
    name = details['name']
    total_marks = sum(details['marks'].values())
    print(f"{name}: {total_marks}")