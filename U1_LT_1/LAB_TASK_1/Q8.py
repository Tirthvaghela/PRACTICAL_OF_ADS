num_patients = int(input("How many patients do you want to enter? "))

patients = {}

for i in range(num_patients):
    print(f"\n--- Entering details for Patient {i + 1} ---")
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")

    bp = int(input("Enter Blood Pressure value: "))
    sugar = int(input("Enter Blood Sugar value: "))
    cholesterol = int(input("Enter Cholesterol Level value: "))

    patients[patient_id] = {
        "name": name,
        "results": {
            "Blood Pressure": bp,
            "Blood Sugar": sugar,
            "Cholesterol Level": cholesterol
        }
    }

patient_name = ''
lowest_total = float('inf')  

print("\n--- Patient Test Results ---")
for patient_id, details in patients.items():
    name = details['name']
    total_values = sum(details['results'].values())
    
    print(f"Patient: {name}, Total of Test Values: {total_values}")
    
    if total_values < lowest_total:
        lowest_total = total_values
        patient_name = name

    print("\n--- Healthiest Patient ---")
    print(f"The healthiest patient is {patient_name} with a total score of {lowest_total}.")
