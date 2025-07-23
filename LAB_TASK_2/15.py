# 15. Input Patient Records Dynamically (Nested Dictionary)
patients = {}

n = int(input("How many patient records do you want to enter? "))

for i in range(n):
    pid = int(input("\nEnter Patient ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    illness = input("Enter Illness: ")

    patients[pid] = {
        "name": name,
        "age": age,
        "illness": illness
    }

# Display all records
print("\nPatient Records:")
for pid, details in patients.items():
    print(f"\nPatient ID: {pid}")
    for key, value in details.items():
        print(f"  {key.capitalize()}: {value}")
