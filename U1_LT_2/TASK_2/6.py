# 6. Dosages for 10 patients
dosages = [45, 60, 55, 40, 70, 65, 30, 80, 55, 90]

# a) Average dosage
avg_dosage = sum(dosages) / len(dosages)
print("Average dosage:", avg_dosage)

# b) Replace < 50 with 50
for i in range(len(dosages)):
    if dosages[i] < 50:
        dosages[i] = 50
print("After replacing:", dosages)

# c) Dosages for patients 3 to 7
print("Patients 3 to 7:", dosages[2:7])
