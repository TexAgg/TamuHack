#! /usr/bin/python
import json
from flask import Flask,request,render_template
import requests
from firebase import firebase
import json

from flask import Flask
app = Flask(__name__)

# pls dont steal database secret.
db = firebase("https://tamuhack-62a7e.firebaseio.com/", "9aPTl5HogP4eHdKHdNhRWqiFH5WkOW1HeHrN30gD")

@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html")
@app.route("/login", methods = ['GET','POST'])
def login():
	if request.method == "GET":
		return render_template('login.html')
	elif request.method == "POST":
		name = request.form['FullName']
		email = request.form['Email']
		phone = request.form['Phone']
		password = request.form['Password']
		skills = request.form['Skills']
		hacks = request.form['Hackathon']

		query = {
			"name": name,
			"email": email,
			"phone": phone,
			"password": password,
			"skills": skills,
			"hacks": hacks
		}

		db.push(path = "/users", payload = json.dumps(query))

		print email
		print hacks
		return "done"
	



if __name__ == "__main__":
    app.run()
