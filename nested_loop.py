# nested loops =    The "inner loop" will finish all of it's iterations
#                   before the "outer loop" will finish one

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print() # This will create a new line after the inner loop has finished2
