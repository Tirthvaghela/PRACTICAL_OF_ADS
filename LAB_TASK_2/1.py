# 1. CRUD Operations on a Patient Dictionary
patients = {}

# Create
patients[101] = "Alice"
patients[102] = "Bob"

# Read
print("Current Patients:")
for pid, name in patients.items():
    print(f"ID: {pid}, Name: {name}")

# Update
patients[102] = "Robert"

# Delete
del patients[101]

# Final state
print("\nUpdated Patients:")
for pid, name in patients.items():
    print(f"ID: {pid}, Name: {name}")
