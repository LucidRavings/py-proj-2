from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", cupcakes = get_cupcakes("menu.csv"))

@app.route("/add_cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("menu.csv", name)

    if cupcake:
        add_cupcake("order.csv", cupcake=cupcake)
        return redirect(url_for("home"))
    else:
        return "Invalid cupcake name."

@app.route("/single_cupcake/<name>")
def single_cupcake(name):
    cupcake = find_cupcake("menu.csv", name)

    if cupcake:
        return render_template("single_cupcake.html", cupcake=cupcake)
    else:
        return "Invalid cupcake name."

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 5005, host = "localhost")