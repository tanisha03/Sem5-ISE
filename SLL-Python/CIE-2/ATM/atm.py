from flask import Flask, redirect, render_template, request, url_for, session
import time
import re  # regular expressions

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "secret"  # for pretected routes


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        balance = session["balance"]  # after session has been initialized
    except KeyError:
        balance = session["balance"] = 8000  # first time only

    if request.method == "GET":  # initialize get route,blank msg
        session["transactions"]=0
        return render_template("index.html", balance=balance, msg="Welcome to ATM")

    if request.method == "POST":
        if session["transactions"]>5:
            msg = "Cannot process more than 5 transactions"
            return render_template("index.html", balance=balance, msg=msg)
        # Checks if user clicked on Withdraw
        elif request.form["action"] == "Withdraw":
            # Checks if amount is greater than balance
            if int(request.form["amount"]) > session["balance"]:
                msg = "Cannot withdraw amount greater than balance"
                return render_template("index.html", balance=balance, msg=msg)

            # Deducts amount entered from balance and stores in session
            else:
                session["transactions"]=session["transactions"]+1
                balance = balance - int(request.form["amount"])
                session["balance"] = balance
                msg = "Money Withdrawn"
                return render_template("index.html", balance=balance, msg=msg)

        # Checks if user clicked on Deposit
        elif request.form["action"] == "Deposit":
            session["transactions"]=session["transactions"]+1
            # Adds amount entered to balance and stores in session
            balance = balance + int(request.form["amount"])
            session["balance"] = balance
            msg = "Money Deposited"
            return render_template("index.html", balance=balance, msg=msg)


if __name__ == "__main__":
    app.run(debug=True)

