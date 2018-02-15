#Author: Diego Torres
#Date Modified: 2/14/18
#Author: Diego Torres
#GUI class
#Handles the interface for the ticket System
#       aswell as triggers input information
#       the db
from Tkinter import *
from Queue import *
from DataSheet import *
class TicketGUI:
	#Take information from state of GUI to determine
	#the information processed
	def processRequest(self,num):
		print("Is there a ticket!")
		#Which message to display on window
		switcher = {
			0: "Business Ticket is selected",
			1: "Economy Ticket is selected",
			2: "First Class Ticket is selected",
			4: "Order is placed",
			5: "Added to order"
		
		}
		message = switcher.get(num,"None are Selected")
		#Get number of orders for ticket type
		if(num != 5 | num != 4):
			self.selectNum = num
		if(num == 5):
			if(self.selectNum == 0):
				print("Adding Business Order")
				self.business.addCount(self.w.get())
				self.messageCheckout += "\n %d : Business" % self.business.count
				self.currentOrderLabel.config(text= self.messageCheckout)
			elif(self.selectNum == 1):
				print("Adding Economy Order")
				self.economy.addCount(self.w.get())
				self.messageCheckout += "\n %d : First" % self.economy.count
				self.currentOrderLabel.config(text= self.messageCheckout)
			elif(self.selectNum == 2) :
				print("Adding First Class Order")
				self.first.addCount(self.w.get())
				self.messageCheckout += "\n %d : First" % self.first.count
				self.currentOrderLabel.config(text= self.messageCheckout)
			else:
				message = "None have been selected"

		
		
		self.ticketLabel2.config(text=message)
	#CREATE GUI for the plane app
	def __init__(self,master,business,economy,first,db):
		self.master = master
		self.business = business
		self.economy = economy
		self.first = first
		self.db = db
		print("TicketGUI is created")
		requestTicket = lambda buttonChoice: self.processRequest(buttonChoice)
		master.minsize(width=500, height=300)
		master.maxsize(width=500, height=300)
		frame = Frame(master)
		self.messageCheckout = "--------"
		
		frame2 = Frame(master)
		frame.pack()
		frame2.pack()
	#ticketLabel
		self.ticketLabel2 = Label(frame2, text="Nothing Selected",bd = 30)
		self.ticketLabel2.pack(side = LEFT)
	#currentOrderLabel
		self.currentOrderLabel = Label(frame2, text = "Nothing in Checkout",bd = 30)
		self.currentOrderLabel.pack(side = LEFT)
	#recieptLabel
		self.ticketLabel3 = Label(frame2, text="Receipt\nNothing to show\n...\n...",bd = 30)
		self.ticketLabel3.pack(side = LEFT)
	#quit button
		self.quitButton = Button(frame, text="QUIT", fg="red", command=frame.quit)
		self.quitButton.pack(side=LEFT)
	#businessButton
		self.businessButton = Button(frame, text="Business", command=lambda:requestTicket(0))
		self.businessButton.pack(side=LEFT)
	#economyButton
		self.economyButton = Button(frame, text="Economy", command=lambda:requestTicket(1))
		self.economyButton.pack(side=LEFT)
	#firstButton
		self.firstButton = Button(frame, text="First", command=lambda:requestTicket(2))
		self.firstButton.pack(side=LEFT)
	#slider value
		self.w = Scale(master, from_=0, to=20,orient = HORIZONTAL)
		self.w.pack(side = BOTTOM)
	#orderButton
		self.orderButton = Button(master, text="Order",command=self.messageWindow)
		self.orderButton.pack(side = BOTTOM)
	#addToOrder
		self.addButton = Button(master, text = "Add To Order", command = lambda:requestTicket(5))
		self.addButton.pack(side = BOTTOM)
	#messageWindow
	def messageWindow(self):
                
                cur = self.db.cursor()
                sql_message = "SELECT COUNT(*) FROM PLANE"
                print 'MESSAGE OF SQL: ' + sql_message
                try:
                        #execute the sql command
                        cur.execute(sql)
                        #commit changes
                        self.db.commit()
                except:
                        #handle if there is an error
                        print "There is an error"
                        self.db.rollback()
                for row in cur.fetchall():
                        val =   int(row)
                #execute SQL query
                if ((business.count + economy.count + first.count) < 100-val):
                        self.win.quit()
		if (self.business.count == 0 | self.economy.count == 0 | self.first.count == 0):
			return 1
		
		# create child window
		self.win = Toplevel()
		# display message
		message = "Information Sheet"
		Label(self.win, text=message).pack()
		#Get current ticket type from ticket objects
		
		# quit child window and return to root window
		# the button is optional here, simply use the corner x of the child window
		self.eFirstName = Entry(self.win)
		self.eLastName = Entry(self.win)
		self.eAge = Entry(self.win)
		self.eGender = Entry(self.win)
		self.enterButton = Button(self.win, text = "Submit Information", command = self.submitInfo)

		self.eFirstName.pack()
		self.eLastName.pack()
		self.eAge.pack()
		self.eGender.pack()
		self.enterButton.pack()
		

		self.eFirstName.insert(0, "first name")
		self.eLastName.insert(0, "last name")
		self.eAge.insert(0, "age")
		self.eGender.insert(0, "gender")

		#Generate the queue
		self.q = Queue()
		#createTickets for business
		for i in range(0, self.business.count):
			datasheet = DataSheet("FIRST", "LAST", "AGE", "GENDER", "business")
			self.q.put(datasheet)
		#createTickets for economy
		for i in range(0,self.economy.count):
			datasheet = DataSheet("FIRST", "LAST", "AGE", "GENDER", "economy")
			self.q.put(datasheet)
		#createTickets for first
		for i in range(0,self.first.count):
			datasheet = DataSheet("FIRST", "LAST", "AGE", "GENDER", "first")
			self.q.put(datasheet)
		if(self.q.empty()):
			self.win.quit()
			

	def submitInfo(self):
		
		#retrieve the data from entry widgets
		self.firstName = self.eFirstName.get()
		self.lastName = self.eLastName.get()
		self.age = self.eAge.get()
		self.gender = self.eGender.get()

		#Take from queue
		if(not self.q.empty()):
			datasheet = self.q.get()
		ticket = datasheet.getTicket()

		#check if string is less than limit
		if(len(self.firstName) < 30 and len(self.lastName) < 30 and len(self.age) < 10 and len(self.gender) < 10):
			#All of the parameters are of right size
			self.cur = self.db.cursor()
			sql = "INSERT INTO PLANE (FIRST_NAME, LAST_NAME, AGE, GENDER, TICKET) VALUES ('%s','%s','%s','%s','%s')" %(self.firstName,self.lastName,self.age, self.gender, ticket)
			print 'MESSAGE OF SQL: ' + sql
			try:
				#execute the sql command
				self.cur.execute(sql)
				#commit changes
				self.db.commit()
			except:
				#handle if there is an error
				print "There is an error"
				self.db.rollback()
			#execute SQL query

		if(self.q.empty()):
			self.win.quit()

				
		
		


		
		
		
			
			
			
	

	


		
		
