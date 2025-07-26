# 48 .Writes sample student data to a text file.

data = "Name : Tirth \nCourse : IMSCIT \n Marks : 92"
with open('data.txt','w') as file:
    file.write(data)
print("DATA PRINTED")