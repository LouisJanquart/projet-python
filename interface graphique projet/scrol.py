from tkinter import *
from fonctionstableaux import *
import fenetre as fenetre 
import os

## La fenetre, avec les options de grille qui vont bien
root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


## Le canvas
cnv = Canvas(root)
cnv.grid(row=0, column=0, sticky='nswe')

## Les scrollbars
hScroll = Scrollbar(root, orient=HORIZONTAL, command=cnv.xview)
hScroll.grid(row=1, column=0, sticky='we')

vScroll = Scrollbar(root, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=1, sticky='ns')

cnv.configure(xscrollcommand=hScroll.set, yscrollcommand=vScroll.set)

## Le Frame, dans le Canvas, mais sans pack ou grid
frm = Frame(cnv)
## Les labels et entrys dans le frame#########################################################################################################################################################################
register = Button(root,text = "Nutons", width = "10", height = "2", command = tab_nutons, bg = "grey")
register.place(x = 00, y = 0)

register = Button(root,text = "Lutins", width = "10", height = "2", command = tab_lutins, bg = "grey")
register.place(x = 75, y = 0)

register = Button(root,text = "Louveteaux", width = "10", height = "2", command = tab_louveteaux, bg = "grey")
register.place(x =150, y = 0)

register = Button(root,text = "Guides", width = "10", height = "2", command = tab_guides, bg = "grey")
register.place(x = 225, y = 0)

register = Button(root,text = "Scouts", width = "10", height = "2", command = tab_scouts, bg = "grey")
register.place(x = 300, y = 0)

register = Button(root,text = "Pionniers", width = "10", height = "2", command = tab_pionniers, bg = "grey")
register.place(x = 375, y = 0)

register = Button(root,text = "Chefs", width = "10", height = "2", command = tab_chefs, bg = "grey")
register.place(x = 450, y = 0)

Inscription = Button(root,text = "Inscription", width = "30", height = "2",command= lambda : os.system("fenetre.py"), bg = "grey")
Inscription.place(x = 590, y = 0)



###################################################################################################################################################################################
for i in range(1):
 Label(frm, text='NUMERO').grid(row=i+4, column=0)
 Label(frm, text='PRENOM ').grid(row=i+4, column=1)
 Label(frm, text='NOM ' ).grid(row=i+4, column=2)
 Label(frm, text='ANNEE ' ).grid(row=i+4, column=3)
 Label(frm, text='MAIL ' ).grid(row=i+4, column=4)
 Label(frm, text='ADDRESSE ' ).grid(row=i+4, column=5)
 Label(frm, text='STATUT ' ).grid(row=i+4, column=6)
 Label(frm, text='SECTION ' ).grid(row=i+4, column=7)
 
for i in range(50):
 Label(frm, text='' ).grid(row=i, column=10)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=0)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=1)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=2)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=3)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=4)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=5)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=6)
 Label(frm, text='Label%s: ' % i).grid(row=i+5, column=7)

 
## Pour etre sur que les dimensions sont calculées
frm.update()

## Création de la window dans le Canvas
cnv.create_window(15, 75, window=frm, anchor=NW)

## La scrollregion est la boite englobante pour tout ce qu'il y a dans le Canvas
cnv.configure(scrollregion=cnv.bbox(ALL))

## C'est parti!
root.mainloop()