from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# to run the server type the following in the terminal: export FLASK_APP=server.py THEN TYPE flask run NOTE: YOU MUST BE IN THE SAME DIRECTORY AS server.py


#Decorators to add a tag around text on web page.
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


# Different routes using the app.route decorator
@app.route("/bye")
@make_emphasis
@make_bold
def bye():
    return "Bye"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def green(name, number=None):
    return f"Hello {name}, you are {number} years old"


# USING THE FOLLOWING CODE ALLOWS THE PYCHARM RUN CONTROLS TO BE USABLE TO START/STOP THE SERVER
if __name__ == "__main__":
    app.run(debug=True)
    # debug allows the server to auto reload


