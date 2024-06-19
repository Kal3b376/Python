class Student:
    def __init__(self, firstname, course, language ):
        self.firstname = firstname
        self.course = course
        self.language = language

    def sleep(self):
        print(self.firstname ,"is sleeping")

K = Student("Kaleb","MIT", "Python")
print(K.firstname)
print(K.course)
print(K.language)
K.sleep()

student2 = Student("Clarence","Web", "Kotlin")
print(student2.firstname)
print(student2.course)
print(student2.language)
student2.sleep()
