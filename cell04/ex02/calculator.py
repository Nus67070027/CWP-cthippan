first: int = int(input("Give me the first number: "))
second: int = int(input("Give me the second number: "))
print("Thank you!")
print(
    f"{first} + {second} = {first + second}\n{first} - {second} = {first - second}\n{first} / {second} = {(first / second):.0f}\n{first} * {second} = {first * second}"
)
