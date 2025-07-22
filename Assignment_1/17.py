# 17. Store Marks in a List and Calculate Average, Maximum, and Minimum
marks = []
for i in range(3):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)
average = sum(marks) / len(marks)
maximum = max(marks)
minimum = min(marks)
print(f"\nAverage Marks: {average:.2f}")
print(f"Maximum Marks: {maximum:.2f}")
print(f"Minimum Marks: {minimum:.2f}")
