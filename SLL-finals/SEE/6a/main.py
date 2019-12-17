from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", msg="")
    if request.method == "POST":
        if (
            request.form["price1"].isdigit()
            and request.form["price2"].isdigit()
            and request.form["price3"].isdigit()
        ):
            c = (
                int(request.form["price1"])
                + int(request.form["price2"])
                + int(request.form["price3"])
            )
            msg = "Price is " + str(c)
            return render_template("index.html", msg=msg)
        else:
            return render_template("index.html", msg="Enter a valid price")


if __name__ == "__main__":
    app.run(debug=True)
