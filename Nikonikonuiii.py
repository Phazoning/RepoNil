from tkinter import *
import mysql.connector
import system

kappaUser = 0
kappaPassword = 0
kappaDatabase = 0
def intro():
	Master = Tk()
	Label(Master, text = "Nombre de Usuario").grid(row=0)
	Label(Master, text = "Contraseña").grid(row=1)
	
	en1 = Entry(Master)
	en2 = Entry(Master)
	
	en1.grid(row=0, column=1)
	en2.grid(row=1, column=1)
	
	Button(Master, text = "input", command = data(en1, en2, Master).grid(row=4, column=0, sticky=W, pady=4)
	Button(Master, text = "exit", command = sys.exit).grid(row=4, column=0, sticky=W, pady=4)
	
	Master = Tk()
	Label(Master, text 
	
	mainloop()
	
def data(input1, input2):
	check = False
	while check == False:
		try:
			kappaDatabase = mysql.connector.connect(host="localhost", user=str(en1), password=str(en2))
			kappaUser, kappaPassword = en1, en
			check = True
		except:
			print "No se ha podido acceder, nombre de usuario o contraseña incorrectos"
	


