import sqlite3
import datetime
import time
from Stand import Stand
from Journal import Journal

class BD:
    def __init__(self,nomBD):
        self.nomBD=nomBD

    def Init(self):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="CREATE TABLE STAND(id INTEGER PRIMARY KEY,nom TEXT,prix INTEGER)"
        curseur.execute(sql1)
        sql2="CREATE TABLE JOURNAL(id INTEGER PRIMARY KEY,date TEXT,idStand INTEGER,recette INTEGER, FOREIGN KEY(idStand) REFERENCES STAND(id))"
        curseur.execute(sql2)
        conn.commit()
        courseur.close()
        conn.close()

    def NStand(self,stand):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        sql1="INSERT INTO STAND VALUES(?,?)"
        curseur.execute(sql1,stand.getNom(),stand.getPrix())
        conn.commit()
        curseur.close()
        conn.close()

    def addjournal(self,journal):
        conn=sqlite3.connect(self.nomBD)
        curseur=conn.cursor()
        j=journal.getJournal()
        for id,recette in journal.items():
            sql1="INSERT INTO JOURNAL VALUES(?,?,?)"
            curseur.execute(sql1,journal.getDate(),id,recette)
        conn.commit()
        curseur.close()
        conn.close()
























            
