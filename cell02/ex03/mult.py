first_number: float = float(input("Enter the first number:\n"))
second_number: float = float(input("Enter the second number:\n"))
result: float = first_number * second_number
print(
    f"{first_number:.0f} X {second_number:.0f} = {result:.0f}\nThe result is {'positive and negative' if result == 0 else 'negative' if result < 0 else 'positive'}."
)
