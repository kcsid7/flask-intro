from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_func():
    """Adds two user arguments"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route("/sub")
def sub_func():
    """Subtracts two user arguments"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route("/mult")
def mult_func():
    """Multiplies two user arguments"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route("/div")
def div_func():
    """Divides two user arguments"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))


math_functions = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route("/math/<func>")
def math_func(func):
    """Perform a math function"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(math_functions[func](a, b))
