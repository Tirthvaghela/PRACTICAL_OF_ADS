# 32. CRUD operations on a dictionary (student records).

student_records = {}

def create_record(roll_no, name):
    student_records[roll_no] = name
    print(f"Record created: Roll No. {roll_no}, Name: {name}")

def read_record(roll_no):
    if roll_no in student_records:
        print(f"Roll No. {roll_no}: Name: {student_records[roll_no]}")
    else:
        print(f"Roll No. {roll_no} not found.")

def update_record(roll_no, new_name):
    if roll_no in student_records:
        student_records[roll_no] = new_name
        print(f"Record updated: Roll No. {roll_no}, New Name: {new_name}")
    else:
        print(f"Roll No. {roll_no} not found for update.")

def delete_record(roll_no):
    if roll_no in student_records:
        del student_records[roll_no]
        print(f"Record deleted: Roll No. {roll_no}")
    else:
        print(f"Roll No. {roll_no} not found for deletion.")

# Example Usage
print("--- Creating Records ---")
create_record(101, "Alice")
create_record(102, "Bob")
create_record(103, "Charlie")
print("Current records:", student_records)

print("\n--- Reading Records ---")
read_record(101)
read_record(104)

print("\n--- Updating Records ---")
update_record(102, "Robert")
update_record(104, "David")
print("Current records:", student_records)

print("\n--- Deleting Records ---")
delete_record(103)
delete_record(105)
print("Current records:", student_records)