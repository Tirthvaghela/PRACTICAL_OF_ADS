# 1. Start with an empty dictionary to store the records.
students = {}

# 2. Ask the user how many students to enter.

num_students = int(input("How many students do you want to enter? "))
    
    # 3. Loop to get the details for each student.
for i in range(num_students):
        print(f"\n--- Entering details for Student {i + 1} ---")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        
        # Create an inner dictionary for the marks.
        marks = {}

        marks['Math'] = int(input("Enter Math marks: "))
        marks['Science'] = int(input("Enter Science marks: "))
        marks['English'] = int(input("Enter English marks: "))


        # 4. Add the completed student record to the main dictionary.
        students[student_id] = {
            "name": name,
            "marks": marks
        }

    # 5. Iterate and display the records that were entered.
print("\n--- Student Records ---")
if not students:
        print("No student data was entered correctly.")
else:
        for student_id, student_info in students.items():
            name = student_info["name"]
            total_marks = sum(student_info["marks"].values())
            print(f"Student: {name}, Total Marks: {total_marks}")