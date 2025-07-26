# 53. Searches for a specific word and returns the lines containing it

search_word = 'Tirth'

with open('data.txt', 'r') as file:
    lines = file.readlines()  
    for line_number, line in enumerate(lines, start=1):
        if search_word in line:
            print(f"Line {line_number}: {line.strip()}")
