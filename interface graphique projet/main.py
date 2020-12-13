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


prenomt = Label(text = "PRENOM ",)
prenomt.place(x = 10, y = 120)

nomt = Label(text = "NOM ",)
nomt.place(x = 100, y = 120)


anneet = Label(text = "ANNEE ",)
anneet.place(x = 175, y = 120)

mailt = Label(text = "MAIL",)
mailt.place(x = 275, y = 120)

addrt = Label(text = "ADDRESSE ",)
addrt.place(x = 355, y = 120)


statutt = Label(text = "STATUT ",)
statutt.place(x = 425, y = 120)

sectiont = Label(text = "SECTION",)
sectiont.place(x = 495, y = 120)

screen.grid_rowconfigure(0, weight=1)
screen.grid_columnconfigure(0, weight=1)

## Le canvas
cnv = Canvas(screen)
cnv.grid(row=0, column=0, sticky='nswe')

## Les scrollbars
hScroll = Scrollbar(screen, orient=HORIZONTAL, command=cnv.xview)
hScroll.grid(row=1, column=0, sticky='we')

vScroll = Scrollbar(screen, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')

cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)

## Le Frame, dans le Canvas, mais sans pack ou grid
frm = Frame(cnv)
## Les labels et entrys dans le frame
for i in range(50):
 Label(frm, text='Label%s: ' % i).grid(row=i, column=0)
 Entry(frm).grid(row=i, column=1)
## Pour etre sur que les dimensions sont calculées
frm.update()

## Création de la window dans le Canvas
cnv.create_window(0, 0, window=frm, anchor=NW)

## La scrollregion est la boite englobante pour tout ce qu'il y a dans le Canvas
cnv.configure(scrollregion=cnv.bbox(ALL))
screen.mainloop()
