from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key' #required for flask messages
@app.route("/add", methods=("GET", "POST"))
def AddStudent():

    # Did the user post data?
    if request.method == "POST":
         
         #Get the values from the form
         firstname     = request.form['firstname']
         lastname      = request.form['lastname']
         dob           = request.form['dob']
         
         # build our query and save to the database
         db =sqlite3.connect("database/student_marks.db")
         cursor = db.cursor()

         cursor.execute("SELECT * FROM Students WHERE firstname = ? AND lastname = ? AND dob = ?",
                        (firstname, lastname, dob))
         existing_student = cursor.fetchone()
         
         if existing_student:
              flash(f"Student {firstname} {lastname} with DOB {dob} already exists")
    else:
         cursor.execute("INSERT INTO Students('Firstname', 'lastname', 'dob') VALUES (?, ? , ?)",
                        (firstname, lastname, dob))
         db.commit()
         flash(f" Student {firstname} {lastname} added successfully.")
    
    db.close()

    
    return render_template('add.html')

app.run(debug=True, port=5000)