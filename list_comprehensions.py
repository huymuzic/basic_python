# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Without list comprehension
flattened = []
for sublist in matrix:
    for item in sublist:
        flattened.append(item)

# With list comprehension
flattened = [item for sublist in matrix for item in sublist]

print(flattened)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Without list comprehension
pairs = []
for item1 in list1:
    for item2 in list2:
        pairs.append((item1, item2))

# With list comprehension
pairs = [(item1, item2) for item1 in list1 for item2 in list2]

print(pairs)

words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)  # Output: ['a', 'b', 'c']
