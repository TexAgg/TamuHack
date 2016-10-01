#! /usr/bin/python
import requests
from bs4 import BeautifulSoup

class hackgetter:

	def __init__(self):
		pass
	
	def download_html(self, url):
		res = requests.get(url)
		res.raise_for_status()
		file = open('hackhtml.txt','wb')
		file.write('/n')
		file.write(res.text)
	
	def get_hackathons(self):
		file = open('hackhtml.txt','r')
		soup = BeautifulSoup(file.read())
		Events = soup.findAll('h3',{"itemprop":"name"})
		for x in range (len(Events)):
			print(Events[x].getText())
		return Events

if __name__ =="__main__":

	w = hackgetter()
	w.download_html("https://mlh.io/seasons/na-2017/events")
	w.get_hackathons()
