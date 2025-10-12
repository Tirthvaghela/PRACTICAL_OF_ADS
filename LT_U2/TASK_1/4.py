# 4. A department recorded research publications by 4 faculty members for 3 years (2D array).
# Options:
# a) Print the total publications for each faculty.
# b) Find which faculty member has the highest total publications.
# c) Print publications for Year 2 only.
import numpy as np

# 2D array: 4 faculty × 3 years
publications = np.array([
    [5, 3, 4],   # Faculty 1
    [2, 4, 6],   # Faculty 2
    [3, 3, 2],   # Faculty 3
    [6, 5, 4]    # Faculty 4
])

totals = np.sum(publications, axis=1)

print("Total publications for each faculty:")
for i, total in enumerate(totals, start=1):
    print(f"Faculty {i} total publications: {total}")

print("\nFaculty with the highest total publications:")
print(total)

print("\nPublications for Year 2 only:")
year_2 = publications[:, 1]  # Index 1 → Year 2

for i, pub in enumerate(year_2, start=1):
    print(f"Faculty {i}: {pub}")
