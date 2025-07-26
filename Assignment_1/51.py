with open("data.txt", "r") as file:
    line_count = len(file.readlines())

print("Number of lines in the file:", line_count)
