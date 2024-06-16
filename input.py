from datetime import datetime

terminate = ""

while True:
    try:
        name = input('What is your name? ')
        age = int(input('How old are you? '))
    except ValueError:
        print('Please enter a valid age')
        continue

    hundredYearsOld = datetime.now().year + 100 - int(age)
    print(f"{name} will be 100 years old in {hundredYearsOld}")

    terminate = input("Do you wish to continue? (yes/no)")
    if terminate.lower() == 'no':
        break