# 4. Display Only Keys and Values from Single Employee Dictionary

employee = {
    "name": "Anita",
    "designation": "Manager",
    "salary": 75000
}

# Display keys and values
for key, value in employee.items():
    print(f"{key.capitalize()}: {value}")
