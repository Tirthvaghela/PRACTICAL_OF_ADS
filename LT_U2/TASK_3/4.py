# 4. Student Exam Scores (Boolean Indexing + Masking)
# A school records exam scores of 100 students (range: 0–100).
# • Generate a 1D NumPy array of size 100 with random integers between 0 and 100.
# • Create a Boolean mask to find all students who scored more than 75.
# • Count how many students failed (score < 40).
# • Replace all failing scores with 40 (grace marks policy).


import numpy as np

exam_scores = np.random.randint(0, 100, size=100)
high_mask = exam_scores > 75
failing_count = np.sum(exam_scores < 40)
exam_scores[exam_scores < 40] = 40

print("=====================================================")
print("4. Student Exam Scores:")
print("=====================================================")
print("Scores > 75:", exam_scores[high_mask])
print("=====================================================")
print("Number of failing students (before grace):", failing_count)
print("=====================================================")
print("Scores after grace policy applied:", exam_scores)
print("=====================================================")
print()