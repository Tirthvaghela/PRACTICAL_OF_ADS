# 7. Update Disease or Status of a Patient and Display
patient = {
    "id": 101,
    "name": "John",
    "age": 35,
    "disease": "Fever"
}

print("Original Record:")
for key, value in patient.items():
    print(f"{key.capitalize()}: {value}")
print("\nUpdating disease...\n")
# Update disease
patient.update({"disease": "Recovered"})

# Display updated record
for key, value in patient.items():
    print(f"{key.capitalize()}: {value}")
