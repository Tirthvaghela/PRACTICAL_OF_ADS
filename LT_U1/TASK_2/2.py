# 2. Store and Display Multiple Employee Records (Nested Dictionary)
employees = {}

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))
    employees[emp_id] = {"Name": name, "Age": age, "Salary": salary}


# Display
for emp_id, details in employees.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
