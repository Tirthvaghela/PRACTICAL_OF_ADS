# 26.Performs union, intersection, and difference on two sets

def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return union, intersection, difference

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union, intersection, difference = set_operations(A, B)

print("Union:", union)
print("Intersection:", intersection)
print("Difference (A - B):", difference)