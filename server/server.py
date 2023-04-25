from flask import Flask, render_template
from cupcakes import get_cupcakes

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html", cupcakes = get_cupcakes("menu.csv"))

@app.route("/single_cupcake")
def single_cupcake():
    return render_template("single_cupcake.html")

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 5005, host = "localhost")