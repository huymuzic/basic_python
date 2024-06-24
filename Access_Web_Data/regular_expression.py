import re

with open('actual_data.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
total = 0
numlist = []
for line in data:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        numlist.append(numbers)
    for num in numbers:
        total += int(num)
print(total)
    