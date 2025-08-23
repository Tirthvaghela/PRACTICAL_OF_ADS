import numpy as np

# 9. Random marks for 15 students (35–100)
marks_rand = np.random.randint(35, 101, 15)
print("\nAll Marks:", marks_rand)
print("Marks > 75:", marks_rand[marks_rand > 75])