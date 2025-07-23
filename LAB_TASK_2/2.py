# 2. Store and Display Multiple Employee Records (Nested Dictionary)
employees = {
    1: {"name": "Tirth", "salary": 50000, "department": "HR"},
    2: {"name": "Dhruv", "salary": 60000, "department": "IT"},
    3: {"name": "Dhurvee", "salary": 55000, "department": "Finance"}
}

# Display
for emp_id, details in employees.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
