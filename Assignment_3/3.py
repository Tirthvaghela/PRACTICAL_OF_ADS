import pandas as pd
# ---------------------------------------------
# 3. Student Marks from Dictionary
# ---------------------------------------------
marks = {'Math': 78, 'Science': 82, 'English': 90, 'History': 85}
marks_series = pd.Series(marks)
print("=== Student Marks Series ===")
print("Subjects with marks > 80:\n", marks_series[marks_series > 80])
print("\n")
print("=== Average Marks ===")
print("Average Marks:", marks_series.mean())
