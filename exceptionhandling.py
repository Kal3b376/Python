
try:
    print(number)
except:
    print("An error occured")

finally:
    print("Success")

x = 67
y = 2
try:
    print(x / y)
except:
    print("An arithmetic error occured")
finally:
    print("Success")