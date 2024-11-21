from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def Home():
    # Set a variable to value
    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Set the template name to our variable
    return render_template('index.html', name=nameValue, time= timeValue)

app.run(debug=True, port=5000)