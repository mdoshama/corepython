# Ask user for a number, Print multiplication table of that number (1 to 10)

number = int(input("Enter a number: "))
for i in range(1,11):
    print(number, "*", i ,"=", number * i )