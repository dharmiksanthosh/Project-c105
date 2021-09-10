import math

data = [60,61,65,63,98,99,90,95,91,96]

def mean(data):
    total = 0
    n = len(data)

    for x in data:
        total += int(x)

    mean = total/n
    return mean

squared_list = []

for entry in data:
    a = int(entry) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum += i

result = sum/(len(data)-1)

std_deviation = math.sqrt(result)
print(f'Standard Deviation is {std_deviation}')