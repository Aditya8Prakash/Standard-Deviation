import csv
import math
with open('./data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
def mean (data) : 
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean
def stendered_dev (data):
    squaredList = []
    for number in data:
        a = int(number)-mean(data)
        a = a**2
        squaredList.append(a)
    sum = 0
    for i in squaredList :
        sum = sum + i
    result = sum/(len(data)-1)
    std_dev = math.sqrt(result)
    return std_dev
final_result = stendered_dev(data)
print('> '+str(final_result))