from flask import Flask, redirect, render_template, request, url_for,request
import time
import re

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
	if request.method == "GET":
		return render_template("index.html")


	if request.method == "POST":

		try:
			time.strptime(request.form["dob"], "%d/%m/%Y")

		except ValueError:
			msg = "****date is invalid****"
			return render_template("index.html",msg=msg)

		usn_pattern = "^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"
		if not re.match(usn_pattern, request.form["usn"]):
			msg="***usn is invalid***"
			return render_template("index.html",msg=msg)


		s = (int(request.form["m1"])+int(request.form["m2"])+int(request.form["m3"]))/3

		msg= "Average marks is:" + str(s)
		return render_template("success.html",res=msg)

if __name__ == "__main__":
	app.run(debug=True)
