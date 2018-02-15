#Author: Diego Torres
#Date Modified: 2/14/18
#Author: Diego Torres
#Program Description: Program implements ticketing system with mysql
#       and tkinter. Old programming assignement with addition of
#       databases and a GUI. Program is used to keep track of tickets
#       ordered for airplane. Information is then inputted and sent to
#       the db for storage.
import MySQLdb
from Tkinter import *
from Business import Business
from Economy import Economy
from First import First
from TicketGUI import TicketGUI
#3 types of tickets Economy, Business, First
def main():
        
	print("TicketMain")

        #Connect to DataBase
	db = MySQLdb.connect(host = "localhost", user = "root", passwd = "protonic", db = "plane")

	#Make ticket tracker objects
	bus = Business()
	econ = Economy()
	first = First()

	#Create GUI
	root = Tk()
	gui = TicketGUI(root,bus,econ,first,db)

	#Enter Main Loop
	root.mainloop()

	#Terminte Program
	root.destroy()
	db.close()
	
	
if __name__ == "__main__":
	main()
