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