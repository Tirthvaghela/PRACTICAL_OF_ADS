# 3. Add New Patient Record and Display

patients = {}

n = int(input("Enter number of patients: "))

for i in range(n):
    pid = int(input("Enter patient ID: "))
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    patients[pid] = {"name": name, "age": age, "disease": disease}

# Add new patient(s)
while True:
    add_more = input("\nDo you want to add a new patient? (y/n): ").strip().lower()
    if add_more != 'y':
        break
    pid = int(input("Enter new patient ID: "))
    name = input("Enter new patient name: ")
    age = int(input("Enter new patient age: "))
    disease = input("Enter new patient disease: ")
    patients[pid] = {"name": name, "age": age, "disease": disease}

# Display all
for pid, info in patients.items():
    print(f"\nPatient ID: {pid}")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
