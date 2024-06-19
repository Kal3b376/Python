class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
            print(self.name,"is studying")

accountant = Person("Joe", "34", "Male")
accountant.details()
print(accountant.name)
print(accountant.age)
print(accountant.gender)
consultant = Person("Martha", "56", "Female")
consultant.details()
print(consultant.name)
print(consultant.age)
print(consultant.gender)
doctor = Person("James", "27", "Male")
doctor.details()
print(doctor.name)
print(doctor.age)
print(doctor.gender)
