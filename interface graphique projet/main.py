from tkinter import *
from fonctionstableaux import *
import fenetre as fenetre 
import os


 
screen = Tk()
screen.geometry("830x500")
screen.title("Projet Scouts")
heading = Label(text = "Tableaux de renseignements", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()


 

 
register = Button(screen,text = "Nutons", width = "10", height = "2", command = tab_nutons, bg = "grey")
register.place(x = 10, y = 60)

register = Button(screen,text = "Lutins", width = "10", height = "2", command = tab_lutins, bg = "grey")
register.place(x = 85, y = 60)

register = Button(screen,text = "Louveteaux", width = "10", height = "2", command = tab_louveteaux, bg = "grey")
register.place(x =160, y = 60)

register = Button(screen,text = "Guides", width = "10", height = "2", command = tab_guides, bg = "grey")
register.place(x = 235, y = 60)

register = Button(screen,text = "Scouts", width = "10", height = "2", command = tab_scouts, bg = "grey")
register.place(x = 310, y = 60)

register = Button(screen,text = "Pionniers", width = "10", height = "2", command = tab_pionniers, bg = "grey")
register.place(x = 385, y = 60)

register = Button(screen,text = "Chefs", width = "10", height = "2", command = tab_chefs, bg = "grey")
register.place(x = 460, y = 60)

Inscription = Button(screen,text = "Inscription", width = "30", height = "2",command= lambda : os.system("fenetre.py"), bg = "grey")
Inscription.place(x = 600, y = 60)
screen.mainloop()
