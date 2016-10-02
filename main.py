#! /usr/bin/python
import json
from flask import Flask,request,render_template
import requests
from firebase import firebase
import json
from hackgetter import hackgetter

from flask import Flask
app = Flask(__name__)

# pls dont steal database secret.
db = firebase("https://tamuhack-62a7e.firebaseio.com/", "9aPTl5HogP4eHdKHdNhRWqiFH5WkOW1HeHrN30gD")

@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html")


@app.route("/login", methods = ['GET','POST'])
def login(Events=None):
	if request.method == "GET":
		c = hackgetter()
		c.download_html("https://mlh.io/seasons/na-2017/events")
		events = c.get_hackathons()
		return render_template('login.html',Events=events)
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

		db.push(path = "/users/" + hacks, payload = json.dumps(query))

		print email
		print hacks
		return render_template("return.html")
	
@app.route("/nearby", methods = ['GET'])
def nearby():
	if "Hackathon" in request.args:
		hacks = request.args.get('Hackathon')
		results = db.get("/users/" + hacks)
		return json.dumps(results)
		#return render_template("nearby.html", results = results)
	else:
		c = hackgetter()
		c.download_html("https://mlh.io/seasons/na-2017/events")
		events = c.get_hackathons()
		return render_template("choose_hack.html", Events=events)



if __name__ == "__main__":
    app.run()
