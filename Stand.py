class Stand:
    def __init__(self,id,nom,prix):
        self.id=id
        self.nom=nom
        self.prix=prix

    def getId(self):
        return self.id

    def getNom (self):
        return self.nom

    def getPrix (self):
        return self.prix

    def setNom (self,n):
        self.nom=n

    def setPrix (self,n):
        self.prix=n
