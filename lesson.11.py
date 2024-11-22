from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/student/<id>")
def Student(id):
   

   # Get the student's data
   db = sqlite3.connect("database/student_marks.db")
   db.row_factory = sqlite3.Row

   # We use fetch one, since we know were only selecting 1 student
   studentData = db.execute(f"SELECT * FROM Students WHERE id={id}").fetchone()

   #Get the marks as wellm note we fetch all because they may have multiple marks
   markData = db.execute(f"SELECT * FROM Marks WHERE student_id={id}").fetchall()

   html = f"""
        the student information is <br>
        Firstname: {studentData[ 'firstname']}<br>
        Lastname: {studentData[ 'lastname']}<br>
        DOB: {studentData[ 'dob']}<br>
        """
   for result in markData:
       html += f"Mark for {result['subject]']}"

       return html
app.run(debug=True, port= 5000)