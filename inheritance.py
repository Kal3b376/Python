# The parent class
  class Animal:
    def speak(self):
        print("Animal is speaking")

# Child classes
class Bee(Animal):
    def buzz(self):
        print("Bee is buzzing")


class Duck(Bee):
    def quack(self):
        print("Duck is quacking")

A = Animal()
A.speak()
B = Bee()
B.buzz()
B.speak()
D = Duck()
D.quack()
D.buzz()
D.speak()