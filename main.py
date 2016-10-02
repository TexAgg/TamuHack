#! /usr/bin/python
import json
from flask import Flask,request,render_template
import requests
from firebase import firebase
import json
from hackgetter import hackgetter
import math
import hashlib
from sender import sender

from flask import Flask
app = Flask(__name__)

# pls dont steal database secret.
db = firebase("https://tamuhack-62a7e.firebaseio.com/", "9aPTl5HogP4eHdKHdNhRWqiFH5WkOW1HeHrN30gD")
result = [' ',' ',' ',' ',' ']
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
			"hacks": hacks,
			"members":"",
			"full":False
		}

		# hash the email adress to get a valid json key
		db.pat(path = "/users/" + hacks + "/" + hashlib.sha224(email).hexdigest(), payload = json.dumps(query))

		print email
		print hacks
		calculateall()
		return render_template("return.html")
	
@app.route("/nearby", methods = ['GET'])
def nearby():
	if "Hackathon" in request.args:
		hacks = request.args.get('Hackathon')
		results = db.get("/users/" + hacks)
		#return json.dumps(results)
		return render_template("nearby.html", results = results)
	else:
		c = hackgetter()
		c.download_html("https://mlh.io/seasons/na-2017/events")
		events = c.get_hackathons()
		return render_template("choose_hack.html", Events=events)


def calculateall():
	match(separate())

def separate():
	keys = []
	groups ={}
	users = db.get("/users/")

	#this is what u do
	for key,value in users.iteritems():
		keys.append(key)
		

	for k in keys:
		for key,value in users[k].iteritems():
			groups[value['hacks']] = []
	for k in keys:
		for key,value in users[k].iteritems():
			for key1, value1 in groups.iteritems():
				if (key1 == value['hacks']):
					print key1
					groups[key1].append(value)
	
					
	for key,value in groups.iteritems():
		print groups[key] 		

	for key,value in groups.iteritems():
		print key
		print value
	
	return groups

def match(groups):
	print " "
	for x in range(len(groups)):
		match2(groups.values()[x])
	
def match2(lod):
	print'\n'
	for x in range(int(math.ceil(float(len(lod))/4))):
		a = {
		    "Names":[ lod[0]['name'],lod[1]['name'],lod[2]['name'],lod[3]['name']],
		    "Emails": [ lod[0]['email'],lod[1]['email'],lod[2]['email'],lod[3]['email']]
		}

		db.put("/users/"+lod[0]['hacks']+"/"+hashlib.sha224(lod[0]['email']).hexdigest()+"/", payload = json.dumps({"members":a}))
		db.put("/users/"+lod[1]['hacks']+"/"+hashlib.sha224(lod[1]['email']).hexdigest()+"/", payload = json.dumps({"members":a}))
		db.put("/users/"+lod[2]['hacks']+"/"+hashlib.sha224(lod[2]['email']).hexdigest()+"/", payload = json.dumps({"members":a}))
		db.put("/users/"+lod[3]['hacks']+"/"+hashlib.sha224(lod[3]['email']).hexdigest()+"/", payload = json.dumps({"members":a}))

		b = lod[0]['name']+"   "+lod[0]['email']+"\n"+lod[1]['name']+"   "+lod[1]['email']+"\n"+lod[2]['name']+"   "+lod[2]['email']+"\n"+lod[3]['name']+"   "+lod[3]['email']+"\n"
		

		c = sender("Here is your team: \n"+b,lod[0]['email'])
		c.sendEmail()
		c = sender("Here is your team: \n"+b,lod[1]['email'])
		c.sendEmail()
		c = sender("Here is your team: \n"+b,lod[2]['email'])
		c.sendEmail()
		c = sender("Here is your team: \n"+b,lod[3]['email'])
		c.sendEmail()

	for x in range (0,4):
		lod.pop(0)

if __name__ == "__main__":
	#db.put("/users/HackTX/-KT2jHBWPPb1_0uXMD6-/", payload = json.dumps({"members":"gigem@gmail,com \n asddssd"}))
	#print "hi"
	app.run()
	
