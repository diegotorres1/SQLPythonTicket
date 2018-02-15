#Author: Diego Torres
#Date Modified: 2/14/18
#Program Description: Keep track of tickets that are
#       are of type Economy
class Economy:
	def __init__(self):
		print("Economy is created")
		self.cost = 50.00
		self.count = 0
	
	def displayCost(self):
		print "%d" % self.cost
	#Number of type of tickets
	def addCount(self, count):
		self.count = self.count + count
	
	
	
