# 10. Use get() to Access Non-existent Key with Default Value
patient = {
    "id": 105,
    "name": "Tina",
    "age": 28,
    "disease": "Cold"
}

# Access non-existent key 'status' safely
status = patient.get("status", "Not Available")
print(f"Patient Status: {status}")
