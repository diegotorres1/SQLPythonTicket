#Author: Diego Torres
#Date Modified: 2/14/18
#Program Description: Keep track of complete information
#       currently held in a queue of inputs for the db
#Can hold information about the ticket
import MySQLdb

class DataSheet:
	def __init__(self, firstName, lastName, age, gender,ticket):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.gender = gender
		self.ticket =  ticket

	def getFirstName(self):
		return self.firstName
	def getLastName(self):
		return self.lastName
	def getAge(self):
		return self.age
	def getGender(self):
		return self.gender
	def getTicket(self):
                return self.ticket

