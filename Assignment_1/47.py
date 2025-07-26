# 47.Reads a CSV file containing marks of students and calculates average marks per subject.
import csv

with open('marks.csv',newline='') as file:
    reader = csv.DictReader(file)
    total = {"Math" : 0 ,"Science" : 0 ,"English" : 0}
    count = 0

    for row in reader :
        total['Math']+= int(row["Math"])
        total['Science']+= int(row["Science"])
        total['English']+= int(row["English"])
        count+=1

    print("AVARAGE MARKS : ")
    for subject in total :
        print(f"Avarage Of {subject} : {total[subject]/count}")