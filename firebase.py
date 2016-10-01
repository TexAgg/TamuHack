import requests
import urllib

class firebase:
	def __init__(self, url, secret):
		self.url = url
		self.secret = secret
	
	def push(self, path, payload):
		requests.request("POST", self.url + path + ".json", params={"auth":self.secret}, data = payload)
	def get(self, path):
		r = requests.request("GET", self.url + path + ".json", params={"auth":self.secret})
		return r.json()