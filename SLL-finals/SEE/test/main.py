from flask import Flask, render_template, redirect, url_for, request, session

app=Flask(__name__)
app.secret_key="session"

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        balance=session["balance"]
    except KeyError:
        balance=session["balance"]=8000
        session["transac"]=5
    
    if request.method=="GET":
        return render_template("index.html", balance=balance, msg="Welcome to the bank")

    if request.method=="POST":
        if session["transac"]>0:
            session["transac"]-=1
            # print("--------------------------",int(request.form["amount"]))
            if int(request.form["amount"])<0:
                return render_template("index.html", balance=balance, msg="Negative amount not allowed")
            elif int(request.form["amount"])>5000:
                return render_template("index.html", balance=balance, msg="5000 greater")
            else:
                if request.form["action"]=="Deposit":
                    balance+=int(request.form["amount"])
                    return render_template("index.html", balance=balance, msg="Deposited")
                if request.form["action"]=="Withdraw":
                    balance+=int(request.form["amount"])
                    return render_template("index.html", balance=balance, msg="Withdrawn")
        else:
            return render_template("index.html", balance=balance, msg="No more than five transactions")

if __name__=="__main__":
    app.run(debug=True)