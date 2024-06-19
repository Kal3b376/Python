# A class s a blueprint of an object
# Object is an instance of a class
class Person:
    #Properties/Attribute/Variable/Characteristic
    name = "Patrick"
    age = 18
    height = 2.1

    # Method/Function/Behaviour
    def walk(self):
        print("Person is walking")

accountant = Person()  #Creating an object
accountant.walk()

teacher = Person()
teacher.walk()