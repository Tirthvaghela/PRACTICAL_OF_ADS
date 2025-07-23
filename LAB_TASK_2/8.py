# 8. Delete the “department” Field from an Employee Dictionary
employee = {
    "name": "Sara",
    "salary": 70000,
    "department": "Marketing"
}

# Delete 'department'
if "department" in employee:
    del employee["department"]

# Display updated dictionary
print("Updated Employee Record:")
for key, value in employee.items():
    print(f"{key.capitalize()}: {value}")
