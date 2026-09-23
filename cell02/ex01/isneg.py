number: float = float(input())
print(
    "This number is both positive and negative."
    if number == 0
    else "This number is negative." if number < 0 else "This number is positive."
)
