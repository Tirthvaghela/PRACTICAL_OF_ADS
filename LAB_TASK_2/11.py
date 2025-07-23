# 11. Merge Two Employee Dictionaries with Overlapping Keys
emp1 = {101: "Tirth", 102: "Dhruv"}
emp2 = {102: "Dhruvee", 103: "Sakshi"}

# Merge emp2 into emp1 (overwrites duplicates)
merged = emp1.copy()
merged.update(emp2)

print("Merged Employee Dictionary:")
print(merged)
