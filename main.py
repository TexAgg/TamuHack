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
@app.route("/login")
def login():
	return render_template("login.html")
if __name__ == "__main__":
    app.run()
