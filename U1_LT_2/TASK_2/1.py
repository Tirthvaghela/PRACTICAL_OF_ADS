import numpy as np

# 1. Create 2D array: 5 patients -> [Systolic, Diastolic]
bp = np.random.randint(60, 181, size=(5, 2))  # 5 patients, systolic 60-180, diastolic 60-180
print("Blood pressure readings for 5 patients (Systolic, Diastolic):")
print(bp)

# a) Blood pressure of 3rd patient
print("3rd patient BP:", bp[2])

# b) All diastolic readings
print("Diastolic readings:", [row[1] for row in bp])

# c) Replace systolic < 100 with 100
for row in bp:
    if row[0] < 100:
        row[0] = 100
print("After replacing low systolic:", bp)
