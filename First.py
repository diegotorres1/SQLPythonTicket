#Author: Diego Torres
#Date Modified: 2/14/18
#Program Description: Keep track of tickets that are 
#       ordered of type first.
class First:
	def __init__(self):
		print("First is created")
		self.cost = 200.00
		self.count = 0
	
	def displayCost(self):
		print "%d" % self.cost
	#Number of type of tickets
	def addCount(self, count):
		self.count = self.count + count
	
	
	
