
courses = ["MIT","Cyber security","Data Science" ]

print(courses)

# Accessing an element in an array
print(courses[1])

# Adding a ne element in an array
courses.append("Android Development")
print(courses)

# Deleting an element in array
courses.remove("Cyber security")
print(courses)

# looping through an array
for course in courses:
    print(course)