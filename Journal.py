import datetime
import time

class Journal:
    def __init__(self,id,date,j={}):
        self.id=id
        self.date=date
        self.journal=j

    def getId(self):
        return self.id
    
    def getJournal(self):
        return self.journal

    def getDate(self):
        return self.date

    def getRecette(self,standId):
        if ((standId in self.journal)==False):
            return -1
        return self.journal[standId]
    
    def addRecette(self,standId,recette):
        self.journal[standId]=recette

    def total (self):
        s=0
        for j in self.journal.values(): 
            s+=j
        return s

    
