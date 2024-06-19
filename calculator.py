# A simple calculator program
op = input("Enter an operator (+, -, *, /):")
first = float(input("Enter first number:"))
second = float(input("Enter second number:"))

if op == '+':
    print({first + second})
elif op == '-':
    print(first - second)
elif op == '*':
    print(first * second)
elif op == '/':
    if second == 0:
        print("Error! Divison by zero.")
    else:
        print(first / second)
else:
    print("Invalid operator input")
