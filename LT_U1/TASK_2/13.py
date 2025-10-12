# 13. Combine Two Lists into a Patient Dictionary
keys = ["Name", "Age", "Disease"]
values = ["Meena", 42, "Diabetes"]

# Combine using zip and dict()
patient = dict(zip(keys, values))

print("Patient Record:")
print(patient)
