import sqlite3
from datetime import datetime
import json


class OrdreDeMission:
    def __init__(self):

        self.Chauffeur = "init"
        self.Graisseur = "init"
        self.vehicule = "init"
        self.engin = "init"
        self.remorque = "init"
        self.DateDepart = "JJ-MM-AAAA//HH:MM"
        self.ChantierDepart = "init"
        self.ChantierArrivee = "init"
        self.NatureTrasport = "init"

    def sauvgarde_Ordre(self):
        donnees = [self.Chauffeur, self.Graisseur, self.vehicule, self.engin, self.remorque,
                   self.DateDepart, self.ChantierDepart, self.ChantierArrivee, self.NatureTrasport]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()
        curseur.execute('''
            INSERT INTO Ordres_Mission(Chauffeur,Graisseur, vehicule,engin,remorque,DateDepart,ChantierDepart,ChantierArrivee,NatureTrasport) VALUES (?,?,?,?,?,?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Ordre Mission reussi")

    def print_Ordre(self):
        f = open('User_Log.json',)
        data = json.load(f)
        User_ = data["user"]
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        template = ["#####################################################################################",
                    "             #######        ########         #######        #############",
                    "            #       #       #      #         #      #       #     #     #",
                    "            #       #       #######          #      #       #     #     #",
                    "            #       #       #     #          #      #       #     #     #",
                    "             #######        #      #         #######        #     #     #",
                    "######################################################################################",
                    "Creer le : ///////////////////////////////// "+dt_string,
                    "Utilisateur : ///////////////////////////////// "+User_,
                    "#######################################################################################",
                    "Chauffeur :  ///////////////////////////////// "+self.Chauffeur,
                    "Graisseur : ///////////////////////////////// "+self.Graisseur,
                    "Vehicule :  ///////////////////////////////// "+self.vehicule,
                    "Engin : ///////////////////////////////// "+self.engin,
                    "Remorque : ///////////////////////////////// "+self.remorque,
                    "Date Depart : ///////////////////////////////// "+self.DateDepart,
                    "Chantier de depart : ///////////////////////////////// "+self.ChantierDepart,
                    "Chantier d'arrivee : ///////////////////////////////// "+self.ChantierArrivee,
                    "Nature du transport: ///////////////////////////////// "+self.NatureTrasport,
                    "#####################################################################################"]
        with open('OrdreDeMission.txt', 'w') as f:
         for line in template:
            f.write(line)
            f.write('\n')

def get_latest_ORDM():
        data = ()
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Ordres_Mission ORDER BY code DESC LIMIT 1;")
            data = (row for row in cursor.fetchall())
        
        return list(data)
# print(get_latest_ORDM())
# print(get_table_ORDM()[0][1])