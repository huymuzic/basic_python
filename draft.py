# Without list comprehension
numbers = []
for x in range(1, 11):
    if x % 2 == 0:
        numbers.append("even")
    else:
        numbers.append(x)

# With list comprehension
numbers = ["even" if x % 2 == 0 else x for x in range(1, 11)]

print(numbers)

for x in range (6):
    print(x)

friends = [ 'Joseph', 'Glenn', 'Sally' ]

print(friends[0])

# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    each_line = line.rstrip().split()
    for item in each_line :
        if item not in lst :
            lst.append(item)
        else :
            continue

lst.sort()
print(lst)
    
fname = "mbox-short.txt"
fh = open(fname)
count = 0

for line in fh :
    if line.startswith("From:") :
        continue
    if line.startswith("From") :
        line_lst = line.rstrip().split()
    print(line_lst)

print("There were", count, "lines in the file with From as the first word")


# handle = open(filename)
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1