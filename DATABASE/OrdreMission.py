import sqlite3

class OrdreDeMission:
     def __init__(self):
        
        self.Chauffeur = "init"
        self.Graisseur = "init"
        self.DateDepart ="JJ-MM-AAAA//HH:MM"
        self.ChantierDepart="init"
        self.ChantierArrivee="init"
        self.NatureTrasport="init"

        
     def sauvgarde_Ordre(self):
        donnees = [ self.Chauffeur, self.Graisseur,self.DateDepart,self.ChantierDepart,self.ChantierArrivee,self.NatureTrasport]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Ordres_Mission(Chauffeur, Graisseur,DateDepart,ChantierDepart,ChantierArrivee,NatureTrasport) VALUES (?,?,?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Ordre Mission reussi")