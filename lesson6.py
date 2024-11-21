#We need to import a new object for templates
from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def Home():
    # Return the page found at templates/index.html
    return render_template('index.html')

app.run(debug=True, port=5000)
