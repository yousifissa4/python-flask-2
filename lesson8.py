from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def Home():
    # Set a variable to a value
    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d %H:%,:%S")

    # Set the tmeplate name to our variables
    return render_template('index.html', logged_in=False, name=nameValue, time=timeValue)

app.run(debug=True, port=5000)