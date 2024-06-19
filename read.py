imprt sqlite3

conn = sqlite3.connect('example.db')
print("Successfully Connected")

data = conn.execute("SELECT * FROM Employee")
for employee in data:
    print("ID: ", employee[0])
    print("FIRSTNAME: ", employee[1])
    print("LASTNAME: ", employee[2])
    print("AGE: ", employee[3])
    print("SALARY: ", employee[4])
    print("POSITION: ", employee[5])

print("Successfully fetched data")
conn.close()