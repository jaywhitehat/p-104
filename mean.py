import csv
from tkinter import N
#to read and convert the file into list
with open('SOCR-HeightWeight.csv')as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
#to get height data from the file
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

#to calculate mean
n=len(new_data)
print(n)
total=0
for x in new_data:
    total += x

mean = total/n
print("mean / average height of people :" + str(mean))
