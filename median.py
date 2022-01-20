import csv
from hashlib import new
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

n=len(new_data)
print(n)

new_data.sort()
#to calculate median
if (n % 2 == 0):
    m1=float(new_data[n//2])#floorDivision gives nearest whole no.
    m2=float(new_data[n//2-1])
    median=(m1+m2)/2
else:
    median=new_data[n//2]
print("median:"+ str(median))