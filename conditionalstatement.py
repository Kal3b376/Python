temperature = 32

if temperature < 25:
    print("It is cold")
elif temperature > 25:
    print("It is hot")
else:
    print("Normal Temperature")

# A program that returns the largest number among three numbers
first = 56
second = 23
third = 78
if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second, "is the largest number")
else:
    print(third, "is the largest  number")

# A simple program that checks whether it is even or odd
number = int(input("Enter a number:"))
if number == 0:
    print(number, "is neutral.")
elif (number % 2) == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# A python program that returns area of a rectangle
# A = L * W
length = 20
witdh = 5
area= length * witdh
print("The area is ", area)

# A python program that returns area of a rectangle
# A = ½ (a + b) h
a = int(input("Enter a value:"))
b = int(input("Enter another value:"))
h = int(input("Enter a value:"))
Area = 0.5*(a + b)*h
print("The area is ", Area)

