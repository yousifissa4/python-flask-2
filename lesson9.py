# import the new sqlite package
import sqlite3

# connect to the db we made
db = sqlite3.connect("database/student_marks.db")
# when I get data, also give me the feild names
db.row_factory = sqlite3.Row

# Run a SELECT query on students
students= db.execute("SELECT * From students").fetchall()

# Display the first student
for person in students:
    print(f"Firstname : {students[0]['firstname']}")
    print(f"Lastname  : {students[0]['Lastname']}")
    print(f"DOB       : {students[0]['dob']}")