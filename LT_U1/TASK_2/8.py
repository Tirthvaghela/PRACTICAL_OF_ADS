# 8. Delete the “department” Field from an Employee Dictionary
employee = {}

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))
    department = input("Enter employee department: ")
    employee[emp_id] = {"name": name, "age": age, "salary": salary, "department": department}

# Delete 'department'
if "department" in employee:
    del employee["department"]

# Display updated dictionary
print("Updated Employee Record:")
for key, value in employee.items():
    print(f"{key.capitalize()}: {value}")
