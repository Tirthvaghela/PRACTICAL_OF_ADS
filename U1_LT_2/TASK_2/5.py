# 5. Salaries for 5 faculty
salaries = [750000, 820000, 640000, 900000, 780000]

# a) Add ₹25,000 bonus
for i in range(len(salaries)):
    salaries[i] += 25000
print("After bonus:", salaries)

# b) Lowest salary after bonus
print("Lowest salary:", min(salaries))

# c) Salaries > ₹8,00,000
high_salaries = []
for s in salaries:
    if s > 800000:
        high_salaries.append(s)
print("Salaries > 8,00,000:", high_salaries)
