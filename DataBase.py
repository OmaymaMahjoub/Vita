import sqlite3
import datetime
import time
from Stand import Stand
from Journal import Journal

class BD:

    def __init__(self,nomBD):
        self.nomBD=nomBD

    #Initialisation des BD
    def INIT(self):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="CREATE TABLE STAND(id INTEGER PRIMARY KEY, nom TEXT,prix INTEGER)"
        curseur.execute(sql1)
        sql2="CREATE TABLE JOURNAL(id INTEGER PRIMARY KEY,day TEXT,id_stand INTEGER, recette INTEGER, FOREIGN KEY(id_stand) REFERENCES STAND(id))"
        curseur.execute(sql2)
        conn.commit()
        curseur.close()
        conn.close()

    #ADD
    def addStand(self,stand):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="INSERT INTO STAND VALUES(?,?,?)"
        curseur.execute(sql1,[stand.getId(),stand.getNom(),stand.getPrix()])
        conn.commit()
        curseur.close()
        conn.close()

    def addJournal(self,journal):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        j=journal.getJournal()
        d=journal.getDate()
        i=journal.getId()
        for s,r in j.items():
            sql1="INSERT INTO JOURNAL VALUES(?,?,?,?)"
            curseur.execute(sql1,[i,d,s,r])
            i+=1
        conn.commit()
        curseur.close()
        conn.close()
        
    #GET
    def listStands(self):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="SELECT * FROM STAND"
        curseur.execute(sql1)
        l=curseur.fetchall()
        stands=[]
        for i in range(0,len(l)):
            s=Stand(l[i][0],l[i][1],l[i][2])
            stands.append(s)
        curseur.close()
        conn.close()
        return stands


    def Agenda(self):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="SELECT * FROM JOURNAL"
        curseur.execute(sql1)
        l=curseur.fetchall()
        agenda=[]
        days=[]
        for i in range (0,len(l)):
            if (i==0):
                id=0
                h=[x for x in l if x[1]==l[0][1]]
                days.append(l[0][1])
            elif l[i][1] in days:
                continue
            else:
                id=l[i][0]
                h=[x for x in l if x[1]==l[i][1]]
                days.append(l[i][1])
            journal={}
            for j in range(0,len(h)):
                journal[h[j][2]]=h[j][3]
            agenda.append(Journal(id,h[0][1],journal))
        curseur.close()
        conn.close()
        return agenda

    #Update
    def updateStand(self,id,stand):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="UPDATE STAND SET nom=? , prix=? WHERE id=?"
        curseur.execute(sql1,[stand.getNom(),stand.getPrix(),id])
        curseur.close()
        conn.close()

    def updateJournal(self,id,date,standId,recette):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="INSERT INTO JOURNAL VALUES(?,?,?,?)"
        curseur.execute(sql1,[id,date,standId,recette])
        curseur.close()
        conn.close()

















        
















    











        






















        
