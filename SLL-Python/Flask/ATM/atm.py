from flask import Flask, redirect, render_template, request, url_for, session
import time
import re

app = Flask(__name__)

# protexted routes
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        balance = session["balance"]
    except KeyError:
        balance = session["balance"] = 8000  # first time only

    if request.method == "GET":
        return render_template("index.html", balance=balance, msg="")


if __name__ == "__main__":
    app.run(debug=True)
