# /usr/bin/python

import smtplib

class sender:

	def __init__(self,message,reciever):
		self.__message__ = message
		self.__reciever__ = reciever
	
	def sendEmail(self):
		smtpObj = smtplib.SMTP('smtp.gmail.com',587)
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login('hackrteam@gmail.com', '244466666')
		print smtpObj.sendmail('hackrteam@gmail.com', self.__reciever__,'Subject:Team Made! \n'+self.__message__)

if __name__ =="__main__":
	c = sender("Hey this is an automated voice message.","kevinzuang@gmail.com")
	c.sendEmail()
