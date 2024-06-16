# function = a block of code which only runs when it is called

def hello(name):
    print("Hello! " + name)
    print("Have a nice day!")

my_name = "Huy"

# hello(my_name)

def multiply(a, b):
    return a * b

x = multiply(3, 4)
# print(x)

# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Flo" # global scope (available everywhere)

def display_name():
    name = "Huy" # local scope (only available inside the function)
    print(name)

# display_name()
# print(name)

# args = parameters that will pack all arguments into a tuple
#        useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

# print(add(1, 2, 3, 69))

# kwargs = parameters that will pack all arguments into a dictionary
#          useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Huy", last="Le")

