#! /usr/bin/python
import json
from flask import Flask,request,render_template
import requests

from flask import Flask
app = Flask(__name__)

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

		print email
		print hacks
		return "done"
	



if __name__ == "__main__":
    app.run()
