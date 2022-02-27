from flask import app
from flask import render_template    # Add this line
from flask import Flask

app = Flask (__name__)

@app.route('/')
def say_hello():
    user = {"name": "Faith"}
    return render_template("index.html", user=user)    # Modify this line

app.run(
    debug = True
)






    