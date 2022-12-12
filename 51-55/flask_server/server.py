from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# to run the server type the following in the terminal: export FLASK_APP=server.py THEN TYPE flask run NOTE: YOU MUST BE IN THE SAME DIRECTORY AS server.py