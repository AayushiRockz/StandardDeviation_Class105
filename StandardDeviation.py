import csv

with open("data.csv", newline='') as f :
    reader = csv.reader(f)
    file_data = list(reader)

print(file_data)
data = file_data[0]
print(data)

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    return mean

squared_list = []
for num  in data:
    a = int(num)-mean(data)
    a = a**2
    squared_list.append(a)

sum =0
for x in squared_list:
    sum += x

result = sum/(len(data)-1)

import math

standard_deviation = math.sqrt(result)
print("SD is :"+str(standard_deviation))
