# Data type

numbers = 60 # Int
num = 45.36 # Float
greeting = "Hello there" # str
isPythonInteresting = True # boolean
fruits = ["apple", "banana", "mango"] # List
cars = ("BMW", "Mercedes", "Toyota","v8") #Tuple
countries = {"Kenya","Tanzania","Uganda"} #Set
student ={
    "firstname" : "Gold",
    "age" : 19,
    "course" : "MIT",
    "nationality" : "Kenyan"
} # Dictionary

print(num)
print(isPythonInteresting)
print(fruits)
print(cars)
print(countries)
print(student["firstname"])

# Determining datatype
print(type(isPythonInteresting))
print(type(cars))

# Typecasting is conerting one datatype to another
print(int(num))
print(float(numbers))