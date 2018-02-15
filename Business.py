#Author: Diego Torres
#Date Modified: 2/14/18
#Program Description: Keep track of tickets that are
#       ordered of type first.
class Business:
	#Base class for Business
	def __init__(self):
		self.cost = 100.00
		self.count = 0
		print("Business object created.")
	
	def displayCost(self):
		print "%d" % self.cost
	#Number of type of tickets
	def addCount(self, count):
		self.count = self.count + count
