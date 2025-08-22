# 3. Add New Patient Record and Display

patients = {
    201: {"name": "Sam", "age": 30, "disease": "Flu"},
    202: {"name": "Lily", "age": 25, "disease": "Cold"}
}

# Add new patient
patients[203] = {"name": "Max", "age": 40, "disease": "Diabetes"}

# Display all
for pid, info in patients.items():
    print(f"\nPatient ID: {pid}")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
