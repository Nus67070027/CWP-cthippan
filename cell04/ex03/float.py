from math import floor

num: float = float(input('Give me a number: '))
print("This number is an integer." if floor(num) == num else "This number is a decimal.")