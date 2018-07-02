from tkinter import *
import mysql.connector
import system

def intro():
	Master = Tk()
	Label(Master, text = "Nombre de Usuario").grid(row=0)
	Label(Master, text = "Contraseña").grid(row=1)
	Label(Master, text = "Base de datos".grid(row=2)
	
	en1 = Entry(Master)
	en2 = Entry(Master)
	e3 = Entry(Master)
	
	en1.grid(row=0, column=1)
	en2.grid(row=1, column=1)
	en3.grid(row=2, column=1)
	
	Button(Master, text = "input", command = data(en1, en2, en3).grid(row=4, column=0, sticky=W, pady=4)
	Button(Master, text = "exit", command = sys.exit).grid(row=4, column=0, sticky=W, pady=4)
	       
	kappaUser = 0
	kappaPassword = 0
	kappaDatabase = 0
	base = 0
	
	mainloop()
	
def data(i1, i2, i3):
	check = False
	Essit = 0
	while check == False:
		try:
			lambdaDatabase = mysql.connector.connect(host="localhost", user=str(i1), password=str(i2), database = str(i3))
			kappaUser, kappaPassword = en1, en
			check = True
		except:
			try:
	       			Database = tkSimpleDialog.askstring("No database", "Enter name to create a new one", Parent=Master)
	       			lambdaDatabase = mysql.connector.connect(host="localhost", user=str(en1), password=str(en2))
	       			cursor= lambdaDatabase.cursor()
	       			cursor.execute("CREATE DATABASE " + str(Database))
	       			kappaDatabase = Database
	       			base = lambdaDatabase)
	       		except:
	      			if Essit == 10:
	      				tkMessageBox.FunctionName("No way", "No attempts left, closing...", parent = Master)
	      				sys.close()
	      			else:
	      				Essit += 1
	


