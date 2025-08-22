# 7. Marks for 15 students
marks = [35, 90, 65, 40, 75, 82, 33, 58, 95, 45, 38, 88, 77, 66, 50]

# a) Replace < 40 with "Fail"
for i in range(len(marks)):
    if marks[i] < 40:
        marks[i] = "Fail"
print("After replacing fails:", marks)

# b) Count passed students
passed_count = 0
for m in marks:
    if isinstance(m, int) and m >= 40:
        passed_count += 1
print("Passed students:", passed_count)

# c) Top 5 marks sorted
valid_marks = []
for m in marks:
    if isinstance(m, int):
        valid_marks.append(m)
valid_marks.sort(reverse=True)
print("Top 5 marks:", valid_marks[:5])
