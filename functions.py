# Inbuilt functions
y = max(230, 6578, 12, 890)
print(y)

x = min(230, 6578, 12, 890)
print("The minimum value is", x)

z = pow(2, 3)
print(z)

# User-defined functions
def student():
    print("Kaleb")

student() # Calling a function

def Person():
    print("Person is walking")

Person()

# Parameters and Arguments
def add(num1, num2):
    print(num1 + num2)

add(34, 35)
add(num1:=29, num2:=28)

def Employee(fullname,age,email,maritalstatus, position):
    print(fullname,age,email,maritalstatus,position)

Employee("Kaleb",18,"ndunguc376@gmail.come","Single","MD")
Employee("Kylian",28,"ndunguc376@gmail.come","Divorced","MD")
Employee("Kenneth",21,"ndunguc376@gmail.come","Single","MD")
Employee("Kenneth",38,"ndunguc376@gmail.come","Married","MD")
