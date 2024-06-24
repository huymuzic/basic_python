import pprint

# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
food = food + ["pasta", "taco"]

food[0] = "sushi"

food.append("ice cream")
food.remove("hamburger")
# print(food)
# print(food.pop())
food.pop()
food.insert(0, "cake")
food.sort()
for index, item in enumerate(food): 
    print(f'index: {index} - item: {item}')
food.clear()

furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):
    print(f'The {item} costs ${amount}')

# print(furniture[0:-1])
# print(sorted(furniture))

a, b = 'table', 'chair'
a, b = b, a
print(a, b)

test = ['a', 'b', 'c', 'd', 'e']
test.sort(reverse=True)
print(test)        

multiple_assignment = ['first', 'second', 'third', 'fourth']
table, chair, rack, shelf = multiple_assignment
assignment = [table, chair, rack, shelf]
for item in assignment:
    print(item)

# 2D lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

# print(food)

# tuples cannot be changed while lists can

tuple(['cat', 'dog', 5])
print(tuple(['cat', 'dog', 5]))

list(('cat', 'dog', 5))
print(list(('cat', 'dog', 5)))

list('hello')
print(list('hello'))

student = ("Huy", 19, "male")

print(student.count("Huy")) 
# count() method returns the number of times a specified value occurs in a tuple
print(student.index("male"))
# index() method finds the first occurrence of the specified value
if "Huy" in student:
    print("Yes, 'Huy' is in the student tuple")

# set = collection which is unordered, unindexed, and unchangeable, 
#       and does not allow duplicate values
#       a set is faster than a list

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
dishes.update(utensils)
print(dishes)
dinner_table = utensils.union(dishes)
# dinner_table = utensils | dishes

print(dishes.difference(utensils))
# dishes - utensils
print(dishes.intersection(utensils))
# dishes & utensils
print(dishes.symmetric_difference(utensils))
# dishes ^ utensils

# for item in dinner_table:
#     print(item)


# dictionary = A changeable, unordered collection of unique key:value pairs
#              fast because they use hashing, allow us to access a value quickly

capitals = {
            'USA': 'Washington D.C.', 
            'India': 'New Delhi', 
            'China': 'Beijing'
           }

# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
capitals['Vietnam'] = 'Hanoi'

print("")
pprint.pprint(capitals)
print(capitals['Vietnam'])
capitals.update({'Vietnam': 'Ho Chi Minh City'})
print(capitals.get(('Germany'), "Country not found"))
print(capitals.get('India'))
capitals.setdefault('Germany', 'Berlin')
print('Germany' in capitals.keys())
print('Berlin' in capitals.values())
capitals.pop('China')
# del remove without returning the value
capitals.popitem()

for key, value in capitals.items():
    print(f'Key: {key} | Value: {value}')

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)

largest = None
smallest = None
numbers = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        numbers.append(num)

    except ValueError:
        print("Invalid input")
        continue
    
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Maximum:", largest)
print("Minimum:", smallest)

