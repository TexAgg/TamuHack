import requests
import urllib

class firebase:

	# Create a firebase object with a url and a database secret.
	def __init__(self, url, secret):
		self.url = url
		self.secret = secret
	
	# Push a dict to a path in the database.
	def push(self, path, payload):
		requests.request("POST", self.url + path + ".json", params={"auth":self.secret}, data = payload)

	# Return a dict from a path in the database.
	def get(self, path):
		r = requests.request("GET", self.url + path + ".json", params={"auth":self.secret})
		return r.json()