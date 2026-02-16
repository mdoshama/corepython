# Create a function:, Named : is_even , Takes one number , Returns True if number is even, Returns False if odd

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))
result = is_even(number)
print(result)
