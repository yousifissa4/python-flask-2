from flask import Flask, render_template
import sqlite3

# Create the flask app
app = Flask(__name__)

# Home page route
@app.route("/")
def Home():
    # Connect and get all the data
    db = sqlite3.connect("database/students_marks.db")
    db.row_factory = sqlite3.Row
    studentData = db.execute("SELECT * FROM Students").fetchall()


    #Return the page and data
    return render_template("index.html", students=studentData, logged_in= False)

@app.route("/marks")
def Marks():
    # Connect and get all the data
    db = sqlite3.connect(" database/student_marks.db")
    db.row_factory = sqlite3.Row
    markData = db.execute("SELECT * FROM Marks").fetchall()

    #Return the page and data
    return render_template("marks.html", results=markData)

app.run(debug=True, port=5000)