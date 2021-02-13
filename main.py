import sqlite3
import datetime
import time
from Stand import Stand
from Journal import Journal
from DataBase import BD
from tkinter import *
from tkinter import messagebox 


bd=BD("vitaBD.sql")
list_stands=bd.listStands()
agenda=bd.Agenda()

def Home():
    global homePage
    homePage= Toplevel()
    homePage['bg']='IndianRed2'
    
    label = Label(homePage, text="Bienvenue Mr.Mahjoub",bg='IndianRed2',fg="brown4")
    label.config(font=("Times New Roman",60,"bold"))
    label.pack(pady=5)

    ag=Button(homePage, text="Agenda", bg="tomato4", fg="IndianRed2", height=2,width=10)
    ag.pack(side=TOP,pady=15)
    ag.config(font=("Times New Roman",40,"bold"))
    #ag.config(command = agenda_interf)

    gs=Button(homePage, text="Gestion des \nStands", bg="tomato4", fg="IndianRed2", height=2,width=10)
    gs.pack(side=TOP,pady=15)
    gs.config(font=("Times New Roman",40,"bold"))
    gs.config(command = stand_interf)

    stat=Button(homePage, text="Statistique", bg="tomato4", fg="IndianRed2", height=2,width=10)
    stat.pack(side=TOP,pady=15)
    stat.config(font=("Times New Roman",40,"bold"))
    #stat.config(command = stat_interf)

    homePage.mainloop()

#Gestion des Stands 
def stand_interf():
    homePage.destroy()

    global st_interf
    st_interf=Toplevel()
    st_interf['bg']='IndianRed2'

    label = Label(st_interf, text="Gestion des Stands",bg='IndianRed2',fg="brown4")
    label.config(font=("Times New Roman",60,"bold"))
    label.pack(pady=5)

    ls=Button(st_interf, text="Liste des \nStands", bg="tomato4", fg="IndianRed2", height=2,width=15)
    ls.pack(side=TOP,pady=15)
    ls.config(font=("Times New Roman",40,"bold"))
    ls.config(command = affStands)

    cs=Button(st_interf, text="Création de \nStand", bg="tomato4", fg="IndianRed2", height=2,width=15)
    cs.pack(side=TOP,pady=15)
    cs.config(font=("Times New Roman",40,"bold"))
    cs.config(command = nstand)

    ms=Button(st_interf, text="Modification d'un\nStand", bg="tomato4", fg="IndianRed2", height=2,width=15)
    ms.pack(side=TOP,pady=15)
    ms.config(font=("Times New Roman",40,"bold"))
    ms.config(command = Mstand)

    st_interf.mainloop()

#nouveau stand
def nstand():
    st_interf.destroy()

    global ns_interf
    ns_interf=Toplevel()
    ns_interf['bg']='IndianRed2'

    label = Label(ns_interf, text="Nouveau Stand",bg='IndianRed2',fg="brown4")
    label.config(font=("Times New Roman",40,"bold"))
    label.pack(pady=5)

    label2 = Label(ns_interf, text="Merci de nous fournir les information de ce nouveau stand",bg='IndianRed2',fg="brown3")
    label2.config(font=("Times New Roman",12,"bold"))
    label2.pack(pady=5)
    
    global nom
    nom=Entry(ns_interf,width= 70, textvariable=DoubleVar(), bg='tomato4', fg="IndianRed2")
    nom.insert(0,"Nom du stand")
    nom.config(font=("Times New Roman", 25,"bold"))
    nom.pack(pady=20)

    global prix
    prix=Entry(ns_interf,width= 70, textvariable=DoubleVar(), bg='tomato4', fg="IndianRed2")
    prix.insert(0,"Merci de nous fournir le nom de stand")
    prix.config(font=("Times New Roman", 25,"bold"))
    prix.pack(pady=20)

    creation=Button(ns_interf, text="Création", bg="tomato4", fg="IndianRed2", height=1,width=10)
    creation.pack(side=TOP,pady=15)
    creation.config(font=("Times New Roman",40,"bold"))
    creation.config(command = creationstand)
    
    s=Button(ns_interf,text="Annuler",bg="tomato4", fg="IndianRed2", height=1,width=10)
    s.pack(pady=10,side=BOTTOM)
    s.config(font=("Times New Roman",30,"bold"))
    s.config(command =exit1)
    
    ns_interf.mainloop()

def exit1():
    ns_interf.destroy()
    Home()
def creationstand():
    s=Stand(len(list_stands),nom.get(),getint(prix.get()))
    list_stands.append(s)
    bd.addStand(s)
    ns_interf.destroy()
    Home()

#afficherstands
def affStands():
    st_interf.destroy()

    global affs_interf
    affs_interf=Toplevel()
    affs_interf['bg']='IndianRed2'

    label = Label(affs_interf, text="Liste des stands",bg='IndianRed2',fg="brown4")
    label.config(font=("Times New Roman",40,"bold"))
    label.pack(pady=20)

    for i in range(0,len(list_stands)):
        info(list_stands[i])

    s=Button(affs_interf,text="Menu",bg="tomato4", fg="IndianRed2", height=1,width=10)
    s.pack(pady=10,side=BOTTOM)
    s.config(font=("Times New Roman",30,"bold"))
    s.config(command =exit)

def exit():
    affs_interf.destroy()
    Home()

def info(stand):
    s=Button(affs_interf,text=stand.getNom(),bg="tomato4", fg="IndianRed2", height=1,width=10)
    s.pack(pady=10,padx=10)
    s.config(font=("Times New Roman",40,"bold"))
    s.config(command =lambda:message(stand))

def message(stand):
    messagebox.showinfo(stand.getNom(),"\tNom:"+stand.getNom()+"\n\tLe prix de la location :"+str(stand.getPrix())+"\n\tMaximum Recette de tout le temps:"+"-"+"\n\tMaximum Recette dans ce mois"+"-")

#Modification de stand
def Mstand():
    st_interf.destroy()

    global ms_interf
    ms_interf=Toplevel()
    ms_interf['bg']='IndianRed2'

    label = Label(ms_interf, text="Choisir un stand à modifier",bg='IndianRed2',fg="brown4")
    label.config(font=("Times New Roman",40,"bold"))
    label.pack(pady=20)

    s=Button(ms_interf,text="Menu",bg="tomato4", fg="IndianRed2", height=1,width=10)
    s.pack(pady=10,side=BOTTOM)
    s.config(font=("Times New Roman",30,"bold"))
    s.config(command =exit3)

    ms_interf.mainloop()
    

def exit3():
    ms_interf.destroy()
    Home()
    
Home()
