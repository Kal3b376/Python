import sqlite3

conn = sqlite3.connect('example.db')
print("Successfully Connected")

conn.execute("INSERT INTO Employee VALUES(1, 'Mark', 'Mugo', 45, 120000.00, 'Manager')")
conn.execute("INSERT INTO Employee VALUES(2, 'Mary', 'Maina', 25, 20000.00, 'Admin')")
conn.execute("INSERT INTO Employee VALUES(3, 'Marley', 'Mwaura', 35, 90000.00, 'HR')")
conn.execute("INSERT INTO Employee VALUES(4, 'Mandy', 'Muigo', 32, 30000.00, 'Receptionist')")
conn.execute("INSERT INTO Employee VALUES(5, 'Morgan', 'Mwangi', 26, 125000.00, 'Marketer')")
conn.execute("INSERT INTO Employee VALUES(6, 'Jane', 'Muindi', 33, 670000.00, 'Consultant')")

conn.commit()
print("Successfully inserted values into Employee table")
