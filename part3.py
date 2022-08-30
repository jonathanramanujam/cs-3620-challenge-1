# Jonathan Ramanujam
# CS 3620
# Python Basics
# Part 3: For Loops and Range Function

print("\nPart 3: For Loops and Range Function")

print("\nPrinting 'I am a programmer' 5x")
for x in range(5):
    print(f"{x + 1}: I am a programmer")

print("\nSquare values of 1 - 9")

def SquareValuesOneToNine():
    for x in range(1, 10):
        print(f"{x}^2 = {x**2}")

SquareValuesOneToNine()
