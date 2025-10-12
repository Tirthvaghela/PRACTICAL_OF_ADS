import numpy as np

# 1. Create 2D array: 5 patients -> [Systolic, Diastolic]
bp = np.random.randint(60, 181, size=(5, 2))  
print("Blood pressure readings for 5 patients (Systolic, Diastolic):")
print(bp)

# a) Blood pressure of 3rd patient
print("3rd patient BP:", bp[2])

# b) All diastolic readings
diastolic_readings = []
for row in bp:
    diastolic_readings.append(row[1])
print("Diastolic readings:", diastolic_readings)

# c) Replace systolic < 100 with 100
for row in bp:
    if row[0] < 100:
        row[0] = 100
print("After replacing low systolic:", bp)
