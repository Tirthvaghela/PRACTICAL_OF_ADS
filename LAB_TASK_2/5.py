# 5. Check if "age" Exists in Patient Record
patient = {
    "name": "Alex",
    "age": 45,
    "disease": "Hypertension"
}

# Check for age
if "age" in patient:
    print(f"Patient's age is: {patient['age']}")
else:
    print("Age not found in patient record.")
