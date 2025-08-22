# 4. Weekly hours for 7 employees
hours = [40, 38, 30, 42, 36, 25, 45]

# a) Total & average
total = sum(hours)
avg = total / len(hours)
print("Total hours:", total)
print("Average hours:", avg)

# b) Hours < 35
less_than_35 = []
for h in hours:
    if h < 35:
        less_than_35.append(h)
print("Employees < 35 hrs:", less_than_35)

# c) Increase all hours by 2
for i in range(len(hours)):
    hours[i] = hours[i] + 2
print("After increase:", hours)
