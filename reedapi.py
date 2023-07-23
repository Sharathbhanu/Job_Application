from flask import Flask
app = Flask('Flask')

@app.route("/")
def hello():
    return "Hello!"